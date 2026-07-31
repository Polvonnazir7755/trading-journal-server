# -*- coding: utf-8 -*-
"""'Matematik strategiya' — haqiqiy va soxta turlarini ajratish."""
import random, math
random.seed(31)

print("="*70)
print("A) MARTINGEYL — 'matematik kafolat' deb sotiladi")
print("   Har yo'qotishdan keyin stavka 2x. 'Bir marta yutsam qoplanadi.'")
print("="*70)
def martingale(start=1000, base=10, p_win=0.5, n=500, max_double=10, sims=5000):
    survive=0; finals=[]
    for _ in range(sims):
        eq=start; stake=base; streak=0; dead=False
        for _ in range(n):
            if eq < stake: dead=True; break
            if random.random()<p_win:
                eq+=stake; stake=base; streak=0
            else:
                eq-=stake; streak+=1
                stake = base*(2**min(streak,max_double))
        if not dead and eq>start: survive+=1
        finals.append(0 if dead else eq)
    finals.sort()
    return survive/sims, finals[len(finals)//2], sum(1 for f in finals if f==0)/sims
for p in (0.50, 0.55):
    s, med, ruin = martingale(p_win=p)
    print(f"  win rate {p*100:.0f}%:  foydada tugash {s*100:5.1f}%   median ${med:>7.0f}   KUYISH {ruin*100:5.1f}%")
print("""
  -> 500 savdoda martingeyl deyarli kafolatlangan tarzda kuyadi.
  -> 'Matematik' ko'rinadi, lekin bu QIMOR matematikasi.
""")

print("="*70)
print("B) GRID / AVERAGING — 'har doim yutadi'")
print("="*70)
def grid(start=1000, step=0.0020, lot_risk=5, trend=0.0, n_days=250, sims=4000):
    ruin=0; finals=[]
    for _ in range(sims):
        eq=start; price=1.1000; entries=[]; dead=False
        for _ in range(n_days*20):
            price += random.gauss(trend, 0.0008)
            if not entries or price < entries[-1]-step:
                entries.append(price)
            float_pnl = sum((price-e)*10000*lot_risk for e in entries)
            if eq+float_pnl <= 0: dead=True; break
            if float_pnl > lot_risk*10:
                eq += float_pnl; entries=[]
        if dead: ruin+=1
        finals.append(0 if dead else eq)
    finals.sort()
    return ruin/sims, finals[len(finals)//2]
for tr, lbl in [(0.0,"trendsiz bozor"), (-0.000015,"sekin pasayish")]:
    r, med = grid(trend=tr)
    print(f"  {lbl:<18} kuyish {r*100:5.1f}%   median ${med:>7.0f}")
print("""
  -> Trendsiz bozorda 'ishlaydi' — kichik, barqaror foyda.
  -> Bitta kuchli trend hammasini yeydi. Bu FOYDA emas, KECHIKTIRILGAN ZARAR.
""")

print("="*70)
print("C) HAQIQIY MATEMATIK EDGE nimaga o'xshaydi?")
print("="*70)
rows=[
 ("Statistik arbitraj","2 aktiv orasidagi barqaror bog'liqlik buzilishi","kointegratsiya testi"),
 ("Mean reversion (isbotli)","narx o'rtachaga qaytish tendensiyasi","Hurst<0.5, ADF test"),
 ("Momentum/trend","avtokorrelyatsiya musbat","AR modeli, t-test"),
 ("Volatilite klasterlash","GARCH — vola bashorat qilinadi","likelihood ratio"),
 ("Sessiya/vaqt effekti","muayyan soatlarda drift","ANOVA, permutatsiya"),
]
print(f"  {'usul':<26}{'g oya':<44}{'tekshiruv'}")
for a,b,c in rows: print(f"  {a:<26}{b:<44}{c}")
print("""
  Umumiy belgisi: HAR BIRI STATISTIK TEST BILAN RAD ETILISHI MUMKIN.
  Agar strategiyani rad etib bo'lmasa — u ilmiy emas, e'tiqod.
""")

print("="*70)
print("D) TEKSHIRUV SAVOLLARI (har qanday 'matematik' strategiyaga)")
print("="*70)
qs=[
 "Qanday statistik test bu edge'ni RAD ETA oladi?",
 "Out-of-sample natija bormi? (ma'lumotning yarmida sozlab, yarmida sinash)",
 "Nechta parametr bor? (ko'p parametr = overfitting)",
 "Spred, komissiya, slippage hisobga olinganmi?",
 "Necha savdoda sinalgan? (n<200 => xulosa yo'q)",
 "Turli yillarda barqarormi? (2022 va 2024 alohida)",
 "Nega bu edge yo'qolmagan? (kim buning teskarisida turibdi?)",
]
for i,q in enumerate(qs,1): print(f"  {i}. {q}")
print("""
  Bu savollarga javob bo'lmasa — 'matematika' so'zi bezak, mohiyat emas.
""")
