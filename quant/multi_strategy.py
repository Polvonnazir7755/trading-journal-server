# -*- coding: utf-8 -*-
"""1 ta strategiya chuqur vs 5 ta strategiya yuzaki — qaysi biri to'g'ri?"""
import random, math
random.seed(17)

def t_stat(rs):
    n=len(rs); m=sum(rs)/n
    sd=(sum((x-m)**2 for x in rs)/(n-1))**0.5 if n>1 else 0
    return (m/(sd/math.sqrt(n))) if sd else 0.0

print("="*72)
print("A) KO'P TAQQOSLASH MUAMMOSI")
print("   Barcha strategiyalar BEFOYDA (exp=0). Nechtasi 'yaxshi' ko'rinadi?")
print("="*72)
print(f"{'strategiya soni':>16}{'kamida 1 ta t>2':>20}{'yolgon topilma':>18}")
for k in (1,3,5,10,20):
    hits=0; sims=4000
    for _ in range(sims):
        found=False
        for _s in range(k):
            rs=[random.gauss(0,1.8) for _ in range(100)]
            if t_stat(rs)>2.0: found=True
        if found: hits+=1
    print(f"{k:>16}{hits/sims*100:>19.1f}%{'  <-- ' + ('XAVFLI' if hits/sims>0.15 else 'ok'):>18}")

print("""
  -> Har bir strategiya alohida 5% xato darajasida sinaladi, lekin
     ko'proq sinasangiz, kamida bittasi tasodifan 'yaxshi' chiqadi.
  -> 10 ta -> 22%, 20 ta -> 40% yolg'on topilma ehtimoli.
""")

print("="*72)
print("B) NAMUNA BO'LINISHI — 300 ta savdo cheklovi")
print("="*72)
print(f"{'strategiya':>11}{'savdo/str':>11}{'aniqlash kuchi (0.2R edge)':>30}")
for k in (1,2,3,5):
    n=300//k
    det=0; sims=3000
    for _ in range(sims):
        rs=[random.gauss(0.20,1.8) for _ in range(n)]
        if t_stat(rs)>2.0: det+=1
    print(f"{k:>11}{n:>11}{det/sims*100:>29.1f}%")
print("""
  -> 0.20R edge JUDA KICHIK signal: 300 savdoda ham atigi ~47% aniqlanadi.
  -> Namunani 5 ga bo'lsangiz, aniqlash kuchi 13% ga tushadi —
     edge BOR bo'lsa ham deyarli ko'rmaymiz.
  -> Xulosa: kam savdo bor ekan, ularni BITTA savolga sarflash kerak.
""")

print("="*72)
print("C) BEPUL KESIMLAR — bitta backtestdan nechta savol")
print("="*72)
print("""  MUHIM FARQ:

  (1) 5 ta ALOHIDA strategiya = 5x ko'proq savdo kerak
      (masalan: Photon + ICT + trend-following + mean reversion + breakout)
      -> namuna bo'linadi, kuch yo'qoladi

  (2) 1 ta strategiya + KESIMLAR = qo'shimcha savdo KERAK EMAS
      (MTF faza A/B/C/D, LC-1 vs LC-2A, LDN vs NY, SL o'lchami...)
      -> bir xil 300 savdodan 10+ savol javob oladi
      -> LEKIN: kesimlarni OLDINDAN yozib qo'yish shart
""")

print("="*72)
print("D) OLDINDAN E'LON QILISH (pre-registration) ta'siri")
print("="*72)
print(f"{'yondashuv':<42}{'yolgon topilma xavfi':>24}")
rows=[("Oldindan 3 ta kesim e'lon qilingan","past (~7%)"),
      ("Backtestdan keyin 20 ta kesim qidirish","JUDA YUQORI (~64%)"),
      ("Bonferroni tuzatish bilan 10 kesim","past (~5%)")]
for a,b in rows: print(f"  {a:<40}{b:>24}")
print("""
  -> Yechim: kesimlar ro'yxatini BACKTESTDAN OLDIN yozamiz va muzlatamiz.
  -> Keyin topilgan har qanday 'qiziq' narsa -> gipoteza, natija emas.
""")
