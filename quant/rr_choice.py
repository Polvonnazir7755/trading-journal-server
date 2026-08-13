# -*- coding: utf-8 -*-
"""1:1 vs 1:2 vs 1:3 — qaysi biri to'g'ri tanlov?"""
import math, random
random.seed(29)

print("="*72)
print("1) BREAKEVEN WIN RATE — siz haqsiz")
print("="*72)
print(f"{'RR':>6}{'breakeven WR':>15}{'+3% edge bilan':>17}{'exp/savdo':>12}")
for rr in (1, 1.5, 2, 3, 4):
    be = 1/(1+rr)
    real = be + 0.03
    exp = real*rr - (1-real)
    print(f"{'1:'+str(rr):>6}{be*100:>14.1f}%{real*100:>16.1f}%{exp:>+12.3f}")
print("""
  -> 1:1 da 50%+ kerak. Siz to'g'ri aytdingiz.
  -> LEKIN: har RR da bir xil "+3% edge" bo'lsa, EXPECTANCY HAR XIL.
""")

print("="*72)
print("2) SPRED SOLIG'I — 1:1 da OG'IRROQ tushadi")
print("="*72)
print("XAUUSD: spred+komissiya+slippage ~0.40 USD, SL 15 pip (1.5 USD)\n")
cost_r = 0.40/1.50   # riskning ulushi
print(f"{'RR':>6}{'nominal':>10}{'real RR':>10}{'nominal BE':>13}{'REAL BE':>10}{'farq':>8}")
for rr in (1, 2, 3, 4):
    real_rr = (1.5*rr - 0.40)/(1.5 + 0.40)
    be_nom = 1/(1+rr)*100
    be_real = 1/(1+real_rr)*100
    print(f"{'1:'+str(rr):>6}{rr:>10}{real_rr:>10.2f}{be_nom:>12.1f}%{be_real:>9.1f}%{be_real-be_nom:>+8.1f}")
print("""
  -> 1:1 da spred BE ni 50% -> 63% ga ko'taradi (+13 punkt!)
  -> 1:3 da 25% -> 32% (+7 punkt)
  -> Ya'ni kichik RR da spred NISBATAN ko'proq zarar qiladi.
  -> Eslatma: bu SL=15 pip uchun. Kattaroq SL da ta'sir kamayadi.
""")

print("="*72)
print("3) 10 SAVDO — hech narsa aytib bo'lmaydi")
print("="*72)
def wilson(k, n, z=1.96):
    if n == 0: return (0,0)
    p=k/n; d=1+z*z/n; c=p+z*z/(2*n)
    s=z*math.sqrt(p*(1-p)/n + z*z/(4*n*n))
    return ((c-s)/d*100, (c+s)/d*100)
print(f"{'n':>6}{'yutuq':>8}{'WR':>8}{'95% ishonch oralig i':>26}{'xulosa':>12}")
for n, k in [(10,5),(10,6),(30,16),(100,53),(300,159)]:
    lo, hi = wilson(k, n)
    verdict = "50% dan yuqorimi?" if lo < 50 < hi else ("HA" if lo > 50 else "yo'q")
    print(f"{n:>6}{k:>8}{k/n*100:>7.0f}%{lo:>13.1f}% - {hi:.1f}%{verdict:>14}")
print("""
  -> 10 savdoda 6 yutuq (60%) bo'lsa ham, haqiqiy WR 31%-83% orasida.
  -> "50% dan baland chiqmasa foyda yo'q" -- to'g'ri, LEKIN buni
     10 savdoda BILIB BO'LMAYDI. Kamida 100 kerak.
""")

print("="*72)
print("4) RISK MANAGEMENT — muhim, lekin YETARLI EMAS")
print("="*72)
def run(exp_r, risk_pct, n=500, sims=8000, start=10000):
    fin=[]
    for _ in range(sims):
        eq=start
        for _ in range(n):
            r = random.gauss(exp_r, 1.6)
            eq *= (1 + risk_pct/100*r)
            if eq < start*0.2: break
        fin.append(eq)
    fin.sort()
    return fin[len(fin)//2]
print(f"{'edge':>10}{'risk 0.25%':>13}{'risk 0.5%':>12}{'risk 2%':>11}")
for e, lbl in [(-0.05,"MANFIY"), (0.0,"NOL"), (0.10,"musbat")]:
    row=[run(e, rp) for rp in (0.25, 0.5, 2.0)]
    print(f"{lbl:>10}" + "".join(f"{x:>12.0f}" for x in row))
print("""
  -> MANFIY edge da risk kamaytirish faqat SEKINROQ yo'qotadi.
  -> Risk management HALOKATNI oldini oladi, lekin FOYDA YARATMAYDI.
  -> Formula: FOYDA = EDGE x RISK x VAQT.  Edge nol bo'lsa, ko'paytma nol.
""")

print("="*72)
print("5) XULOSA: qaysi RR?")
print("="*72)
print("""
  1:1  -> BE 50%, spred bilan 56%. Erishish QIYIN.
          Ko'p savdo beradi, statistika tez to'planadi.
          Kichik xato ham minusga olib boradi.

  1:2  -> BE 33%, spred bilan 37%. Muvozanatli.

  1:3  -> BE 25%, spred bilan 28%. Xato uchun joy ko'p.
          Kamroq savdo, uzunroq zarar seriyalari.

  TAVSIYA: 1:2 dan boshlang.
    - BE 42% spred bilan (erishsa bo'ladi)
    - Zarar seriyasi 11-16 (chidasa bo'ladi)
    - Spred 1:1 dagichalik og'ir emas
""")
