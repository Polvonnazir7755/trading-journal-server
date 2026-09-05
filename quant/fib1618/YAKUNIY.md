# 1.618 LEGENDA — YAKUNIY HISOBOT

**Sana:** 05.09.2026
**Manba g'oya:** TIGERS TRADING (MUSLIM ALI) YouTube efiri, 11.01.2026
**Kod:** `quant/fib1618/FIB1618_STRATEGY.pine`

---

## 1. QISQA XULOSA

Strategiya **ikkala sinalgan bozorda ham foydali**, lekin dastlabki
raqamlar (PF 4.2) haqiqiy emas — realistik kutilma ancha kamtarona.

| Ko'rsatkich | Optimistik (dastlabki) | **REALISTIK** |
|---|---|---|
| Profit factor | 4.2 | **1.8 – 2.8** |
| Max drawdown | 11% | **20 – 25%** |
| Expectancy | +0.9R | **+0.35 – 0.6R** |
| Win rate | 72% | **55 – 60%** |

**Video da'vosi rad etildi:** "garant 1.618" — 100% emas, ~46-63%.

---

## 2. YAKUNIY SOZLAMALAR

```
PATTERN ANIQLASH
  Pivot uzunligi              5        <- O'ZGARTIRMANG (pastda sabab)
  W/M eni (max bar)           60
  W/M eni (min bar)           5
  Ikki minimum farqi (%)      25
  Razvorot sharti             YOQ
  Trend tekshirish oynasi     30
  Neckline TANA bilan         YOQ

KIRISH NUQTASI
  Kirish usuli                4-OTE 0.5-0.618
  OTE quyi / yuqori           0.5 / 0.618
  Kirishni kutish (bar)       30

CHIQISH
  TP1 'garant'                1.618
  TP2 'prognoz'               2.618
  TP1 da yopiladigan hajm     100%     <- VIDEO QOIDASI NOTO'G'RI EDI
  TP1 dan keyin BE            (ahamiyatsiz, 100% da)
  SL bufer                    2%

REALISTIK XARAJAT
  Yoqilgan                    HA
  pip AVTOMATIK               HA       <- XAUUSD xatosini oldini oladi
  Spred / Komissiya / Slip / Swap   0.2 / 0.7 / 0.4 / 0.6  = 1.9 pip

RISK
  Risk turi                   Foiz %
  Risk %                      1.0      <- 5% EMAS (pastda sabab)

RADAR                         O'CHIQ   <- foyda bermadi
```

---

## 3. O'LCHANGAN NATIJALAR

### EURUSD M30 (Jan 2 – Sep 4, 2026, 8 oy)

```
Savdolar:        33  (24 yutuq / 7 zarar / 2 BE)
Win rate:        72.73%
Profit factor:   4.186
Net profit:      $2,257.69  ($1000 dan)
Max drawdown:    11.28%
Recovery factor: 11.10
Expectancy:      +0.615R
t-statistika:    3.57      p = 0.0004
```

### XAUUSD D (~1968 – 2026, to'g'ri pipSize=0.10 bilan)

```
Savdolar:        69  (39 yutuq / 30 zarar)
Win rate:        56.52%   95% CI: 44.8% - 68.2%
Profit factor:   1.827
Net profit:      $3,289.43
Max drawdown:    23.43%
Recovery factor: 5.61
Expectancy:      +0.360R
t-statistika:    2.50      p = 0.0123
Break-even WR:   41.6%  (zaxira 14.9 punkt)

Signal taqsimoti: W(long) foydali, M(short) ZARAR
```

**Xulosa:** EURUSD kuchli, XAUUSD zaif. Oltinda short signallari ishlamaydi
(20 yillik ko'tarilish trendi tufayli).

---

## 4. NIMA ISHLADI VA NIMA ISHLAMADI

### ✅ Ishladi

| Topilma | Ta'sir |
|---|---|
| **TP1 = 100%** (70/30 o'rniga) | PF 2.96 → 4.19, Net +$525 |
| OTE 0.5–0.618 da kirish | Model bashorati tasdiqlandi |
| Realistik xarajat qo'shish | Natijani 58% ga tuzatdi (XAUUSD) |

### ❌ Ishlamadi

| Sinov | Natija |
|---|---|
| **RADAR (fanar g'oyasi)** | DD ni tushirmadi (12.65% → 11.84%, shovqin) |
| To'siq gipotezasi | 70.6% vs 50.0%, lekin p = 0.285 — isbot yo'q |
| TP2 = 2.618 | **Hech qachon urilmagan** (0%) |
| Pivot optimallashtirish | Barqaror emas (pastda) |

---

## 5. ENG MUHIM OGOHLANTIRISH: PIVOT BARQAROR EMAS

| Pivot | Savdo | WR | Net | Max DD | **PF** |
|---|---|---|---|---|---|
| 3 | 59 | 57.6% | $1,198 | 22.48% | **1.604** |
| 4 | 45 | 77.8% | $4,019 | 11.74% | **3.975** |
| 5 | 33 | 72.7% | $2,258 | 11.28% | **4.186** |
| 6 | 31 | 51.6% | $355 | 26.90% | **1.413** |

```
PF:  1.6  →  4.0  →  4.2  →  1.4
      3      4      5      6
```

**Bu TOR CHO'QQI — klassik overfitting belgisi.**

Barqaror parametr shunday ko'rinardi: 3.5 / 3.9 / 4.2 / 3.8 (silliq).

Monte-Carlo (20k sinov): haqiqiy PF 2.85 bo'lsa ham, 31–59 savdolik
namunada PF **1.56 – 5.46** oralig'ida tasodifan tebranadi.
Bizning 1.41–4.19 diapazonimiz aynan shu ichiga tushadi.

**Xulosa:** pivot 4/5 farqi ehtimol SHOVQIN. Pivot 5 da qolamiz, chunki u
optimallashtirishdan OLDIN tanlangan edi.

**Realistik kutilma = 4 qiymatning o'rtachasi: PF ~2.8, DD ~18%.**

---

## 6. STATISTIK ISHONCH

Loyiha davomida **~26 ta test/variant** sinaldi.

Bonferroni tuzatishi: kerakli t = **3.09** (p < 0.05/26)

| Test | t | Holat |
|---|---|---|
| EURUSD M30 | 3.57 | ✅ o'tdi |
| XAUUSD D | 2.50 | ❌ o'tmadi |

**Ya'ni:** EURUSD natijasi statistik jihatdan mustahkam.
XAUUSD chegarada — ishonch past.

---

## 7. REAL SAVDOGA O'TISH REJASI

### Bosqich 0 — DEMO (majburiy)

```
Muddat:     kamida 30 savdo (EURUSD M30 da ~4 oy)
Maqsad:     backtest raqamlari real vaqtda takrorlanadimi?
Yozib bor:  har savdo — sana, kirish, SL, TP, natija, R
```

**O'tish sharti:** demo PF > 1.5 va DD < 25%.
Agar demo backtestdan keskin farq qilsa — TO'XTATING.

### Bosqich 1 — Kichik depozit

```
Depozit:    $300–500  (100$ EMAS — 1% risk uchun lot juda kichik)
Risk:       1%        (5% EMAS)
Aktiv:      EURUSD M30 (faqat bitta)
TF:         bitta     (M30+H1+H4 birga EMAS)
```

**Nega 1%?** 33 savdolik namuna, WR ning ishonch oralig'i keng.
5% risk bilan haqiqiy WR 50% ga tushsa — DD 40%+ bo'ladi.

**Nega $300+?** $100 da 1% = $1 risk, SL 30 pip → lot 0.0033.
Broker minimumi 0.01 → savdo qilib bo'lmaydi. Majburan 3-5% risk olasiz.

### Bosqich 2 — Kengaytirish shartlari

Riskni oshirish faqat shu shartlar bajarilsa:

| Shart | Qiymat |
|---|---|
| Real savdolar soni | 50+ |
| Real PF | > 1.5 |
| Real Max DD | < 20% |
| Real WR | backtest ± 10 punkt ichida |

Har 50 savdodan keyin riskni **1% → 1.5% → 2%** ga oshirish mumkin.
**Hech qachon 3% dan oshmang.**

### Bosqich 3 — Diversifikatsiya

TF qo'shmang (M30+H1 korrelyatsiyasi 0.75 — bu konsentratsiya).
**Aktiv qo'shing:** EURUSD + XAUUSD + US500, har biriga risk byudjetining
1/3 qismi.

---

## 8. QACHON TO'XTATISH KERAK (stop-loss qoidasi)

Strategiyani **darhol to'xtating** agar:

| Shart | Sabab |
|---|---|
| Real DD > 25% | Backtest chegarasidan oshdi |
| Ketma-ket 8 zarar | WR 56% da bu ehtimoli 0.4% — model buzilgan |
| 30 savdodan keyin PF < 1.0 | Edge yo'q |
| 3 oy davomida signal yo'q | Bozor rejimi o'zgargan |

Bu qoidalarni **oldindan yozing** va his-tuyg'uga qarab o'zgartirmang.

---

## 9. HALOL BAHO

**Nimaga ishonch bor:**
- Strategiyada haqiqiy edge bor (ikki bozorda, xarajat bilan foydali)
- Kirish mantiqi asosli (W/M + neckline + OTE retest)
- Repaint yo'q, look-ahead yo'q (tekshirilgan)
- TP1=100% topilmasi bizning o'z hissamiz — video muallifi buni bilmagan

**Nimaga ishonch YO'Q:**
- Parametr barqarorligi (pivot 3/6 da PF 1.4-1.6 ga tushadi)
- XAUUSD natijasi Bonferroni chegarasidan o'tmadi
- EURUSD faqat 8 oy, 33 savdo — bitta bozor rejimi
- Bar magnifier yo'q: SL va TP bir barda urilsa TradingView optimistik tanlaydi

**Kutilma:**
$300 depozit, 1% risk, EURUSD M30 → yiliga **~15-30%** (agar edge saqlansa).
Bu "Dubay uyi" emas, lekin S&P 500 dan yaxshiroq.

---

## 10. KODDAGI TUZATISHLAR (05.09.2026)

1. **pipSize avtomatik aniqlash** — `pipAuto` inputi qo'shildi.
   XAUUSD da 0.0001 qoldirib yuborish xatosi natijani 58% ga buzgan edi.
2. **TP1 hisoblagichi tuzatildi** — `tp1Pct=100` rejimida savdo darhol
   yopilgani uchun `position_size != 0` sharti hisoblagichni bloklab qo'ygan edi.

---

## 11. TEKSHIRILMAGAN / KEYINGI ISHLAR

| № | Ish | Nega muhim |
|---|---|---|
| 1 | Demo forward test (30+ savdo) | Yagona haqiqiy tasdiq |
| 2 | Uchinchi bozor (GBPUSD, US500) | Curve-fitting tekshiruvi |
| 3 | EURUSD H1/H4 | TF barqarorligi |
| 4 | Qolgan 4 kirish usuli (Imbalans, OB) | Faqat OTE sinalgan |
| 5 | Oltinda faqat LONG | Short zarar keltirmoqda |

**Diqqat:** har yangi test Bonferroni chegarasini ko'taradi.
Yangi test qilishdan oldin — demo natijasini kuting.
