# -*- coding: utf-8 -*-
"""Realistik prognoz: depozit, daromad, drawdown, ruin ehtimoli."""
import random, math
random.seed(11)

def simulate(exp_r, sd_r, n_trades, risk_pct, start, n_sims=20000, ruin_at=0.5):
    """Bootstrap: kutilma va tarqoqlik asosida kapital yo'lini modellaydi."""
    finals, dds, ruins = [], [], 0
    for _ in range(n_sims):
        eq = start; peak = eq; mdd = 0.0; dead = False
        for _ in range(n_trades):
            r = random.gauss(exp_r, sd_r)
            eq *= (1 + risk_pct/100 * r)
            peak = max(peak, eq)
            dd = (peak - eq)/peak
            mdd = max(mdd, dd)
            if eq <= start * ruin_at:
                dead = True; break
        if dead: ruins += 1
        finals.append(eq); dds.append(mdd)
    finals.sort(); dds.sort()
    q = lambda a, p: a[int(len(a)*p)]
    return dict(p5=q(finals,0.05), p25=q(finals,0.25), med=q(finals,0.50),
                p75=q(finals,0.75), p95=q(finals,0.95),
                dd_med=q(dds,0.50), dd95=q(dds,0.95),
                ruin=ruins/n_sims)

print("="*74)
print("A) EDGE DARAJASIGA QARAB YILLIK NATIJA")
print("   200 savdo/yil, risk 0.5%, boshlang'ich $1000")
print("="*74)
print(f"{'Ssenariy':<26}{'exp':>7}{'median':>10}{'5%':>9}{'95%':>11}{'DD95':>8}{'ruin':>8}")
scen = [
    ("Edge yo'q (0.00R)",      0.00),
    ("Juda kichik (0.05R)",    0.05),
    ("Kichik (0.10R)",         0.10),
    ("O'rtacha (0.20R)",       0.20),
    ("Kuchli (0.35R)",         0.35),
]
for name, e in scen:
    r = simulate(e, 1.8, 200, 0.5, 1000)
    print(f"{name:<26}{e:>7.2f}{r['med']:>10.0f}{r['p5']:>9.0f}{r['p95']:>11.0f}"
          f"{r['dd_med']*100:>7.0f}%{r['ruin']*100:>7.1f}%")

print("\n" + "="*74)
print("B) RISK FOIZI — 0.20R edge, 200 savdo, $1000")
print("="*74)
print(f"{'risk/savdo':>11}{'median':>10}{'5%':>9}{'95%':>11}{'DD med':>9}{'DD95':>8}{'ruin':>8}")
for rp in (0.25, 0.5, 1.0, 2.0, 3.0):
    r = simulate(0.20, 1.8, 200, rp, 1000)
    print(f"{rp:>10.2f}%{r['med']:>10.0f}{r['p5']:>9.0f}{r['p95']:>11.0f}"
          f"{r['dd_med']*100:>8.0f}%{r['dd95']*100:>7.0f}%{r['ruin']*100:>7.1f}%")

print("\n" + "="*74)
print("C) DEPOZIT HAJMI — 0.5% risk, o'rtacha SL 15 pip")
print("="*74)
print(f"{'depozit':>9}{'risk $':>9}{'lot':>9}{'1 pip $':>9}{'izoh':>32}")
for dep in (100, 500, 1000, 3000, 10000):
    risk_usd = dep * 0.005
    lot = risk_usd / (15 * 10)      # 1 lot = $10/pip
    pipval = lot * 10
    if lot < 0.01:
        note = "cent-hisob kerak (mikrolot ham katta)"
    elif lot < 0.03:
        note = "juda kichik, komissiya sezilarli"
    elif lot < 0.10:
        note = "ishlaydi, lekin daromad kichik"
    else:
        note = "normal"
    print(f"{dep:>9}{risk_usd:>9.2f}{lot:>9.3f}{pipval:>9.2f}   {note:<32}")

print("\n" + "="*74)
print("D) PROP FIRM MATEMATIKASI ($10k challenge, 10% target, 10% max DD)")
print("="*74)
def prop_pass(exp_r, sd_r, risk_pct, target=0.10, maxdd=0.10, max_trades=400, n=20000):
    ok = fail = 0
    for _ in range(n):
        eq = 1.0; peak = 1.0
        for _ in range(max_trades):
            eq *= (1 + risk_pct/100 * random.gauss(exp_r, sd_r))
            peak = max(peak, eq)
            if (peak - eq)/peak >= maxdd or eq <= 1-maxdd:
                fail += 1; break
            if eq >= 1 + target:
                ok += 1; break
        else:
            fail += 1
    return ok/n
print(f"{'edge':>8}{'risk 0.5%':>12}{'risk 1%':>10}{'risk 2%':>10}")
for e in (0.0, 0.10, 0.20, 0.35):
    row = [prop_pass(e, 1.8, rp) for rp in (0.5, 1.0, 2.0)]
    print(f"{e:>8.2f}{row[0]*100:>11.0f}%{row[1]*100:>9.0f}%{row[2]*100:>9.0f}%")
print("""
  -> Edge bo'lmasa, risk oshirish PASS ehtimolini oshiradi (omad),
     lekin funded hisobni saqlab qolish ehtimolini KESKIN pasaytiradi.
""")
