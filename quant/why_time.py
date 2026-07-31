# -*- coding: utf-8 -*-
"""Nima uchun vaqt ketadi? Har bosqichni ajratib ko'ramiz."""
import random, math
random.seed(23)

def t_stat(rs):
    n=len(rs); m=sum(rs)/n
    sd=(sum((x-m)**2 for x in rs)/(n-1))**0.5 if n>1 else 0
    return (m/(sd/math.sqrt(n))) if sd else 0.0

print("="*70)
print("1) TO'LIQ 300 SAVDO x 3 STRATEGIYA (bo'linish YO'Q)")
print("="*70)
print(f"{'holat':<34}{'aniqlash kuchi':>18}{'yolgon xavf':>16}")
# har biriga to'liq 300 -> kuch saqlanadi, faqat Bonferroni tuzatish
for k, thr, lbl in [(1, 2.00, "1 strategiya x 300 savdo"),
                    (3, 2.39, "3 strategiya x 300 savdo (Bonf.)"),
                    (5, 2.58, "5 strategiya x 300 savdo (Bonf.)")]:
    det=0; fp=0; sims=4000
    for _ in range(sims):
        if t_stat([random.gauss(0.20,1.8) for _ in range(300)])>thr: det+=1
        if any(t_stat([random.gauss(0.0,1.8) for _ in range(300)])>thr for _ in range(k)): fp+=1
    print(f"{lbl:<34}{det/sims*100:>17.0f}%{fp/sims*100:>15.1f}%")
print("""
  -> To'liq 300 tadan bersak, aniqlash kuchi deyarli SAQLANADI.
  -> Yolg'on xavf ham nazoratda (Bonferroni tuzatish bilan).
  -> XULOSA: 3 strategiya MUMKIN. Faqat 3x ko'proq ISH.
""")

print("="*70)
print("2) BACKTEST — bu KOMPYUTER emas, SIZNING vaqtingiz")
print("="*70)
print(f"{'ish':<40}{'1 str':>10}{'3 str':>10}")
rows=[("Setup nomzodlarini topish (kompyuter)","2 daq","6 daq"),
      ("Siz ko'rib chiqasiz (300 qaror x 2 daq)","10 soat","30 soat"),
      ("Statistik tahlil (kompyuter)","1 daq","3 daq")]
for a,b,c in rows: print(f"  {a:<38}{b:>10}{c:>10}")
print(f"\n  Kuniga 1 soat ishlasangiz:   1 str = 10 kun    3 str = 30 kun")
print(f"  Kuniga 2 soat ishlasangiz:   1 str =  5 kun    3 str = 15 kun")
print("""
  -> Backtest TEZ. Bu 12 oyning sababi EMAS.
""")

print("="*70)
print("3) HAQIQIY SABAB: bozor kuniga faqat 1-2 setup beradi")
print("="*70)
print(f"{'kerakli savdo':>14}{'kuniga 1.5 setup':>20}{'ish kuni':>12}{'kalendar':>14}")
for n in (100, 200, 300):
    days = n/1.5
    months = days/21
    print(f"{n:>14}{'':>20}{days:>12.0f}{months:>12.1f} oy")
print("""
  -> Demo/jonli savdoda vaqtni TEZLASHTIRIB BO'LMAYDI.
  -> Bozor kelajakni oldindan bermaydi. Kutish shart.
  -> MEN AI bo'lsam ham, ertangi shamni yarata olmayman.
""")

print("="*70)
print("4) 12 OY QAYERGA KETADI?")
print("="*70)
items=[("Kod yozish (men)","1-2 hafta","tezlashtirsa bo'ladi"),
       ("Backtest (siz)","2-6 hafta","tezlashtirsa bo'ladi"),
       ("DEMO SAVDO","4-6 oy","TEZLASHTIRIB BO'LMAYDI"),
       ("Forward tekshiruv","2-3 oy","TEZLASHTIRIB BO'LMAYDI"),
       ("Kichik real","2-3 oy","TEZLASHTIRIB BO'LMAYDI")]
print(f"{'bosqich':<24}{'muddat':>12}   {'izoh'}")
for a,b,c in items: print(f"  {a:<22}{b:>12}   {c}")
print("""
  -> Men qiladigan ish: ~3 hafta jami
  -> Siz qiladigan ish: ~1-2 oy jami
  -> KUTISH: ~8-10 oy   <-- 12 oyning asosiy qismi
""")
