# -*- coding: utf-8 -*-
"""Qo'lda vs avtomatik backtest: vaqt va sifat solishtiruvi."""

print("="*68)
print("1) VAQT XARAJATI — 300 ta savdo yig'ish uchun")
print("="*68)
manual_min = 6      # 1 setup topish + yozish (bar replay)
print(f"{'Usul':<28}{'1 savdo':>10}{'300 savdo':>14}{'kuniga 2 soat':>18}")
tot = 300*manual_min/60
print(f"{'Qo lda (bar replay)':<28}{manual_min:>8} min{tot:>12.0f} soat{tot/2:>14.0f} kun")
print(f"{'Yarim-avtomatik':<28}{2:>8} min{300*2/60:>12.0f} soat{300*2/60/2:>14.0f} kun")
print(f"{'To liq avtomatik':<28}{0.01:>8} min{300*0.01/60:>12.1f} soat{'~1':>14} kun")

print("\n" + "="*68)
print("2) SIFAT — nima yo'qotiladi/yutiladi")
print("="*68)
rows = [
    ("Kontekst tushunish",        "yuqori", "o'rta",  "yo'q"),
    ("Photon subyektiv POI",      "mumkin", "mumkin", "imkonsiz"),
    ("Hindsight bias xavfi",      "KATTA",  "o'rta",  "yo'q"),
    ("Overfitting xavfi",         "kichik", "o'rta",  "KATTA"),
    ("Namuna hajmi",              "kichik", "o'rta",  "katta"),
    ("Takrorlanuvchanlik",        "past",   "o'rta",  "100%"),
]
print(f"{'Mezon':<28}{'Qo lda':>12}{'Yarim':>12}{'Avto':>12}")
for a,b,c,dd in rows:
    print(f"{a:<28}{b:>12}{c:>12}{dd:>12}")

print("""
================================================================
3) ASOSIY MUAMMO: HINDSIGHT BIAS (o'tmishni bilib turib qaror)
================================================================
  Bar replay da ham siz bilasiz:
    - grafik qayerga borganini yarim eslaysiz
    - "bu POI ishlagan" deb ichingizda his qilasiz
    - shubhali setuplarni beixtiyor tashlab yuborasiz

  Natija: qo'lda backtest deyarli HAR DOIM real natijadan yaxshi chiqadi.
  Odatdagi farq: 30-50% optimistik.
""")
