# -*- coding: utf-8 -*-
"""
Gann Angle Calculator — "STYLE FX calculator2" formulasi.

FORMULA:
    daraja = ( sqrt(baza) ± burchak/180 ) ^ 2

    DEGREE FACTOR = burchak / 180

Tasdiqlangan (o'rtacha farq 0.3 punkt — kalkulyator butun songa yaxlitlaydi):
    baza 2611, 180° -> (51.09795 + 1.0)^2 = 2714.20   [kalkulyator: 2714]
    baza 2762, 180° -> (52.55473 - 1.0)^2 = 2657.89   [kalkulyator: 2658]

MUHIM: 180° = 1.0 birlik = sqrt shkalasida to'liq qadam.
Ya'ni bu 1-kalkulyator (Square of 9) bilan BIR XIL tizim,
faqat qadamlar burchak tilida ifodalangan:

    1-kalk:  1/8 qadam          <->  2-kalk:  22.5°
    1-kalk:  2/8 = 1/4          <->  2-kalk:  45°
    1-kalk:  4/8 = 1/2          <->  2-kalk:  90°
    1-kalk:  8/8 = 1.0          <->  2-kalk:  180°
"""
import math
from typing import List, Tuple

GANN_ANGLES = [12.5, 22.5, 45, 67.5, 90, 135, 180, 225, 270, 315, 360]


def degree_factor(angle_deg: float) -> float:
    """Kalkulyatordagi DEGREE FACTOR ustuni."""
    return angle_deg / 180.0


def gann_level(base: float, angle_deg: float, direction: int = +1) -> float:
    """
    direction = +1  -> resistance (yuqoriga)
    direction = -1  -> support (pastga)
    """
    return (math.sqrt(base) + direction * degree_factor(angle_deg)) ** 2


def resistance_table(base: float, angles=None) -> List[Tuple[float, float]]:
    angles = angles or GANN_ANGLES
    return [(a, gann_level(base, a, +1)) for a in angles]


def support_table(base: float, angles=None) -> List[Tuple[float, float]]:
    angles = angles or GANN_ANGLES
    return [(a, gann_level(base, a, -1)) for a in angles]


def price_to_angle(price: float, base: float) -> float:
    """Teskari hisob: narx bazadan necha gradus uzoqda?"""
    return (math.sqrt(price) - math.sqrt(base)) * 180.0


def sq9_equivalent(angle_deg: float) -> str:
    """Square of 9 tilida nechanchi qadam."""
    eighths = angle_deg / 22.5
    return f"{eighths:.2f}/8"


if __name__ == "__main__":
    print("=" * 72)
    print("TASDIQLASH — skrinshotdagi raqamlar bilan")
    print("=" * 72)

    cases = [
        ("RESISTANCE", 2611, +1,
         [2617, 2624, 2637, 2649, 2662, 2688, 2714, 2740, 2767, 2793, 2819]),
        ("SUPPORT", 2762, -1,
         [2755, 2749, 2736, 2723, 2710, 2684, 2658, 2632, 2607, 2581, 2556]),
    ]

    for name, base, sign, expected in cases:
        print(f"\n{name}   baza = {base}   sqrt = {math.sqrt(base):.5f}")
        print(f"  {'burchak':>8}{'factor':>10}{'hisoblangan':>13}"
              f"{'kalkulyator':>13}{'farq':>8}{'Sq9':>9}")
        tot = 0.0
        for a, exp in zip(GANN_ANGLES, expected):
            calc = gann_level(base, a, sign)
            d = calc - exp
            tot += abs(d)
            print(f"  {a:>8}{degree_factor(a):>10.5f}{calc:>13.2f}"
                  f"{exp:>13}{d:>8.2f}{sq9_equivalent(a):>9}")
        print(f"  -> o'rtacha farq: {tot/len(expected):.2f} punkt (yaxlitlash)")

    print("\n" + "=" * 72)
    print("DEGREE FACTOR maydoni (skrinshotdagi 3-blok)")
    print("=" * 72)
    price, angle_shown, factor = 6349, 77.51, 0.430612447
    print(f"  price={price}  angle(ekranda)={angle_shown}  factor={factor}")
    print(f"  factor*180 = {factor*180:.4f}  -> haqiqiy burchak (ekranda yaxlitlangan)")
    print(f"  moslik: {abs(factor*180 - angle_shown) < 0.01}")
    print(f"\n  sqrt({price}) = {math.sqrt(price):.6f}")
    print(f"  {math.sqrt(price):.6f} - 79.25 = {math.sqrt(price)-79.25:.6f} = factor")
    print(f"  -> burchak eng yaqin 45-gradus belgisidan o'lchanadi")

    print("\n" + "=" * 72)
    print("IKKALA KALKULYATOR — BIR XIL TIZIM")
    print("=" * 72)
    print(f"  {'Sq9 qadam':>12}{'burchak':>10}{'factor':>10}")
    for k in (1, 2, 3, 4, 8, 16):
        print(f"  {k:>10}/8{k*22.5:>10.1f}{k/8:>10.4f}")
    print("""
  Ya'ni 2-kalkulyator yangi narsa emas — o'sha Square of 9,
  faqat qadamlar burchak tilida yozilgan.""")

    print("\n" + "=" * 72)
    print("ISHLATISH")
    print("=" * 72)
    b = 2650.0
    print(f"\n  Baza {b}:")
    print(f"  {'burchak':>8}{'resistance':>13}{'support':>12}")
    for a in [45, 90, 180, 360]:
        print(f"  {a:>8}{gann_level(b,a,+1):>13.2f}{gann_level(b,a,-1):>12.2f}")
