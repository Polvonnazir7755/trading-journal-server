# -*- coding: utf-8 -*-
"""
Gann Square of 9 kalkulyatori.

Skrinshotdagi "STYLE FX calculator" aynan shu formulani ishlatadi:
    sqrt(narx) -> +/- k/8 -> kvadratga ko'tarish

Tasdiqlangan misol (XAUUSD, markaz 2704.00):
    sqrt(2704) = 52.000  (aniq butun son)
    52.000 - 2/8 = 51.750 -> 2678.06   (Support 1)
    52.000 + 1/8 = 52.125 -> 2717.02   (Resistance 1)
"""
import math
from typing import List, Tuple


def sq9_levels(price: float, steps: int = 8, div: int = 8) -> List[Tuple[float, float]]:
    """
    Narx atrofidagi Gann Sq9 darajalarini qaytaradi.

    div=8  -> har qadam 45 daraja (1/8 aylana)
    div=16 -> har qadam 22.5 daraja (nozikroq grid)
    """
    root = math.sqrt(price)
    out = []
    for k in range(-steps, steps + 1):
        r = root + k / div
        if r > 0:
            out.append((k, r * r))
    return out


def nearest_center(price: float, div: int = 8) -> float:
    """Narxga eng yaqin 'toza' Sq9 markazi (sqrt butun yoki k/8 ga tushadigan)."""
    root = math.sqrt(price)
    snapped = round(root * div) / div
    return snapped * snapped


def levels_from_center(center: float, steps: int = 8, div: int = 8):
    """Markazdan support/resistance darajalari."""
    root = math.sqrt(center)
    res, sup = [], []
    for k in range(1, steps + 1):
        res.append(((root + k/div) ** 2, k))
        sup.append(((root - k/div) ** 2, k))
    return sup, res


def degrees_to_step(deg: float) -> float:
    """Gann darajasini (45, 90, 180...) qadamga aylantiradi."""
    return deg / 360.0


if __name__ == "__main__":
    print("=" * 62)
    print("TEKSHIRUV — skrinshotdagi raqamlar bilan solishtirish")
    print("=" * 62)

    expected = {
        2639.39: "Support 4 (skrinshot)",
        2652.25: "Support 3",
        2665.14: "Support 2",
        2678.06: "Support 1",
        2691.02: "(oraliq)",
        2704.00: "MARKAZ",
        2717.02: "Resistance 1",
        2730.06: "Resistance 2",
        2743.14: "Resistance 3",
        2756.25: "Resistance 4",
        2782.56: "(skrinshotda bor)",
    }

    center = 2704.00
    print(f"\nMarkaz: {center}   sqrt = {math.sqrt(center):.5f}\n")
    print(f"{'qadam':>7}{'sqrt':>10}{'hisoblangan':>14}{'kutilgan':>12}{'farq':>9}  izoh")

    ok = 0
    for k, lvl in sq9_levels(center, steps=6):
        root = math.sqrt(center) + k / 8
        match = None
        for e in expected:
            if abs(lvl - e) < 0.05:
                match = e
                break
        if match:
            ok += 1
            print(f"{k:>7}{root:>10.3f}{lvl:>14.2f}{match:>12.2f}"
                  f"{lvl-match:>9.3f}  {expected[match]}")
        else:
            print(f"{k:>7}{root:>10.3f}{lvl:>14.2f}{'—':>12}{'—':>9}")

    print(f"\n  Moslik: {ok} / {len(expected)} daraja aniq topildi")
    print("  -> Formula TASDIQLANDI: Gann Square of 9, qadam = 1/8 (45 daraja)")

    print("\n" + "=" * 62)
    print("ISHLATISH")
    print("=" * 62)
    for p in (2650.0, 1.0850):
        c = nearest_center(p)
        sup, res = levels_from_center(c, steps=4)
        print(f"\n  Narx {p}  ->  markaz {c:.4f}")
        print(f"    Resistance: {', '.join(f'{v:.4f}' for v, _ in res)}")
        print(f"    Support   : {', '.join(f'{v:.4f}' for v, _ in sup)}")
