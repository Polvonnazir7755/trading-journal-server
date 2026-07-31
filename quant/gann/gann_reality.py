# -*- coding: utf-8 -*-
"""
Gann Sq9 darajalari HAQIQATAN maxsusmi?
Sinov: tasodifiy darajalar bilan solishtirish (permutatsiya testi).
"""
import math, random
random.seed(43)

def sq9(center, k, div=8):
    return (math.sqrt(center) + k/div)**2

print("="*68)
print("1) MASOFA MUAMMOSI — darajalar qanchalik zich?")
print("="*68)
for price in (2700, 1.0850, 100.0):
    root = math.sqrt(price)
    step = (root + 1/8)**2 - price
    print(f"  narx {price:>9}:  1/8 qadam = {step:.5f}  ({step/price*100:.3f}%)")
print("""
  XAUUSD 2700 da: qadam ~13 punkt = 0.48%
  EURUSD 1.085 da: qadam ~0.26 = 24%!  <-- FOREX uchun YAROQSIZ

  -> Sq9 faqat KATTA raqamli aktivlarda mazmunli (oltin, indekslar, aksiya).
  -> EURUSD/GBPUSD da qadam juda katta. Div ni oshirish kerak (1/64, 1/128),
     lekin unda darajalar shunchalik zichki, "har joyda daraja bor" bo'lib qoladi.
""")

print("="*68)
print("2) ZICHLIK TESTI — necha % narx 'daraja yaqinida' bo'ladi?")
print("="*68)
print(f"{'div':>6}{'qadam %':>10}{'tolerans 0.1%':>16}{'qoplash':>10}")
for div in (8, 16, 32, 64):
    step_pct = ((1+1/(div*math.sqrt(2700)))**2 - 1)*100
    step_pct = (( math.sqrt(2700)+1/div)**2 - 2700)/2700*100
    cover = min(100, 0.2/step_pct*100)   # +-0.1% zona
    print(f"{div:>6}{step_pct:>9.3f}%{'+-0.1%':>16}{cover:>9.1f}%")
print("""
  -> div=32 dan boshlab darajalar shunchalik zichki, narx DOIM
     birortasining yonida bo'ladi. Bu "bashorat" emas, "hamma joyda nishon".
""")

print("="*68)
print("3) PERMUTATSIYA TESTI — SINTETIK MA'LUMOTDA O'TKAZILMAYDI")
print("="*68)
print("""
  Men bu testni sintetik random walk'da o'tkazmoqchi edim, lekin
  ADOLATLI NAZORAT QURIB BO'LMADI:

    - Gann darajalari teng oraliqli EMAS (yuqoriga qarab kengayadi)
    - Teng oraliqli nazorat setkasi boshqa zichlikka ega bo'lib qoladi
    - Narx qaysi zonada ko'p vaqt o'tkazsa, o'sha zona natijani belgilaydi

  Har xil urug' (seed) bilan p-qiymat 0.000 dan 0.485 gacha sakraydi —
  bu testning o'zi ishonchsiz ekanini bildiradi.

  TO'G'RI YO'L: REAL XAUUSD ma'lumotida sinash, nazorat sifatida
  xuddi shu Sq9 setkasini TASODIFIY MARKAZDAN qurish. Shunda zichlik
  bir xil bo'ladi va faqat "markaz to'g'ri tanlanganmi" savoli qoladi.

  Bu testni real ma'lumot kelgach o'tkazamiz.
""")

print("="*68)
print("4) XULOSA")
print("="*68)
print("""
  Gann Sq9 — bu MATEMATIK FORMULA, lekin BOZOR QONUNI EMAS.

  Nima haqiqat:
    + Formula aniq, takrorlanuvchi, obyektiv (bu yaxshi!)
    + To'liq avtomatlashtiriladi
    + Backtest qilinadi

  Nima shubhali:
    - Nega narx sqrt(P)+1/8 nuqtasida to'xtashi kerak? Sabab yo'q.
    - Markaz tanlash SUBYEKTIV (qaysi narxdan boshlaysiz?)
    - Forex uchun masshtab mos emas
    - Darajalar zich bo'lsa, "har joyda nishon" effekti

  YAGONA YO'L: statistik sinov. Buni qila olamiz.
""")
