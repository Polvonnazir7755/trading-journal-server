# -*- coding: utf-8 -*-
"""
QAT'IY TEKSHIRUV: struktura funksiyalari kelajakka qaraydimi?

Usul: bir xil ma'lumotni ikki marta beramiz —
  (a) to'liq tarix
  (b) faqat N-shamgacha kesilgan tarix
Agar N-shamgacha bo'lgan natijalar bir xil bo'lmasa -> LOOK-AHEAD BOR.
"""
from mtf_engine import Bar
from resample_demo import gen_m1, resample
from structure import (find_swings, detect_events, find_fvg,
                       find_order_blocks, mark_mitigation)

raw = gen_m1(14400)
h1 = [Bar(t, o, h, l, c) for t, o, h, l, c in resample(raw, 60)]
print(f"H1 shamlar: {len(h1)}\n")

CUT = int(len(h1) * 0.6)
full, part = h1, h1[:CUT]
fails = 0

def check(name, a, b, keyfn):
    """a = to'liq tarixdan olingan, CUT gacha filtrlangan; b = kesilgan tarixdan."""
    global fails
    ka = [keyfn(x) for x in a]
    kb = [keyfn(x) for x in b]
    ok = ka == kb
    if not ok:
        fails += 1
        extra_a = [x for x in ka if x not in kb][:3]
        extra_b = [x for x in kb if x not in ka][:3]
        print(f"  [XATO] {name}: {len(ka)} vs {len(kb)}")
        if extra_a: print(f"          faqat to'liqda: {extra_a}")
        if extra_b: print(f"          faqat kesikda : {extra_b}")
    else:
        print(f"  [OK]   {name}: {len(ka)} ta element mos")
    return ok

print(f"Kesish nuqtasi: {CUT}-sham\n")

# --- swings ---
sw_full = [s for s in find_swings(full) if s.confirmed_at < CUT]
sw_part = [s for s in find_swings(part) if s.confirmed_at < CUT]
check("find_swings", sw_full, sw_part, lambda s: (s.idx, s.kind, round(s.price, 6)))

# --- events ---
ev_full = [e for e in detect_events(full, find_swings(full)) if e.idx < CUT]
ev_part = [e for e in detect_events(part, find_swings(part)) if e.idx < CUT]
check("detect_events", ev_full, ev_part, lambda e: (e.idx, e.kind, e.direction))

# --- FVG ---
f_full = [z for z in find_fvg(full) if z.idx < CUT]
f_part = [z for z in find_fvg(part) if z.idx < CUT]
check("find_fvg", f_full, f_part, lambda z: (z.idx, z.direction, round(z.top, 6)))

# --- Order Blocks ---
ob_full = [z for z in find_order_blocks(full, detect_events(full, find_swings(full))) if z.idx < CUT]
ob_part = [z for z in find_order_blocks(part, detect_events(part, find_swings(part))) if z.idx < CUT]
check("find_order_blocks", ob_full, ob_part, lambda z: (z.idx, z.direction, round(z.top, 6)))

# --- mitigation (BU YERDA look-ahead BO'LISHI KUTILADI) ---
print("\nMitigatsiya tekshiruvi (kelajakni ishlatishi TABIIY):")
mf = [z for z in find_fvg(full) if z.idx < CUT]
mp = [z for z in find_fvg(part) if z.idx < CUT]
mark_mitigation(mf, full)
mark_mitigation(mp, part)
tapped_full = sum(1 for z in mf if z.tapped)
tapped_part = sum(1 for z in mp if z.tapped)
print(f"  to'liq tarixda tegilgan: {tapped_full}")
print(f"  kesilgan tarixda       : {tapped_part}")
print("  -> Farq normal: kesikda kelajak hali yo'q.")
print("  -> DIQQAT: backtestda mark_mitigation FAQAT joriy shamgacha chaqirilishi shart!")

print("\n" + "="*58)
if fails == 0:
    print("NATIJA: LOOK-AHEAD TOPILMADI ✓")
else:
    print(f"NATIJA: {fails} ta funksiyada MUAMMO BOR ✗")
print("="*58)
