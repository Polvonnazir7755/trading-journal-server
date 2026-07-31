# -*- coding: utf-8 -*-
"""
Savdo statistikasi — win rate emas, EXPECTANCY va ishonch oralig'i.
Photon kundaligidagi CSV ni o'qib, kesimlar bo'yicha tahlil qiladi.
"""
import csv, math, sys, random
from collections import defaultdict

def wilson(k, n, z=1.96):
    """Win rate uchun ishonch oralig'i (Wilson). Kichik namunada halol."""
    if n == 0:
        return (0.0, 0.0, 0.0)
    p = k / n
    d = 1 + z*z/n
    c = p + z*z/(2*n)
    s = z * math.sqrt(p*(1-p)/n + z*z/(4*n*n))
    return (p, (c-s)/d, (c+s)/d)

def load(path):
    rows = []
    with open(path, newline="", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            if not r.get("result_r"):
                continue
            try:
                r["_r"] = float(r["result_r"])
            except ValueError:
                continue
            r["_win"] = r["_r"] > 0
            rows.append(r)
    return rows

def block(rows, label="UMUMIY", spread_cost_r=0.0):
    n = len(rows)
    if n == 0:
        return None
    rs = [r["_r"] - spread_cost_r for r in rows]
    wins = [x for x in rs if x > 0]
    losses = [x for x in rs if x <= 0]
    k = len(wins)
    p, lo, hi = wilson(k, n)
    exp_r = sum(rs) / n
    gross_win = sum(wins)
    gross_loss = abs(sum(losses)) or 1e-9
    pf = gross_win / gross_loss
    # max drawdown (R da)
    eq, peak, mdd = 0.0, 0.0, 0.0
    for x in rs:
        eq += x
        peak = max(peak, eq)
        mdd = max(mdd, peak - eq)
    # standart xato -> edge haqiqiymi?
    sd = (sum((x-exp_r)**2 for x in rs)/(n-1))**0.5 if n > 1 else 0.0
    se = sd / math.sqrt(n) if n else 0.0
    t = exp_r / se if se else 0.0
    return dict(label=label, n=n, wr=p, wr_lo=lo, wr_hi=hi,
                exp_r=exp_r, total_r=sum(rs), pf=pf, mdd=mdd,
                sd=sd, se=se, t=t,
                avg_win=(gross_win/k if k else 0),
                avg_loss=(sum(losses)/len(losses) if losses else 0))

def show(b):
    if not b:
        return
    verdict = "shovqin"
    if b["n"] >= 30 and b["t"] > 2.0:
        verdict = "EDGE BOR (ehtimol)"
    elif b["n"] >= 30 and b["t"] < -2.0:
        verdict = "MANFIY EDGE"
    elif b["n"] < 30:
        verdict = "namuna kichik"
    print(f"\n{'='*66}\n{b['label']}   (n={b['n']})\n{'='*66}")
    print(f"  Win rate     : {b['wr']*100:5.1f}%   [95% CI: {b['wr_lo']*100:.1f}% – {b['wr_hi']*100:.1f}%]")
    print(f"  Expectancy   : {b['exp_r']:+.3f} R / savdo")
    print(f"  Jami         : {b['total_r']:+.1f} R")
    print(f"  Profit factor: {b['pf']:.2f}")
    print(f"  Max DD       : {b['mdd']:.1f} R")
    print(f"  O'rt. yutuq  : {b['avg_win']:+.2f} R   |   O'rt. yo'qotish: {b['avg_loss']:+.2f} R")
    print(f"  t-statistika : {b['t']:+.2f}   ->  {verdict}")

def by(rows, key, min_n=5, spread_cost_r=0.0):
    g = defaultdict(list)
    for r in rows:
        g[r.get(key, "?")].append(r)
    out = []
    for k, v in g.items():
        if len(v) >= min_n:
            out.append(block(v, f"{key} = {k}", spread_cost_r))
    return sorted([o for o in out if o], key=lambda x: -x["exp_r"])

def monte_carlo(rows, n_sims=10000, spread_cost_r=0.0):
    """Bootstrap: savdolarni QAYTARISH BILAN tanlab, muqobil tariхlar yaratadi.
    Shu tariqa 'omadim kelgan bo'lsa-chi?' degan savolga javob beradi."""
    rs = [r["_r"] - spread_cost_r for r in rows]
    if len(rs) < 10:
        return None
    n = len(rs)
    dds, finals = [], []
    for _ in range(n_sims):
        s = [random.choice(rs) for _ in range(n)]   # replacement bilan
        eq, peak, mdd = 0.0, 0.0, 0.0
        for x in s:
            eq += x
            peak = max(peak, eq)
            mdd = max(mdd, peak - eq)
        dds.append(mdd); finals.append(eq)
    dds.sort(); finals.sort()
    return dict(
        dd_median=dds[len(dds)//2],
        dd_95=dds[int(len(dds)*0.95)],
        dd_99=dds[int(len(dds)*0.99)],
        final_5=finals[int(len(finals)*0.05)],
        final_median=finals[len(finals)//2],
        p_negative=sum(1 for f in finals if f < 0)/len(finals),
    )

def main(path, spread_cost_r=0.0):
    rows = load(path)
    if not rows:
        print("Yakunlangan savdo topilmadi.")
        return
    show(block(rows, "UMUMIY", spread_cost_r))

    print(f"\n\n{'#'*66}\n#  KESIMLAR BO'YICHA (kamida 5 ta savdo)\n{'#'*66}")
    for key in ["mtf_phase", "entry_model", "probability", "session", "pair", "direction", "htf_bias"]:
        blocks = by(rows, key, 5, spread_cost_r)
        if not blocks:
            continue
        print(f"\n--- {key.upper()} ---")
        print(f"  {'qiymat':<22}{'n':>5}{'WR':>8}{'exp R':>9}{'jami R':>9}{'PF':>7}")
        for b in blocks:
            val = b['label'].split('= ')[1]
            print(f"  {val:<22}{b['n']:>5}{b['wr']*100:>7.1f}%{b['exp_r']:>+9.3f}{b['total_r']:>+9.1f}{b['pf']:>7.2f}")

    mc = monte_carlo(rows, spread_cost_r=spread_cost_r)
    if mc:
        print(f"\n\n{'#'*66}\n#  MONTE CARLO (10 000 ta aralashtirish)\n{'#'*66}")
        print(f"  Median max DD      : {mc['dd_median']:.1f} R")
        print(f"  95% holatda DD <   : {mc['dd_95']:.1f} R")
        print(f"  99% holatda DD <   : {mc['dd_99']:.1f} R   <- kapitalni shunga moslang")
        print(f"  Median yakun       : {mc['final_median']:+.1f} R")
        print(f"  5% eng yomon yakun : {mc['final_5']:+.1f} R")
        print(f"  Minusda tugash ehtimoli: {mc['p_negative']*100:.1f}%")

    print(f"""
{'='*66}
IZOH
{'='*66}
  t > 2.0  va  n >= 30  ->  edge statistik ma'noli bo'lishi mumkin
  t < 2.0            ->  hozircha shovqindan farqi yo'q, davom eting
  95% CI keng bo'lsa  ->  namuna kichik, xulosa chiqarmang

  DIQQAT: bu o'tmish statistikasi. Kelajakni kafolatlamaydi.
""")

if __name__ == "__main__":
    p = sys.argv[1] if len(sys.argv) > 1 else "trades.csv"
    sc = float(sys.argv[2]) if len(sys.argv) > 2 else 0.0
    main(p, sc)
