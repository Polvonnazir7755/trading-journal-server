# -*- coding: utf-8 -*-
"""Strategiya 'slot' narxi: nima yo'qotamiz, nima yutamiz?"""
import random, math
random.seed(53)

def t_stat(rs):
    n=len(rs); m=sum(rs)/n
    sd=(sum((x-m)**2 for x in rs)/(n-1))**0.5 if n>1 else 0
    return (m/(sd/math.sqrt(n))) if sd else 0.0

print("="*70)
print("1) BONFERRONI NARXI — qo'shimcha strategiya qancha kuch yeydi?")
print("="*70)
print(f"{'strategiya':>11}{'chegara t':>11}{'0.20R aniqlash':>17}{'yo qotilgan kuch':>19}")
base=None
for k,thr in [(1,2.00),(2,2.24),(3,2.39),(4,2.50),(5,2.58)]:
    det=sum(1 for _ in range(4000)
            if t_stat([random.gauss(0.20,1.8) for _ in range(300)])>thr)/4000
    if base is None: base=det
    print(f"{k:>11}{thr:>11.2f}{det*100:>16.0f}%{(base-det)*100:>18.0f}%")
print("""
  -> 1 -> 3 strategiya: kuch 47% dan 32% ga tushadi (-15 punkt)
  -> 3 -> 4: yana -3 punkt.  Har qo'shimcha slot ARZONLASHIB boradi,
     lekin BIRINCHI qo'shimchalar qimmat.
""")

print("="*70)
print("2) BENCHMARK (nazorat) — Bonferroni TALAB QILMAYDI")
print("="*70)
print("""
  MUHIM FARQ:

  (a) STRATEGIYA NOMZODI = "bu pul keltiradimi?" degan da'vo
      -> Bonferroni tuzatish KERAK (ko'p taqqoslash)

  (b) BENCHMARK / NAZORAT = "boshqalar shundan yaxshiroqmi?" savoli
      -> tuzatish KERAK EMAS, chunki edge topmoqchi emasmiz
      -> u shunchaki O'LCHOV CHIZG'ICHI

  Misol: Gann'ni benchmark qilsak, u BEPUL. Slot yemaydi.
  Photon undan yaxshi bo'lsa -> ma'noli. Yomon bo'lsa -> tashvishli.
""")

print("="*70)
print("3) 'NEGA BU EDGE MAVJUD?' — nomzodlarni saralash")
print("="*70)
rows=[
 ("Gann Sq9",        "yo'q",                      "past",  "BENCHMARK"),
 ("Photon/SMC",      "chakana xatolar, likvidlik","o'rta", "asosiy"),
 ("Trend-following", "risk premiyasi, poda effekti","YUQORI","tavsiya"),
 ("Sessiya/vaqt",    "institutsional oqim vaqti", "YUQORI","tavsiya"),
 ("Vola breakout",   "vola klasterlanishi (GARCH)","yuqori","yaxshi"),
 ("Mean reversion",  "likvidlik ta'minoti",       "o'rta", "ehtiyot"),
 ("Fibonachchi",     "yo'q",                      "past",  "o'tkazib yuborish"),
]
print(f"  {'strategiya':<18}{'nega edge bor?':<30}{'ishonch':<9}{'qaror'}")
for a,b,c,d in rows:
    print(f"  {a:<18}{b:<30}{c:<9}{d}")
print("""
  Qoida: "nega bu edge hali yo'qolmagan?" savoliga javobi BORLARNI oling.
""")

print("="*70)
print("4) ISH HAJMI — qaysi biri sizning vaqtingizni yeydi?")
print("="*70)
print(f"  {'strategiya':<20}{'sizning vaqtingiz':>20}{'mening vaqtim':>16}")
for a,b,c in [("Photon (diskretsion)","30 soat","1 hafta"),
              ("Gann (avtomatik)","0 soat","3 soat"),
              ("Trend-following","0 soat","4 soat"),
              ("Sessiya effekti","0 soat","2 soat")]:
    print(f"  {a:<20}{b:>20}{c:>16}")
print("""
  -> Avtomatik strategiyalar sizning vaqtingizni UMUMAN yemaydi.
  -> Ular uchun "slot" tushunchasi deyarli bo'sh gap.
""")
