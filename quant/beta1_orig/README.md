# BETA 1 + LAOL — ASL KOD, faqat strategy() ga aylantirilgan

**Fayl:** `BETA1_ASL_STRATEGY.pine`

---

## Nima o'zgardi — FAQAT SHU 2 TA

1. `indicator(...)` → `strategy(...)`
2. `alert(...)` bo'lgan joylarga `strategy.entry` / `strategy.exit` qo'shildi

**Boshqa hech narsa o'zgarmagan.**

---

## Nima O'ZGARMAGAN — tekshirib chiqing

| Element | Holati |
|---|---|
| `TF_COUNT = 25` | ✅ asl holicha (25 ta taymfreym) |
| `TP_MULTIPLIER = 8` | ✅ asl holicha |
| `PIP_TARGET = 40.0` | ✅ asl holicha |
| `SETUP_LOOKBACK = 5` | ✅ asl holicha |
| `LAOL_DELETE_DELAY = 2` | ✅ asl holicha |
| S1 / S2 / S3 / S4 ta'riflari | ✅ **aynan asl** |
| `f_find_next_extreme_candle(500)` | ✅ asl holicha |
| `request.security(... open, high, low, close ...)` | ✅ **asl holicha** (yopilmagan sham) |
| `protection_candles = f_is_entry ? 3 : 1` | ✅ asl holicha |
| FU / SN / X3 / LAOL / HCS / TBE mantiqi | ✅ aynan asl |
| HCS box faqat tf "50"/"60" | ✅ asl holicha |

Men **hech qanday filtr qo'shmadim, hech narsani o'chirmadim.**

---

## Oldingi versiyada nima noto'g'ri qilgan edim

Ochiq tan olaman — men juda ko'p narsani o'zgartirgan edim:

| Nima | Asl | Men qilgan |
|---|---|---|
| Taymfreymlar | 25 ta | ~~9 ta~~ |
| TP | SL × 8 | ~~SL × 3~~ |
| SL | 500 bar ekstremum | ~~ATR chegarali~~ |
| S3 | scalp EM asosida | ~~INTRA asosida~~ |
| S4 | faqat HCS | ~~HCS + retest~~ |
| Qo'shimcha filtrlar | yo'q | ~~HTF align, P&D, min tasdiq, range~~ |
| request.security | yopilmagan sham | ~~yopilgan sham~~ |

Natijada u **boshqa strategiya** bo'lib qolgan. Shuning uchun natija
indikatordan farq qilgan.

---

## Faqat savdo sozlamalari qo'shildi

Bular **asl mantiqqa ta'sir qilmaydi** — faqat savdo qanday
ochilishini belgilaydi:

```
Qaysi signalda savdo?   FINAL ENTRY / CONFIRMED / IKKALASI
Risk turi:              Foiz % / Dollar $
Risk %:                 2.0
Risk $:                 20.0
Komissiya hisobga...:   ☑
Komissiya $:            0.15
Slippage (tick):        2
TP = 40 pip:            ☐   (yoqilsa 8R o'rniga 40 pip)
```

### Nega bu kerak

Asl kodda **3 xil alert** bor:
- `BEAR/BULL FORMING` — hali tasdiqlanmagan
- `BEAR/BULL CONFIRMED` — M1 yopilgan
- `FINAL ENTRY BEAR/BULL` — barcha filtrlardan o'tgan

Qaysi biri savdo ochishini siz tanlaysiz. Indikatorda bularning
hammasi alert sifatida chiqadi.

### TP tanlovi

Asl kodda **ikkala target ham** chiziladi:
- `bear_tp = entry - (range × 8)` — asosiy TP box
- `target_40pip` — 40 pip chizig'i

Qaysi biri "haqiqiy" TP ekani asl kodda aniq emas. Shuning uchun
tanlash imkoniyati qo'ydim.

---

## Sinash tartibi

**1. Avval indikator bilan bir xil ekanini tekshiring**

Ikkalasini bitta grafikka qo'ying. Signal joylari **mos kelishi kerak**.

Agar mos kelmasa — menga ayting, xato bor.

**2. Keyin backtest**

```
Grafik:  XAUUSD M1 yoki M5
Davr:    Properties → Backtest date range → kengaytiring
Signal:  FINAL ENTRY (default)
TP:      SL × 8 (asl holicha)
```

**3. Natijani solishtiring**

| Rejim | Savdo | WR | Net |
|---|---|---|---|
| FINAL ENTRY | ? | ? | ? |
| CONFIRMED | ? | ? | ? |
| TP 40 pip | ? | ? | ? |

---

## ⚠️ Repaint haqida ogohlantirish

Asl kod `request.security` da **yopilmagan** shamni o'qiydi:

```pine
request.security(..., [open[2], ..., open, high, low, close, ...])
                                     ^^^^^^^^^^^^^^^^^^^^^^ joriy
```

Men buni **ataylab o'zgartirmadim** — siz asl kodni so'radingiz.

Lekin bu shuni anglatadi: **backtest natijasi jonli savdodan
yaxshiroq chiqishi mumkin**. Chunki tarixda "yopilgan" sham
ma'lumoti to'liq, jonli savdoda esa u hali shakllanmoqda.

Buni tekshirish uchun: backtest natijasini keyinroq forward test
bilan solishtirish kerak.


---

# 🛡️ BREAKEVEN va TRAILING qo'shildi

Siz so'ragan narsa. **Asl mantiqqa tegilmadi** — bu faqat pozitsiya
boshqaruvi, ya'ni savdo ochilgandan keyingi qism.

## Yangi bo'lim: POZITSIYA BOSHQARUVI

```
☐ Breakeven ko'chirish
   BE ga ko'chirish (R):   1.5
   BE ofset (R):           0.0

☐ Trailing stop
   Trailing masofa (R):    3.0
   Trailing boshlanishi:   2.0
```

Ikkalasi ham **default o'chiq** — avval asl natijani ko'ring, keyin yoqing.

---

## Siz to'g'ri fikrlagansiz — lekin bir nuans bor

### ✅ To'g'ri qismi

**"Bozor foydaga kirgandan keyin SL ni breakeven'ga o'tkazish kerak"**

Ha. Bu:
- Zarar sonini kamaytiradi
- Max drawdown'ni sezilarli yaxshilaydi
- Psixologik bosimni kamaytiradi

**"Hech qanday treyder 100% risk qilmaydi"** — to'g'ri. Professional
fondlar aynan shunday ishlaydi.

### ⚠️ Nuans: BE bepul emas

Har bir BE ko'chirish **potensial yutuqni ham o'ldiradi**.

Tasavvur qiling: narx 1.5R ga bordi → SL breakeven'ga ko'chdi →
narx qaytib BE ga tegdi → chiqdingiz **0R bilan**.

Lekin agar BE ko'chirmasangiz, narx yana ko'tarilib **8R** olishi
mumkin edi.

**Ya'ni:** BE zararni kamaytiradi, lekin foydani ham kamaytiradi.

### "20-30%" haqida

Siz "20-30% ga surish" dedingiz. TP 8R bo'lsa:

| Foiz | R da |
|---|---|
| 10% | 0.8R |
| **20%** | **1.6R** |
| 30% | 2.4R |
| 50% | 4.0R |

**Muhim:** 1.6R ga borish ehtimoli ~35%. Ya'ni har 3 savdodan 1 tasida
BE ishga tushadi. Bu ko'p.

Menimcha **1.5–2R** yaxshi boshlang'ich nuqta.

---

## BE vs Trailing — farqi

| | Breakeven | Trailing |
|---|---|---|
| Nima qiladi | SL ni kirishga ko'chiradi, **bir marta** | SL ni narx ortidan **doim** suradi |
| Natija | 0R yoki TP | 0R dan TP gacha **har qanday** qiymat |
| Yaxshi tomoni | oddiy, tushunarli | foydani ushlaydi |
| Yomon tomoni | katta harakatni o'tkazib yuboradi | erta chiqarishi mumkin |

**Trailing** siz aytgan "surib borish" — aynan shu.

---

## ⚠️ MUHIM: modelim ishonchsiz

Men simulyatsiya qildim, lekin natija shubhali chiqdi (trailing +365R
degan raqam berdi — bu real emas).

Sabab: modelda narx **tekis** harakatlanadi deb faraz qilinadi. Haqiqiy
bozorda narx tebranadi — trailing ko'p marta erta ishga tushadi.

**Shuning uchun javobni faqat REAL BACKTEST beradi.**

---

## Sinash tartibi

Bittadan sinang va yozib boring:

| # | Sozlama | Savdo | WR | Net | Max DD |
|---|---|---|---|---|---|
| 1 | Hech narsa (asl) | 123 | 18.7% | $484 | $565 |
| 2 | BE 1.5R | ? | ? | ? | ? |
| 3 | BE 2.5R | ? | ? | ? | ? |
| 4 | Trailing 3R (start 2R) | ? | ? | ? | ? |
| 5 | BE 1.5R + Trail 3R | ? | ? | ? | ? |

**Nimaga qarash kerak:**

- **Net profit** tushishi normal — muhimi qancha
- **Max DD** sezilarli kamayishi kerak
- **Recovery factor** = Net / MaxDD → 2.0+ bo'lsa yaxshi

Hozirgi holat: `484 / 565 = 0.86` — **bu yomon**. DD foydadan katta.

Maqsad: recovery factor'ni **2.0 dan yuqori** qilish. Foyda kamaysa ham,
chidasa bo'ladigan strategiya yaxshiroq.

---

## BE ofset nima

```
BE ofset (R):  0.1
```

SL kirish narxidan **0.1R yuqoriga** qo'yiladi. Nega kerak:

Toza breakeven'da (ofset 0) siz komissiya va spred tufayli **kichik
zarar** bilan chiqasiz. 0.1R ofset shuni qoplaydi.

Kichik detal, lekin 100+ savdoda sezilarli.


---

# 🎯 "6R GA BORDI, KEYIN SL OLDI" — YECHIM

Siz aynan **eng og'riqli muammoni** ko'rsatdingiz. Va haqsiz.

## Muammo qanchalik katta — raqamlar

Sizning 123 savdongiz MFE (eng yuqori nuqta) bo'yicha taqsimoti:

| MFE oralig'i | Savdo % | Izoh |
|---|---|---|
| 0–0.5R | 9.9% | deyarli darhol SL |
| 0.5–1R | 9.0% | kichik harakat |
| 1–2R | 15.3% | BE zonasi |
| 2–4R | 22.6% | yaxshi harakat |
| **4–6R** | **14.8%** | **juda yaqin edi** |
| **6–8R** | **9.6%** | **OG'RIQLI** |
| 8R+ | 18.8% | TP oldi |

**4R dan oshib, TP ga yetmagan: 24.4%** — bu 123 savdodan **~30 ta**.

Har biri `-1R` o'rniga `+4..7R` bo'lishi mumkin edi. Ya'ni siz
**~150R** ni yo'qotgansiz.

Siz "10-20% zararni oldini oladi" dedingiz — aslida **undan ham ko'p**.

---

## Professional yechimlar — solishtirish

Model sizning natijangizga kalibrlangan:

| # | Usul | Yutuq | BE | Zarar | Jami R | maxDD | **Recovery** |
|---|---|---|---|---|---|---|---|
| 1 | **Hech narsa (asl)** | 23 | 0 | 100 | +84 | 32.0 | **2.62** |
| 2 | BE @ 1.5R | 23 | 67 | 33 | +150 | 11.0 | 13.64 |
| 3 | BE @ 2.5R | 23 | 50 | 50 | +133 | 15.0 | 8.87 |
| 4 | **Trail 2R (start 3R)** | 66 | 0 | 57 | **+257** | **9.0** | **28.52** |
| 5 | Trail 3R (start 4R) | 53 | 0 | 70 | +196 | 12.9 | 15.18 |
| 6 | Partial 50%@2R + BE | 81 | 0 | 42 | +131 | **7.0** | 18.71 |
| 7 | Partial 50%@3R + BE | 66 | 0 | 57 | +133 | 10.5 | 12.62 |
| 8 | TP ni 4R ga tushirish | 53 | 0 | 70 | +142 | 12.0 | 11.83 |
| 9 | TP ni 3R ga tushirish | 66 | 0 | 57 | +141 | 9.0 | 15.67 |

**Eng yaxshi: Trailing 2R (start 3R)** — foyda 3 barobar, DD 3.5 barobar kam.

⚠️ **Lekin bu MODEL.** Real bozorda narx tebranadi, trailing erta ishga
tushishi mumkin. Haqiqiy javob — backtest.

---

## Yangi imkoniyat: QISMIY CHIQISH (partial TP)

Bu **eng professional yechim** — hedj-fondlar aynan shunday ishlaydi.

```
☑ Qismiy chiqish (partial TP)
   1-qism hajmi (%):  50
   1-qism TP (R):     2.0
   2-qism hajmi (%):  30
   2-qism TP (R):     4.0
```

**Qanday ishlaydi:**

Narx 2R ga yetdi → **50%** yopiladi (foyda cho'ntakda)
Narx 4R ga yetdi → yana **30%** yopiladi
Qolgan **20%** → 8R gacha ketadi yoki SL

**Natija:** "6R ga borib SL oldi" holatida siz **0R emas, +2.6R** olasiz.

### Nega bu yaxshi

| | To'liq 8R | Partial |
|---|---|---|
| 6R ga borib qaytdi | **−1R** | **+2.6R** |
| 8R oldi | +8R | +5.4R |
| Darhol SL | −1R | −1R |

Katta yutuqdan biroz yo'qotasiz, lekin **o'rta harakatlarni ushlaysiz**.

---

## Tavsiya etilgan sinov ketma-ketligi

Bittadan yoqing, natijani yozib boring:

| # | Sozlama | Net | Max DD | Recovery |
|---|---|---|---|---|
| 1 | Hech narsa | $484 | $565 | 0.86 |
| 2 | ☑ BE @ 1.5R | ? | ? | ? |
| 3 | ☑ Trailing 2R (start 3R) | ? | ? | ? |
| 4 | ☑ Partial 50%@2R + 30%@4R | ? | ? | ? |
| 5 | ☑ Partial + BE 1.5R | ? | ? | ? |

**Nimaga qarash kerak:**

Net profit tushishi **normal**. Muhimi — **Recovery factor** (Net/MaxDD).

- Hozir: **0.86** ❌
- Maqsad: **2.0+** ✓
- A'lo: **4.0+** ⭐

Chunki 57% drawdown'ga hech kim chiday olmaydi. Foyda kamaysa ham,
chidasa bo'ladigan strategiya ming marta yaxshi.


---

# 📡 RADAR — "yo'lni yorituvchi fanar"

Sizning g'oyangiz. **Juda yaxshi fikr** — va men uni jiddiy deb hisoblayman.

## Nega bu mantiqiy

Savol: **nega narx 6R da qaytdi?**

Uch ehtimol:
1. O'sha yerda qarama-qarshi zona bor edi (OB/FVG)
2. O'sha yerda yechilmagan likvidlik bor edi (LAOL/EQH/EQL)
3. Tasodif

**Agar 1 yoki 2 bo'lsa — buni OLDINDAN bilish mumkin edi.** Chunki bu
zonalar savdo ochilishidan **oldin** grafikda mavjud.

---

## ⚠️ Lekin bitta tuzatish

Siz "SL ni surib boramiz" dedingiz. Men buni **eng kuchsiz** variant deb
hisoblayman. Mana nega:

| Rejim | Nima qiladi | Qachon ishlaydi |
|---|---|---|
| **Dinamik TP** | TP ni to'siqdan **oldin** qo'yadi | savdo **ochilishida** |
| Kirish filtri | to'siq yaqin bo'lsa **kirmaydi** | savdo ochilishida |
| Adaptiv SL | xavf yaqinlashsa SL ni BE ga suradi | narx **borgandan keyin** |

**Sizning misolingizda (6R ga borib qaytdi):**

- **Adaptiv SL:** narx 6R ga borgach SL suriladi → siz **+5R** olasiz
- **Dinamik TP:** TP 5.7R ga qo'yiladi → narx 6R ga borganda **TP olingan**

Ikkinchisi yaxshiroq, chunki u **oldindan** ishlaydi va kafolatlangan.

**Shuning uchun default: "Dinamik TP".**

---

## TP masofasi va yetish ehtimoli

Sizning ma'lumotingizdan hisoblangan:

| TP | Yetish % | exp (R) |
|---|---|---|
| 2R | 65.8% | +0.97 |
| 3R | 53.3% | +1.13 |
| **4R** | **43.2%** | **+1.16** ⭐ |
| 5R | 35.1% | +1.10 |
| 6R | 28.4% | +0.99 |
| **8R (hozirgi)** | **18.7%** | **+0.68** |

**Diqqat:** 8R eng yomon expectancy beradi. 3-5R optimal zona.

Dinamik TP aynan shuni qiladi — to'siq uzoq bo'lsa 8R, yaqin bo'lsa 4R.

---

## Yangi bo'lim: RADAR

```
☐ Radarni yoqish
   Radar rejimi:              Dinamik TP  ← default
   ☑ Qarama-qarshi OB/FVG
   ☑ Yechilmagan likvidlik (LAOL)
   ☑ HCS zonalar
   To'siq buferi (R):         0.15
   Minimal TP (R):            1.5
   Kirish filtri: min yo'l:   2.0
```

### Nima qiladi

**Dinamik TP:**
```
Savdo ochildi, TP = 8R
Radar: 5.5R da qarama-qarshi OB bor
→ TP 5.35R ga ko'chadi (bufer 0.15R)
```

**Kirish filtri:**
```
Radar: 1.2R da to'siq bor
Chegara: 2.0R
→ SAVDOGA KIRILMAYDI
```

**Adaptiv SL:**
```
Narx harakatda, to'siqqa 0.5R qoldi
→ SL breakeven'ga suriladi
```

### Grafikda

To'q sariq punktir chiziq — eng yaqin to'siq.

Dashboard'da:
```
Radar    Dinamik TP  (bloklandi: 12)
```

---

## ⚠️ Ogohlantirish: parametrlar soni

Radar **6 ta yangi parametr** qo'shadi:

| Parametr | Soni |
|---|---|
| Skanerlash masofasi | 1 |
| To'siq buferi | 1 |
| Xavf chegarasi | 1 |
| Qaysi zonalar | 2 |
| Minimal TP | 1 |

Har yangi parametr — yangi **overfitting** imkoniyati.

**Shuning uchun bittadan sinang:**

| # | Sozlama | Return | Max DD | Recovery |
|---|---|---|---|---|
| 1 | Radar o'chiq (asl) | 49.5% | 41.1% | 1.21 |
| 2 | Radar: Dinamik TP | ? | ? | ? |
| 3 | Radar: Kirish filtri | ? | ? | ? |
| 4 | Radar: Adaptiv SL | ? | ? | ? |
| 5 | Radar: Hammasi | ? | ? | ? |

Har birini alohida yozib boring. Agar faqat bitta kombinatsiya yaxshi
chiqsa — bu overfitting belgisi.

---

## Halol prognoz

Menimcha:
- **Dinamik TP** — eng ehtimolli foydali (~60%)
- **Kirish filtri** — savdoni juda kamaytirishi mumkin (~30%)
- **Adaptiv SL** — kam ta'sir (~20%)

Lekin men xato bo'lishim mumkin. **Backtest aytadi.**
