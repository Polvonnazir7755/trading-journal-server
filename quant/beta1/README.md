# BETA 1 + LAOL — backtest versiyasi

**Fayl:** `BETA1_BACKTEST.pine`

Asl indikatorning mantiqi saqlangan, lekin **o'lchash mumkin** qilingan.

---

## Asl koddan 5 ta farq

### 1. REPAINT tuzatildi ⭐ (eng muhim)

Asl kod:
```pine
request.security(..., [open, high, low, close, ...])
                       ^^^^^^^^^^^^^^^^^^^^^^ YOPILMAGAN sham
```

Bu versiya:
```pine
request.security(..., [open[1], high[1], low[1], close[1], ...])
                              ^^^ faqat YOPILGAN
```

Asl kodda 60 daqiqalik shamning 5-daqiqasida `p_h`, `p_l` — bu 5 daqiqadagi
ekstremum. 55 daqiqadan keyin ular **boshqacha** bo'ladi. Natijada tarixda
signallar mukammal ko'rinadi, jonli savdoda titraydi.

### 2. `indicator()` → `strategy()`

Endi TradingView **Strategy Tester** beradi:
win rate, profit factor, max drawdown, equity curve, trade list.

### 3. 25 TF → 9 TF

3 ENTRY + 3 SCALP + 3 INTRA. Hammasi sozlanadi.

Sabab: 25 ta `request.security` — bu sekin va TradingView limitiga uriladi.
9 ta yetarli, chunki qo'shni taymfreymlar (1m/2m/3m/4m) deyarli bir xil
signal beradi.

### 4. SL cheklandi

Asl kod:
```pine
f_find_next_extreme_candle(direction, sl, lookback = 500)
```
SL oxirgi **500 bar** ichidagi ekstremumga ko'chardi — ba'zan 2 pip,
ba'zan 200 pip. Risk boshqaruvi buzilardi.

Endi: `SL maks (ATR)` parametri bilan chegaralangan (default 5×ATR).

### 5. Setup bo'yicha statistika

Dashboard'da S1, S2, S3, S4 alohida:
```
SETUP STATISTIKASI    win/jami  WR
S1                      14/38   37%
S2                       9/21   43%
S3                       5/18   28%
S4                       3/11   27%
JAMI / Net             88 / +412
```

---

## Saqlangan mantiq

Asl koddan ko'chirilgan:

| Element | Ta'rifi |
|---|---|
| **FU** | Oldingi shamdan chiqib, ichkariga yopilish |
| **SN** | Ikkala tomonni olib, tana ichkarida |
| **X3** | Oldingi diapazonni qamrab, ikki soyali |
| **X3 First** | Oldingi sham X3, joriy teskari siljish |
| **LAOL** | Inside bar darajasi |
| **HCS** | Mavjud FU/SN qutiga qayta tegish |
| **TBE** | 5 bosqichli ketma-ketlik |
| **S1–S4** | ENTRY va SCALP moslashuvi |

---

## DEBUG panel

Chap pastda — nega savdo yo'qligini bosqichma-bosqich ko'rsatadi:

```
DEBUG — nega savdo yo'q?           soni
S1-S4 baza shakllandi               412
  + LAOL buzildi                    186
  + SCALP FU/SN retest               94
  + sessiya/guard/cooldown           71
OCHILGAN SAVDO                       71
Baza turlari S1/S2/S3/S4    180/95/88/49
Aktiv quti / LAOL                 18 / 7
```

Qaysi qatorda raqam **keskin tushsa** — muammo o'sha yerda:

| Kam bo'lsa | Yechim |
|---|---|
| Baza | ③ da ko'proq pattern yoqing |
| LAOL | ④ da "LAOL buzilishi shart" ni o'chiring |
| SCALP retest | ④ da "SCALP FU/SN retest" ni o'chiring |
| Sessiya/cooldown | ⑥ sessiyani o'chiring, cooldown 5→2 |

---

## Sozlash tartibi

**1.** Properties → Backtest date range → **2022.01.01**

**2.** DEBUG panelga qarang, savdo sonini 50+ ga yetkazing

**3.** 50+ bo'lgach — **hech narsani o'zgartirmasdan** natijani o'qing

**4.** Keyin `TP = SL × 8` ni 4, 6, 10 bilan sinang.
Agar faqat 8 da ishlasa — bu **overfitting** belgisi.

---

## ⚠️ Kutilgan natija

Men oldin tahlil qilganimda ehtimollarni shunday baholagan edim:

| Natija | Ehtimol |
|---|---|
| Repaint tuzatilgach natija yomonlashadi | ~55% |
| Kichik edge, lekin overfitted | ~30% |
| Haqiqiy edge | ~15% |

**Agar bu versiya asl indikatordan yomon chiqsa — bu repaint tasdiqlanishi.**

Ya'ni asl kodda "ishlayotgandek" ko'ringan narsa illyuziya edi.
Bu yomon xabar emas — bu **haqiqat**, va uni bilish yaxshi.
