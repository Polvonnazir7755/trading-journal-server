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


---

# ⭐ IKKI KIRISH DARAJASI (siz payqagan narsa)

Siz to'g'ri payqadingiz — asl kodda **ikki xil signal** bor:

| Daraja | Shartlar | Xarakteri |
|---|---|---|
| `*_confirmed_triggered` | S1–S4 baza + M1 yopilishi | ko'p savdo, o'rtacha sifat |
| `final_entry_*` | + LAOL buzilishi<br>+ SCALP FU/SN retest<br>+ 10 bar oynasi<br>+ scalp LV mos<br>+ HCS | kam savdo, yuqori sifat |

Birinchi versiyamda men ularni yaxshi ajratmagan edim. **Tuzatildi.**

## Endi ④ bo'limda tanlaysiz

```
Kirish darajasi:
  ○ CONFIRMED (ko'p savdo)
  ● FINAL (sifatli)          <- default
  ○ IKKALASI (solishtirish)
```

**IKKALASI** rejimida ikkalasi ham savdo ochadi, lekin dashboard ularni
**alohida hisoblaydi**:

```
KIRISH DARAJASI    win/jami  WR  avgPnL
FINAL (sifatli)      18/47   38%   +12.4
CONFIRMED (ko'p)     41/186  22%    -2.1
Rejim              IKKALASI
```

Shunda bitta backtestdan **ikki javob** olasiz.

## ⚠️ Statistik tuzoq — buni bilish muhim

Hisoblab ko'rdim:

| Daraja | WR | Savdo/yil | exp | 1 yilda isbotlash |
|---|---|---|---|---|
| CONFIRMED | 14% | 400 | +0.26R | **34%** |
| FINAL | 20% | 60 | +0.80R | **30%** |

**FINAL yuqori sifat bersa ham, savdo kam bo'lgani uchun uni isbotlash
xuddi shunday qiyin.** Chunki statistik kuch faqat WR ga emas, **savdo
soniga** ham bog'liq.

Shuning uchun tavsiyam:
1. Avval **IKKALASI** rejimida ishga tushiring
2. FINAL filtri savdoni qanchaga kamaytirishini ko'ring (DEBUG panelda)
3. Agar FINAL 20 tadan kam savdo bersa — uni bir yilda tekshirib bo'lmaydi

## DEBUG panelda yangi qator

```
FINAL filtri qoldirdi    3%  (412 -> 12)
```

Agar 5% dan kam qolsa — qizil rangda ogohlantiradi. Bu FINAL filtri
juda qattiq degani.


---

# ⭐ TP MASOFASI TUZATILDI (siz payqagan 2-muammo)

## Muammo

Asl kodda:
```pine
const int TP_MULTIPLIER = 8    // TP = SL × 8
```

Bu **1:8 RR** degani. Hisoblab ko'rdim:

| RR | TP ga yetish ehtimoli | Kerakli WR |
|---|---|---|
| 1:2 | 33.3% | 33.3% |
| **1:3** | **25.0%** | **25.0%** |
| 1:4 | 20.0% | 20.0% |
| **1:8** | **11.1%** | **11.1%** |

**1:8 da 9 tadan 8 tasi SL ga uriladi.** Bu matematik jihatdan normal,
lekin sizning past win rate'ingizning asosiy sababi shu edi.

## Psixologik tomoni — undan ham muhim

300 savdoda ketma-ket zararlar:

| RR | Real WR | exp/savdo | Median seriya | 95% seriya |
|---|---|---|---|---|
| 1:2 | 36% | +0.090R | 11 | 16 |
| **1:3** | **28%** | **+0.120R** | **14** | **22** |
| 1:4 | 23% | +0.150R | 17 | 27 |
| 1:8 | 14% | +0.260R | **27** | **43** |

**1:8 da ketma-ket 27-43 zarar NORMAL.** Buni deyarli hech kim ko'tara olmaydi.

Expectancy o'xshash, lekin **psixologiya butunlay boshqa**.

## Nima o'zgardi

### 1. Default RR: 8 → **3**

```
TP = SL × (RR):  3.0     ← default
```

Siz aytganingizdek 1:2, 1:3, 1:4 sinash mumkin.

### 2. Qismiy chiqish (partial) qo'shildi

```
☐ Qismiy chiqish (partial)
   1-qism hajmi %:  50
   1-qism TP (RR):  1.5
```

Pozitsiyaning yarmi 1:1.5 da yopiladi, qolgani asosiy TP gacha ketadi.

**Ta'siri:** win rate sezilarli oshadi (birinchi qism tez yopiladi),
expectancy biroz tushishi mumkin. Psixologik jihatdan ancha yengil.

### 3. Breakeven ko'chirish

```
☐ Breakeven ko'chirish
   BE ga ko'chirish (RR):  1.0
```

Narx 1R ga yetsa — SL kirish narxiga ko'chadi. Zarar riski yo'qoladi.

⚠️ **Diqqat:** BE ko'chirish WR ni oshirmaydi, lekin *zarar hajmini*
kamaytiradi. Ba'zan narx BE ga tegib, keyin TP ga ketadi — bu "bekorga
chiqish". Backtest bilan tekshiring.

### 4. Dashboard'da RR diagnostikasi

```
RR / kutilgan WR    1:3  ->  25.0%
Haqiqiy WR          28.4%   ✓ edge
```

- **Kutilgan WR** = `1/(1+RR)` — adolatli bozorda
- **Haqiqiy WR** > kutilgandan bo'lsa → edge bor
- Kam bo'lsa → edge yo'q

Bu eng to'g'ridan-to'g'ri edge o'lchagichi.

## Tavsiya etilgan sozlama

```
TP = SL × (RR):        3.0
Qismiy chiqish:        ☐ (avval yoqmасdan sinang)
Breakeven:             ☐
Kirish darajasi:       IKKALASI
```

Keyin RR ni 2, 3, 4 bilan alohida sinab, qaysi biri
**expectancy × chidamlilik** bo'yicha yaxshi ekanini toping.

⚠️ Faqat "eng yuqori foyda" ni tanlamang — ketma-ket zararlar
sonini ham hisobga oling. 40 ta zarar seriyasini ko'tara olasizmi?
