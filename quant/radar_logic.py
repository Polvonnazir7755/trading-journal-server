# -*- coding: utf-8 -*-
"""
"Fanar" g'oyasi: yo'lda to'siq bormi?
Uch xil ishlatish mumkin — qaysi biri eng foydali?
"""
import math

print("="*74)
print("MUHIM SAVOL: nega narx 6R da qaytdi?")
print("="*74)
print("""
  Ehtimoliy sabablar:
    1) O'sha yerda QARAMA-QARSHI zona bor edi (OB/FVG)
    2) O'sha yerda yechilmagan LIKVIDLIK bor edi (EQH/EQL)
    3) Shunchaki tasodif

  Agar 1 yoki 2 bo'lsa — buni OLDINDAN bilish mumkin edi!
  Chunki zonalar savdo ochilishidan OLDIN mavjud.
""")

print("="*74)
print("SHUNING UCHUN: 3 xil ishlatish mumkin")
print("="*74)
uses = [
 ("A. KIRISH FILTRI",
  "TP yo'lida katta to'siq bo'lsa — savdoga KIRMAYMIZ",
  "WR to'g'ridan-to'g'ri oshadi", "savdo kamayadi"),
 ("B. DINAMIK TP",
  "TP ni to'siqdan OLDIN qo'yamiz (8R o'rniga 5R)",
  "6R muammosi hal bo'ladi", "katta yutuqlar kichrayadi"),
 ("C. ADAPTIV SL",
  "Xavf yaqin bo'lsa SL ni BE ga suramiz",
  "zarar kamayadi", "erta chiqish ko'payadi"),
]
for name, what, good, bad in uses:
    print(f"\n  {name}")
    print(f"    Nima qiladi : {what}")
    print(f"    Yaxshi      : {good}")
    print(f"    Yomon       : {bad}")

print("\n" + "="*74)
print("MENING FIKRIM: B > A > C")
print("="*74)
print("""
  Nega DINAMIK TP (B) birinchi?

  Sizning muammongiz: "6R ga bordi, keyin qaytdi"
  Sabab: 6R da to'siq bor edi.

  ADAPTIV SL (C) bu holatda nima qiladi?
    -> narx 6R ga borgach SL ni suradi -> siz +5R olasiz
    -> LEKIN bu FAQAT narx u yerga borgandan KEYIN

  DINAMIK TP (B) nima qiladi?
    -> TP ni 5.7R ga qo'yadi (to'siqdan oldin)
    -> narx 6R ga borganda TP OLINGAN bo'ladi
    -> +5.7R kafolatlangan

  B usuli C dan YAXSHIROQ, chunki u OLDINDAN ishlaydi.
""")

print("="*74)
print("TP MASOFASI va YETISH EHTIMOLI (sizning ma'lumotingizdan)")
print("="*74)
MEAN = 8.0 / -math.log(0.187)
print(f"{'TP':>6}{'yetish %':>11}{'exp (R)':>10}{'izoh':>26}")
for tp in (2,3,4,5,6,8):
    p = math.exp(-tp/MEAN)
    exp = p*tp - (1-p)
    note = "hozirgi" if tp==8 else ""
    print(f"{str(tp)+'R':>6}{p*100:>10.1f}%{exp:>+10.2f}{note:>26}")
print("""
  -> Kichikroq TP = yuqoriroq WR, lekin exp tushishi mumkin
  -> DINAMIK TP: har savdoda TP boshqacha (to'siqqa qarab)
     Ya'ni to'siq uzoq bo'lsa 8R, yaqin bo'lsa 4R
""")

print("="*74)
print("⚠️  OGOHLANTIRISH: parametrlar soni")
print("="*74)
print(f"{'nima':>34}{'parametr':>10}")
for n, c in [("Hozirgi strategiya", 0), ("+ Radar skanerlash masofasi", 1),
             ("+ To'siq buferi", 1), ("+ Xavf chegarasi", 1),
             ("+ Qaysi zonalar hisoblanadi", 2), ("+ Zona 'kuchi' filtri", 1)]:
    print(f"{n:>34}{c:>10}")
print(f"{'JAMI YANGI':>34}{6:>10}")
print("""
  Har yangi parametr = yangi overfitting imkoniyati.
  Shuning uchun: BITTADAN qo'shing va har birini alohida sinang.
""")
