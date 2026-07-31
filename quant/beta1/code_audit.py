# -*- coding: utf-8 -*-
"""BETA 1 + LAOL indikatorining strukturaviy tahlili."""

print("="*74)
print("1) KOMBINATORIK PORTLASH — nechta setup varianti bor?")
print("="*74)

base = ["S1","S2","S3","S4"]          # bazaviy setuplar
intra = ["EST+RET","EM","LV","NEG","ZONE"]
patterns = ["X3 Third","X3 First","LAOL Neg","SN","SN [EM]","FU","FU [TBE]","HCS"]
states = ["FORMING","ESTABLISHED","EST_RETEST","FORMING_FRESH","RESPECTED"]
cats = ["ENTRY","SCALP","INTRA"]

# base kombinatsiyalari (S1..S3 birlashishi mumkin, S4 alohida)
base_combos = 2**3 - 1 + 1   # S1,S2,S3 ning bo'sh bo'lmagan kombinatsiyalari + S4
print(f"  Bazaviy setup kombinatsiyalari : {base_combos}")
print(f"  Intra modifikatorlar           : {len(intra)}")
print(f"  Pattern turlari                : {len(patterns)}")
print(f"  Box holatlari                  : {len(states)}")
print(f"  Kategoriyalar                  : {len(cats)}")
total = base_combos * len(intra) * 2   # x2 = bear/bull
print(f"\n  Faqat 'setup_display' variantlari: {total}")
print(f"  Pattern matnlari bilan birga    : {total*len(patterns)}")

print("""
  -> Bu YUZLAB turli signal turi degani.
  -> Har biri alohida statistik gipoteza.
  -> 300 savdo bu kombinatsiyalarga bo'linsa, har biriga 1-2 ta tushadi.
""")

print("="*74)
print("2) PARAMETRLAR — nechta 'sozlanadigan' son bor?")
print("="*74)
params = [
 ("TF_COUNT / TFS ro'yxati", 25, "qaysi 25 ta taymfreym tanlangan"),
 ("ENTRY chegarasi", 2, "1-5 daqiqa"),
 ("SCALP chegarasi", 2, "6-20 daqiqa"),
 ("INTRA chegarasi", 2, "30-120 daqiqa"),
 ("TP_MULTIPLIER", 1, "8"),
 ("PIP_TARGET", 1, "40"),
 ("SETUP_LOOKBACK", 1, "5"),
 ("LAOL_DELETE_DELAY", 1, "2"),
 ("protection_candles", 2, "ENTRY=3, boshqa=1"),
 ("setup window", 1, "10 bar"),
 ("f_should_record_setup", 1, "5 bar"),
 ("HCS box TF filtri", 2, "faqat '50' va '60'"),
 ("laol tolerance", 1, "mintick*2"),
 ("scan tolerance", 1, "mintick*3"),
 ("f_find_next_extreme lookback", 1, "500"),
]
tot_p = sum(p[1] for p in params)
print(f"  {'parametr':<34}{'soni':>6}  qiymat")
for n,c,v in params:
    print(f"  {n:<34}{c:>6}  {v}")
print(f"\n  JAMI ERKINLIK DARAJASI: ~{tot_p}")
print("""
  -> Taqqoslash uchun: Donchian trend-following da 3 ta parametr.
  -> 44 parametr = juda katta overfitting maydoni.
""")

print("="*74)
print("3) REPAINTING XAVFI — eng jiddiy muammo")
print("="*74)
print("""
  f_get_tf_data() shuni qaytaradi:
      request.security(..., [open[2],high[2],low[2],close[2],
                             open[1],high[1],low[1],close[1],
                             open, high, low, close,      <-- JORIY, YOPILMAGAN
                             time, barstate.isconfirmed])

  lookahead=barmerge.lookahead_off  -> BU YAXSHI (kelajakka qaramaydi)

  LEKIN: joriy (yopilmagan) HTF sham ishlatilyapti.
  Masalan 60-daqiqalik shamning 5-daqiqasida:
      p_h, p_l  = shu 5 daqiqadagi maksimum/minimum
      55 daqiqadan keyin bu qiymatlar BOSHQACHA bo'ladi

  Natija:
   - Pattern paydo bo'ladi -> yo'qoladi -> yana paydo bo'ladi
   - Tarixda grafik "mukammal" ko'rinadi (oxirgi holat saqlanadi)
   - Jonli savdoda signal titraydi

  KODDA HIMOYA BOR:
   + i_conf (barstate.isconfirmed) ko'p joyda tekshiriladi
   + box yaratish faqat p_conf da
   + "FORMING" vs "CONFIRMED" ajratilgan

  HIMOYA YETARLI EMAS:
   - f_calculate_patterns() HAR BAR chaqiriladi, conf tekshirmasdan
   - arr_fu_bear, arr_sn_bear va h.k. yopilmagan shamdan to'ladi
   - alert(..., alert.freq_once_per_bar) -> yopilmagan shamda ham otadi
   - LAOL chiziqlari high/low bilan tekshiriladi (intrabar)
""")

print("="*74)
print("4) SL/TP MANTIQI")
print("="*74)
print("""
  SL:  bear_sl = high
       keyin f_find_next_extreme_candle("bear", high) bilan KENGAYTIRILADI
       -> oxirgi 500 bar ichida joriy high dan yuqori birinchi high

       BU MUAMMO: SL oldindan aytib bo'lmaydigan darajada kengayadi.
       Ba'zan 2 pip, ba'zan 200 pip. Risk boshqaruvi buziladi.

  TP:  entry - (sl_range * 8)   -> nominal 1:8 RR

       Agar SL 200 pip bo'lsa, TP 1600 pip. Bu XAUUSD da yetib bo'lmas.
       Agar SL 2 pip bo'lsa, TP 16 pip. Spred bilan real RR ~1:5.

  40 PIP CHIZIG'I: alohida target, lekin qaysi biri asosiy - noaniq.
""")

print("="*74)
print("5) BU INDICATOR, STRATEGY EMAS")
print("="*74)
print("""
  indicator(...) deb e'lon qilingan -> TradingView backtest YO'Q.
  Ya'ni:
   - win rate yo'q
   - profit factor yo'q
   - drawdown yo'q
   - equity curve yo'q

  Faqat grafikdagi qutilar va alertlar.

  Odam grafikka qarab "vaay ishlayapti" deydi. Lekin bu ILLYUZIYA:
  chunki repaint bo'lgan signallar tarixda mukammal ko'rinadi.
""")
