# -*- coding: utf-8 -*-
"""
Photon struktura aniqlash — BOS / CHoCH / i-BOS / OB / FVG / LQ.

MUHIM QOIDA: barcha funksiyalar FAQAT yopilgan shamlar ro'yxatini oladi.
Hech qanday funksiya kelajakka qaramaydi (look-ahead yo'q).
Har bir natijada `confirmed_at` — qaysi indeksda TASDIQLANGANI ko'rsatiladi.
"""
from dataclasses import dataclass, field
from typing import List, Optional, Literal

Dir = Literal["BULL", "BEAR"]


@dataclass
class Swing:
    idx: int            # sham indeksi
    price: float
    kind: Literal["HIGH", "LOW"]
    confirmed_at: int   # qaysi indeksda tasdiqlangan (idx + right)


@dataclass
class Event:
    kind: Literal["BOS", "CHoCH", "iBOS"]
    direction: Dir
    idx: int            # qaysi shamda sodir bo'lgan
    level: float        # buzilgan daraja
    swing_idx: int      # buzilgan swing indeksi


@dataclass
class Zone:
    kind: Literal["OB", "FVG"]
    direction: Dir      # BULL = demand, BEAR = supply
    top: float
    bottom: float
    idx: int            # yaratilgan sham
    mitigated_at: Optional[int] = None
    tapped: bool = False

    @property
    def mid(self):
        return (self.top + self.bottom) / 2

    def contains(self, price: float) -> bool:
        return self.bottom <= price <= self.top


# ---------------------------------------------------------------- swings
def find_swings(bars, left: int = 2, right: int = 2) -> List[Swing]:
    """Fraktal swing nuqtalari. right>0 => tasdiq uchun kutish kerak."""
    out: List[Swing] = []
    for i in range(left, len(bars) - right):
        w = bars[i - left: i + right + 1]
        hi = bars[i].high
        lo = bars[i].low
        if all(hi > b.high for j, b in enumerate(w) if j != left):
            out.append(Swing(i, hi, "HIGH", i + right))
        if all(lo < b.low for j, b in enumerate(w) if j != left):
            out.append(Swing(i, lo, "LOW", i + right))
    return sorted(out, key=lambda s: s.idx)


# ------------------------------------------------------------- structure
def detect_events(bars, swings: List[Swing], use_close: bool = True) -> List[Event]:
    """
    BOS  — trend yo'nalishida swing buzilishi (davom etish)
    CHoCH— trendga qarshi birinchi buzilish (o'zgarish)
    Buzilish `use_close=True` bo'lsa YOPILISH bilan tasdiqlanadi (qat'iyroq).
    """
    events: List[Event] = []
    bias: Optional[Dir] = None

    last_high: Optional[Swing] = None
    last_low: Optional[Swing] = None

    for i, bar in enumerate(bars):
        # shu indeksgacha TASDIQLANGAN swinglarni yangilaymiz
        for s in swings:
            if s.confirmed_at == i:
                if s.kind == "HIGH":
                    last_high = s
                else:
                    last_low = s

        px_up = bar.close if use_close else bar.high
        px_dn = bar.close if use_close else bar.low

        # yuqoriga buzilish
        if last_high and px_up > last_high.price:
            kind = "BOS" if bias == "BULL" else ("CHoCH" if bias == "BEAR" else "BOS")
            events.append(Event(kind, "BULL", i, last_high.price, last_high.idx))
            bias = "BULL"
            last_high = None          # bir marta ishlatiladi

        # pastga buzilish
        if last_low and px_dn < last_low.price:
            kind = "BOS" if bias == "BEAR" else ("CHoCH" if bias == "BULL" else "BOS")
            events.append(Event(kind, "BEAR", i, last_low.price, last_low.idx))
            bias = "BEAR"
            last_low = None

    return events


def current_bias(events: List[Event], upto: int) -> Optional[Dir]:
    """`upto` indeksigacha bo'lgan oxirgi hodisa yo'nalishi."""
    past = [e for e in events if e.idx <= upto]
    return past[-1].direction if past else None


# ------------------------------------------------------------------- FVG
def find_fvg(bars, min_size: float = 0.0) -> List[Zone]:
    """
    Fair Value Gap: 3 shamli imbalance.
    BULL: bar[i-1].high < bar[i+1].low  (pastda bo'shliq -> demand)
    BEAR: bar[i-1].low  > bar[i+1].high (yuqorida bo'shliq -> supply)
    Zona i+1 shamda TASDIQLANADI.
    """
    out: List[Zone] = []
    for i in range(1, len(bars) - 1):
        a, c = bars[i - 1], bars[i + 1]
        if c.low > a.high and (c.low - a.high) >= min_size:
            out.append(Zone("FVG", "BULL", c.low, a.high, i + 1))
        if a.low > c.high and (a.low - c.high) >= min_size:
            out.append(Zone("FVG", "BEAR", a.low, c.high, i + 1))
    return out


# -------------------------------------------------------------------- OB
def find_order_blocks(bars, events: List[Event], lookback: int = 12) -> List[Zone]:
    """
    Order Block: struktura buzilishidan OLDINGI oxirgi qarama-qarshi sham.
    BULL BOS/CHoCH -> undan oldingi oxirgi BEARISH sham = demand OB
    BEAR BOS/CHoCH -> undan oldingi oxirgi BULLISH sham = supply OB
    """
    out: List[Zone] = []
    for ev in events:
        start = max(0, ev.idx - lookback)
        found = None
        for j in range(ev.idx - 1, start - 1, -1):
            b = bars[j]
            if ev.direction == "BULL" and b.close < b.open:
                found = j; break
            if ev.direction == "BEAR" and b.close > b.open:
                found = j; break
        if found is None:
            continue
        b = bars[found]
        out.append(Zone("OB", ev.direction, max(b.open, b.close, b.high),
                        min(b.open, b.close, b.low), found))
    return out


# ------------------------------------------------------------ mitigation
def mark_mitigation(zones: List[Zone], bars) -> None:
    """Har bir zona qachon birinchi marta teginilganini belgilaydi."""
    for z in zones:
        for i in range(z.idx + 1, len(bars)):
            b = bars[i]
            if b.low <= z.top and b.high >= z.bottom:
                z.mitigated_at = i
                z.tapped = True
                break


# -------------------------------------------------------- liquidity pool
def find_liquidity(swings: List[Swing], tol: float) -> List[dict]:
    """Equal highs / equal lows — likvidlik hovuzlari."""
    pools = []
    highs = [s for s in swings if s.kind == "HIGH"]
    lows  = [s for s in swings if s.kind == "LOW"]
    for group, kind in ((highs, "EQH"), (lows, "EQL")):
        for i in range(len(group) - 1):
            a, b = group[i], group[i + 1]
            if abs(a.price - b.price) <= tol:
                pools.append(dict(kind=kind, price=(a.price + b.price) / 2,
                                  idx=b.idx, confirmed_at=b.confirmed_at))
    return pools


# ------------------------------------------------------------------ P&D
def premium_discount(high: float, low: float, price: float):
    if high is None or low is None or high <= low:
        return None, None
    pos = (price - low) / (high - low)
    if pos > 0.79:  return round(pos, 3), "EXTREME_PREMIUM"
    if pos > 0.50:  return round(pos, 3), "PREMIUM"
    if pos < 0.21:  return round(pos, 3), "EXTREME_DISCOUNT"
    return round(pos, 3), "DISCOUNT"


if __name__ == "__main__":
    from mtf_engine import Bar, MTFEngine
    from resample_demo import gen_m1

    eng = MTFEngine(["M15", "H1", "H4"])
    for t, o, h, l, c in gen_m1(20160):     # 14 kun
        eng.feed(Bar(t, o, h, l, c))

    for tf in ["M15", "H1", "H4"]:
        bars = eng.closed(tf)
        if len(bars) < 20:
            print(f"{tf}: shamlar kam ({len(bars)})"); continue
        sw  = find_swings(bars)
        ev  = detect_events(bars, sw)
        fvg = find_fvg(bars)
        ob  = find_order_blocks(bars, ev)
        mark_mitigation(fvg, bars); mark_mitigation(ob, bars)
        pools = find_liquidity(sw, tol=0.00015)
        bos   = sum(1 for e in ev if e.kind == "BOS")
        choch = sum(1 for e in ev if e.kind == "CHoCH")
        print(f"{tf:<4} bars={len(bars):<5} swing={len(sw):<4} "
              f"BOS={bos:<3} CHoCH={choch:<3} FVG={len(fvg):<4} OB={len(ob):<3} "
              f"LQ={len(pools):<3} bias={current_bias(ev, len(bars)-1)}")
        um_fvg = sum(1 for z in fvg if not z.tapped)
        print(f"     mitigatsiya bo'lmagan FVG: {um_fvg} / {len(fvg)}")
