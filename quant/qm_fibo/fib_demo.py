# -*- coding: utf-8 -*-
"""
QM + FIBO + OB + IMB + LIQ strategiyasi — fib darajalari kalkulyatori.

FIB ANKORLARI (siz aytganingizdek):
  0 chizig'i = oxirgi istorik MINIMUM shamining ENG PAST SOYASI (low)
  1 chizig'i = istorik MAKSIMUMni yorib o'tgan shamning TANASI YUQORISI
               (max(open, close) — soya EMAS)

TP = 1.618 (kengaytma)
"""

def fib_levels(anchor0: float, anchor1: float):
    """0 va 1 ankorlari orasida darajalarni hisoblaydi."""
    rng = anchor1 - anchor0
    return {
        "0.0":   anchor0,
        "0.382": anchor0 + rng * 0.382,
        "0.5":   anchor0 + rng * 0.5,
        "0.618": anchor0 + rng * 0.618,
        "0.786": anchor0 + rng * 0.786,
        "1.0":   anchor1,
        "1.272": anchor0 + rng * 1.272,
        "1.618": anchor0 + rng * 1.618,
    }


def entry_zones(anchor0, anchor1, ob_top=None, ob_bottom=None,
                imb_top=None, imb_bottom=None):
    """5 ta kirish zonasi."""
    f = fib_levels(anchor0, anchor1)
    zones = []
    zones.append(("1) 1.0 zonasi (proboy darajasi)", f["1.0"], f["1.0"]))
    zones.append(("2) 0.5 zonasi",                   f["0.5"], f["0.5"]))
    zones.append(("3) 0.618 zonasi",                 f["0.618"], f["0.618"]))
    if imb_top is not None:
        zones.append(("4) IMB (imbalance/FVG)", imb_top, imb_bottom))
    if ob_top is not None:
        zones.append(("5) OB (max soya – min tana)", ob_top, ob_bottom))
    return f, zones


if __name__ == "__main__":
    print("=" * 70)
    print("MISOL: XAUUSD bullish setup")
    print("=" * 70)

    # --- kirish ma'lumotlari ---
    hist_min_low   = 2640.00   # oxirgi istorik minimum shamining eng past soyasi
    breaker_open   = 2698.50   # istorik maxni yorgan sham
    breaker_close  = 2704.20
    breaker_high   = 2707.80   # soya (fib uchun ISHLATILMAYDI)
    body_top       = max(breaker_open, breaker_close)

    print(f"\n  Istorik MIN soyasi (fib 0)     : {hist_min_low:.2f}")
    print(f"  Yorgan sham: O={breaker_open} C={breaker_close} H={breaker_high}")
    print(f"  Tanasi yuqorisi (fib 1)        : {body_top:.2f}   <- soya emas!")
    print(f"  Diapazon                       : {body_top - hist_min_low:.2f}")

    # OB: "max soya va min tana oralig'i"
    ob_top    = breaker_high      # max soya
    ob_bottom = min(breaker_open, breaker_close)   # min tana

    # IMB (misol uchun)
    imb_top, imb_bottom = 2688.00, 2683.50

    f, zones = entry_zones(hist_min_low, body_top,
                           ob_top, ob_bottom, imb_top, imb_bottom)

    print(f"\n{'FIB DARAJALARI':-^70}")
    for k, v in f.items():
        mark = "  <- TP" if k == "1.618" else ("  <- fib 1" if k == "1.0" else "")
        print(f"  {k:>6} : {v:>10.2f}{mark}")

    print(f"\n{'5 TA KIRISH ZONASI':-^70}")
    for name, top, bot in zones:
        if top == bot:
            print(f"  {name:<34} {top:>10.2f}")
        else:
            print(f"  {name:<34} {bot:>10.2f} – {top:.2f}")

    print(f"\n{'RISK/REWARD HISOBI':-^70}")
    tp = f["1.618"]
    sl = hist_min_low          # taxmin: fib 0 ostida
    print(f"  TP (1.618) : {tp:.2f}")
    print(f"  SL (taxmin): {sl:.2f}  <- ANIQLASHTIRISH KERAK")
    print()
    print(f"  {'kirish zonasi':<26}{'entry':>9}{'risk':>9}{'reward':>9}{'RR':>8}")
    for name, top, bot in zones:
        entry = (top + bot) / 2
        risk = entry - sl
        rew = tp - entry
        rr = rew / risk if risk > 0 else 0
        print(f"  {name[:26]:<26}{entry:>9.2f}{risk:>9.2f}{rew:>9.2f}{rr:>7.2f}")

    print("""
  DIQQAT: 1.0 zonasida RR eng past, 0.5 zonasida eng yuqori.
  Ya'ni chuqurroq qaytishni kutish yaxshiroq RR beradi —
  lekin narx u yergacha qaytmasligi ham mumkin.
  Bu KOMPROMISS backtestda o'lchanadi.
""")
