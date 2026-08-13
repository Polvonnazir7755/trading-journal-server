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
