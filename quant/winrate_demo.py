# -*- coding: utf-8 -*-
"""Win rate qopqoni: yuqori win rate != foyda."""
import random
random.seed(42)

def simulate(name, win_rate, rr, n=10000, risk=0.01, start=10000.0):
    """rr = reward/risk. Har savdoda kapitalning `risk` qismi tavakkal."""
    eq = start
    peak = eq
    max_dd = 0.0
    ruined = False
    for _ in range(n):
        stake = eq * risk
        if random.random() < win_rate:
            eq += stake * rr
        else:
            eq -= stake
        peak = max(peak, eq)
        max_dd = max(max_dd, (peak - eq) / peak)
        if eq < start * 0.05:
            ruined = True
            break
    exp_r = win_rate * rr - (1 - win_rate)      # 1R birligida kutilma
    print(f"{name:<34} WR={win_rate*100:>5.1f}%  RR=1:{rr:<4} "
          f"kutilma={exp_r:+.3f}R  yakun=${eq:>12,.0f}  maxDD={max_dd*100:>5.1f}%"
          + ("  <-- KUYDI" if ruined else ""))

print("\n10 000 ta savdo, har birida kapitalning 1% tavakkal:\n")
simulate("Scalper 'aniq signal'",      0.90, 0.10)
simulate("Martingeyl uslub",           0.95, 0.05)
simulate("Grid / mean reversion",      0.80, 0.20)
simulate("Klassik intraday",           0.55, 1.00)
simulate("Trend-following (RenTech)",  0.5075, 1.00)
simulate("Breakout swing",             0.40, 2.00)
simulate("Trend rider (uzoq)",         0.30, 4.00)

print("""
Xulosa: 90% win rate strategiya kapitalni yeydi, 30% win rate esa oshiradi.
Muhimi win rate emas — KUTILMA (expectancy): WR*RR - (1-WR).
Bu musbat bo'lmasa, hech qanday AI yoki kod yordam bermaydi.
""")
