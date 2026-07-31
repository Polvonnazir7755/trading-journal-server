# -*- coding: utf-8 -*-
"""Kichik SL + katta RR: reklama va haqiqat."""
import math

print("="*76)
print("1) SPRED SOLIG'I — kichik SL ning asosiy dushmani")
print("="*76)
print("XAUUSD: spred+komissiya ~0.30 USD, slippage ~0.10 -> jami ~0.40")
print(f"\n{'SL':>6}{'nominal RR':>12}{'real risk':>11}{'real mukofot':>14}{'REAL RR':>10}{'breakeven WR':>14}")
cost = 0.40
for sl in (1.0, 2.0, 3.0, 5.0, 10.0, 20.0, 30.0):
    for nom in (10,):
        real_risk = sl + cost
        real_rew  = sl*nom - cost
        rr = real_rew/real_risk
        be = 1/(1+rr)*100
        print(f"{sl:>6.1f}{'1:'+str(nom):>12}{real_risk:>11.2f}{real_rew:>14.2f}{rr:>9.2f}{be:>13.1f}%")

print("""
  -> 1 USD SL da: nominal 1:10, real 1:6.9  (spred riskning 40%ini yeydi)
  -> 20 USD SL da: real 1:9.8  (spred deyarli sezilmaydi)
  Kichik SL = brokerga ko'proq soliq.
""")

print("="*76)
print("2) BREAKEVEN WIN RATE — 1:10 uchun nima kerak?")
print("="*76)
print(f"{'nominal RR':>12}{'SL=2':>10}{'SL=5':>10}{'SL=10':>10}{'SL=20':>10}")
for nom in (3,5,10,20):
    row=[]
    for sl in (2,5,10,20):
        rr=(sl*nom-cost)/(sl+cost)
        row.append(1/(1+rr)*100)
    print(f"{'1:'+str(nom):>12}" + "".join(f"{x:>9.1f}%" for x in row))
print("""
  -> 1:10 da breakeven WR ~9-13%. Ya'ni 10 tadan 1.3 tasi yutsa kifoya.
  -> Bu OSON ko'rinadi. Muammo boshqa joyda.
""")

print("="*76)
print("3) HAQIQIY MUAMMO: 1:10 gacha yetish EHTIMOLI")
print("="*76)
print("Tasodifiy yurishda (edge yo'q) TP ga yetish ehtimoli ~ risk/(risk+reward)")
print(f"\n{'RR':>6}{'nazariy WR':>13}{'kerakli WR':>13}{'natija':>28}")
for nom in (1,2,3,5,10,20):
    p_theory = 1/(1+nom)*100
    be = 1/(1+nom)*100
    print(f"{'1:'+str(nom):>6}{p_theory:>12.1f}%{be:>12.1f}%{'teng — edge YO Q':>28}")
print("""
  -> Adolatli o'yinda RR qancha bo'lsa ham kutilma NOL.
  -> 1:10 o'z-o'zidan hech narsa bermaydi.
  -> Faqat TP ga yetish ehtimoli nazariydan YUQORI bo'lsa edge paydo bo'ladi.
""")

print("="*76)
print("4) PSIXOLOGIK VA AMALIY TO'SIQLAR")
print("="*76)
import random
random.seed(97)
def streak_sim(wr, n=200, sims=20000):
    worst=[]
    for _ in range(sims):
        cur=mx=0
        for _ in range(n):
            if random.random()<wr: cur=0
            else:
                cur+=1; mx=max(mx,cur)
        worst.append(mx)
    worst.sort()
    return worst[len(worst)//2], worst[int(len(worst)*0.95)]
print(f"{'WR':>6}{'median eng uzun ketma-ket zarar':>34}{'95%':>8}")
for wr in (0.50, 0.30, 0.20, 0.12):
    m,p95 = streak_sim(wr)
    print(f"{wr*100:>5.0f}%{m:>33}{p95:>8}")
print("""
  -> 12% WR da 200 savdoda ketma-ket 17-30 ta zarar NORMAL.
  -> Buni ko'tarish uchun temir asab kerak. Ko'pchilik 8-10 tadan keyin tashlaydi.
""")

print("="*76)
print("5) 'BANK MANIPULATSIYASI' — nima haqiqat, nima marketing")
print("="*76)
print("""
  HAQIQAT (tasdiqlangan):
   + Stop hunting mavjud — likvidlik hovuzlari (equal highs/lows) tozalanadi
   + Institutlar likvidlik qidiradi, chunki katta hajmni joylash kerak
   + Sessiya ochilishlarida oqim keskin oshadi
   + Yangilik paytida spread kengayadi, slippage oshadi

  MARKETING (isbotlanmagan):
   - "Banklar sizning shaxsiy stopingizni ko'radi" -> ko'rmaydi.
     Broker ko'radi, bank emas. Va A-book brokerga bu foydasiz.
   - "Manipulyatsiyani oldindan bilish mumkin" -> agar bilinsa, u
     manipulyatsiya bo'lmay qolardi
   - "1:10 kafolatlangan" -> hech narsa kafolatlanmagan

  MUHIM: "stop hunting bor" degani "men uni bashorat qila olaman" degani EMAS.
""")

print("="*76)
print("6) SHUNGA O'XSHASH DA'VOLARNI TEKSHIRISH")
print("="*76)
qs = [
 "Ochiq statistika bormi? (Myfxbook/FXBlue - broker bilan bog'langan)",
 "Necha savdoda? n<200 bo'lsa xulosa yo'q",
 "MAE/MFE ko'rsatilganmi? (1:10 da ko'p savdo 1:3 da qaytadi)",
 "Slippage hisobga olinganmi? Kichik SL da bu HAL QILUVCHI",
 "Qaysi brokerda? Spred 0.3 va 1.3 - butunlay boshqa natija",
 "Yangilik paytida savdo qiladimi? (o'sha yerda slippage 5-10x)",
 "Ketma-ket 20 zararni ko'rsatgan skrinshot bormi?",
]
for i,q in enumerate(qs,1): print(f"  {i}. {q}")
