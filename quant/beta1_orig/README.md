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
