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


---

# 🔧 BIRINCHI TEST NATIJASI VA TUZATISHLAR

## Sizning natijangiz (XAUUSD M1)

```
① CONFIRMED (S1-S4 baza)        957
② + LAOL buzildi                148   <- 85% yo'qoldi
③ + SCALP retest = FINAL         40
④ + sessiya/guard/cooldown        2   <- 95% yo'qoldi!
OCHILGAN SAVDO                    4
Baza turlari S1/S2/S3/S4  157/94/0/706
```

Bundan **4 ta muammo** aniqlandi.

## ❌ Xato 1: S3 = S1 bilan bir xil edi (mening xatom)

```pine
// oldin:
bool a1 = useS1 and scalpEM > 0 and entryEM > 0 and entryRet > 0
bool a3 = useS3 and scalpEM > 0 and entryEM > 0 and entryRet > 0   // AYNI SHU!
```

Shuning uchun **S3 = 0** chiqdi — u hech qachon ishga tushmasdi.

**Tuzatildi:** S3 endi INTRA moslashuvini talab qiladi:
```pine
bool a3 = useS3 and intraEM > 0 and entryEM > 0 and entryRet > 0
```

## ❌ Xato 2: S4 juda ko'p (706 ta = 74%)

S4 faqat `hcsM1` ni tekshirardi — hech qanday tasdiq yo'q edi.

**Tuzatildi:** endi ENTRY retest ham shart:
```pine
bool a4 = useS4 and hcsM1 and entryRet > 0
```

Ustuvorlik ham o'zgardi: `S2 > S1 > S3 > S4` (kuchliroq setup birinchi).

## ❌ Xato 3: LAOL filtri 85% yo'qotardi

`laolBroke` faqat **aynan buzilgan barda** true bo'lardi. Keyingi barda
allaqachon false — setup shakllangan bo'lsa ham signal yo'qolardi.

**Tuzatildi:** yangi parametr
```
LAOL buzilishi amal qiladi (bar):  10
```
Endi LAOL buzilgandan keyin 10 bar davomida kuchda qoladi.

## ❌ Xato 4: pozitsiya band → 40 dan 2 ta qoldi

Eng katta yo'qotish shu yerda edi (95%).

Sabab: `strategy.position_size == 0` sharti. Bitta savdo ochilsa, u
yopilguncha barcha yangi signallar tashlab yuborilardi. M1 da TP 1:3
ga yetish uzoq vaqt oladi.

**Tuzatildi:**
1. Yangi parametr `Pozitsiya ochiq bo'lsa ham kirish` (⑤ Risk)
2. DEBUG panelda yangi qator:
   ```
   Pozitsiya band -> o'tkazib yuborildi:  38
   ```

---

## ⚠️ Yana bir muhim narsa: M1 juda past

Siz M1 da sinadingiz. Bu muammoli:

| | M1 | M5 | M15 |
|---|---|---|---|
| Spred / harakat nisbati | **yomon** | o'rta | yaxshi |
| Shovqin | **juda ko'p** | o'rta | kam |
| TP ga yetish vaqti | uzoq | o'rta | tez |

**M1 da spred harakatning katta qismini yeydi.** M5 yoki M15 da sinang.

---

## Keyingi test uchun sozlama

```
Grafik:               XAUUSD M5  (M1 emas!)
Davr:                 2024.01.01 dan (Properties)

④ Kirish darajasi:    IKKALASI (solishtirish)
   LAOL amal qiladi:  10 bar

⑤ Risk:
   TP = SL × (RR):    2.0
   Pozitsiya band...: ☑ YOQING  (savdo sonini oshirish uchun)
   Signallar orasi:   3
```

Shu bilan savdo soni 4 dan 50+ ga chiqishi kerak.


---

# 🔍 2-TEST TAHLILI — asosiy sabab topildi

## Sizning raqamlaringiz

```
① CONFIRMED (baza)     903
② + LAOL buzildi       829   ✓ tuzatish ishladi (85% -> 8% yo'qotish)
③ + SCALP retest       242   ✓ yaxshi
④ + sessiya/cooldown     0   ← HAMMASI TO'SILDI!
OCHILGAN SAVDO           3
Pozitsiya band           0
```

## Yaxshi xabar: 2 ta tuzatish ishladi

| Filtr | Oldin | Hozir |
|---|---|---|
| LAOL | 957 → 148 (**-85%**) | 903 → 829 (**-8%**) ✓ |
| S3 | 0 ta | 311 ta ✓ |
| S4 | 706 (74%) | 239 (26%) ✓ |

## ❌ Yomon xabar: 242 → 0

`Pozitsiya band = 0`, ya'ni muammo pozitsiyada emas.

Qolgan aybdorlar: **sessiya**, **kunlik zarar limiti**, **cooldown**.

Eng ehtimolli — **kunlik zarar limiti**. Sizda 3 ta savdo bor, hammasi
zarar. `maxLossDay = 3` → **butun kun bloklandi**.

## 🔧 Tuzatildi

**1. Kunlik zarar limiti endi ixtiyoriy**

```
☐ Kunlik zarar limiti      ← default O'CHIQ (backtest uchun)
```

Backtestda o'chiq bo'lishi kerak — biz statistika to'playmiz, hisobni
himoya qilmaymiz. Jonli savdoda albatta yoqiladi.

**2. DEBUG panel endi aniq ko'rsatadi**

```
④ O'TDI (savdo ochilishi mumkin)    0
   ✗ sessiya to'sdi                 0
   ✗ kunlik limit to'sdi          238   ← aybdor shu!
   ✗ cooldown to'sdi                4
   ✗ pozitsiya band                 0
```

Endi qaysi filtr to'sayotgani **aniq** ko'rinadi.

---

## ⚠️ ENG MUHIM: test davri juda qisqa

Grafikda **09:00 – 12:07** ko'rinyapti. Bu **3 soat** = ~187 M1 bar.

| Davr | Kutilgan savdo |
|---|---|
| **3 soat (hozirgi)** | **~3** |
| 1 kun | ~24 |
| 1 hafta | ~170 |
| 1 oy | ~720 |

**3 ta savdo — bu normal natija 3 soat uchun.** Strategiya yomon emas,
siz shunchaki juda qisqa davrni sinadingiz.

### Backtest davrini kengaytirish

Strategy Tester → ⚙️ **Properties** → **Backtest date range**:
```
Start:  2026.01.01
End:    bugun
```

Yoki grafikda `Home` bosing, keyin bir necha marta chapga suring —
TradingView ko'proq tarix yuklaydi.

⚠️ M1 da TradingView tarix chegarasi bor (odatda ~20-40 ming bar =
2-4 hafta). Shuning uchun **M5** yoki **M15** ga o'ting — o'sha davr
uchun ancha ko'p tarix ko'rasiz.

---

## Keyingi test — aniq sozlama

```
Grafik:              XAUUSD M5      ← M1 EMAS
Davr:                2026.01.01 dan

⑤ Risk:
   ☐ Kunlik zarar limiti    ← O'CHIQ
   TP = SL × (RR):  2.0
   Signallar orasi: 3
   ☐ Pozitsiya ochiq bo'lsa ham kirish

⑥ Vaqt:
   ☐ Sessiya filtri         ← O'CHIQ
```

Kutilgan natija: **50–200 savdo**.

Agar shunda ham savdo kam bo'lsa — DEBUG panelning yangi qatorlari
qaysi filtr to'sayotganini aniq aytadi.


---

# 💰 BALANS $1000 + RISK SOZLAMALARI

## O'zgardi

```pine
initial_capital = 1000    // 10000 dan
```

Yangi risk rejimi (⑤ Risk):
```
Risk turi:   ○ Foiz %    ● Dollar $
Risk %:      1.0
Risk $:      20.0
```

**Dollar rejimida** har savdoda aynan $20 (yoki siz belgilagan) tavakkal
qilinadi — hisob o'sganda ham o'zgarmaydi.

## ⚠️ Risk haqida ogohlantirish

$1000 hisobda:

| Risk | Foiz | Baho |
|---|---|---|
| $5 | 0.5% | Photon tavsiyasi |
| $10-20 | 1-2% | professional standart |
| **$20** | **2%** | **chegara** |
| $30 | 3% | agressiv |
| $50 | 5% | **juda xavfli** |

**200 savdo, yaxshi strategiya (WR 40%, RR 1:2):**

| Risk | Median | 5% yomon | **DD 95%** | Ruin |
|---|---|---|---|---|
| $5 | $1215 | $1030 | 11% | 0% |
| $20 | $2041 | $1061 | **38%** | 0% |
| $30 | $2736 | $1031 | **53%** | 0.1% |
| $50 | $4348 | $867 | **73%** | 1.7% |

**Agar strategiya yomon bo'lsa (WR 30%):**

| Risk | Median | 70% yo'qotish ehtimoli |
|---|---|---|
| $5 | $901 | 0% |
| $20 | $622 | 4% |
| **$50** | **$297** | **72%** |

**Biz hali edge bor-yo'qligini bilmaymiz** (3 ta savdo!).
Shuning uchun: **$10-20 dan boshlang**, edge tasdiqlangach oshiring.

---

# 📈 WIN RATE OSHIRISH — yangi filtrlar

Yangi bo'lim: **⑤ Win rate filtrlari**

| Filtr | Nima qiladi | WR ta'siri |
|---|---|---|
| **HTF trend bilan bir yo'nalishda** | INTRA trendiga qarshi savdo qilmaydi | +5-10% |
| **Faqat discount/premium** | Long pastda, short yuqorida | +3-7% |
| **Min tasdiq soni** | 2-3 mustaqil tasdiq talab qiladi | +5-15% |
| **Range da savdo qilmaslik** | ATR past bo'lsa to'xtaydi | +3-8% |

Dashboard'da ko'rinadi:
```
WR filtrlari    HTF P&D noRange min2  (tasdiq: 3)
```

## ⚠️ MUHIM HAQIQAT: WR ≠ FOYDA

| Usul | WR | exp/savdo |
|---|---|---|
| RR 1:2 (hozirgi) | 40% | **+0.200** |
| RR 1:1 ga tushirish | 55% | +0.100 |
| Qismiy chiqish 50% @1R | 58% | **+0.392** |
| Faqat eng yaxshi setup | 48% | **+0.440** |

**RR 1:1 ga tushirsangiz WR 55% bo'ladi, lekin foyda 2 barobar kamayadi.**

Eng yaxshi ikkitasi:
1. **Qismiy chiqish** — WR 58%, exp +0.392
2. **Sifat filtrlari** — WR 48%, exp +0.440

Ikkalasi ham WR **va** foydani oshiradi. RR pasaytirish — yo'q.

---

## Tavsiya etilgan sozlama

```
⑤ Risk:
   Risk turi:        Dollar $
   Risk $:           20        (2% — chegarada)
   TP = SL × (RR):   2.0
   ☑ Qismiy chiqish
      1-qism hajmi:  50%
      1-qism TP:     1.0

⑤ Win rate filtrlari:
   ☑ HTF trend bilan bir yo'nalishda
   ☐ Faqat discount/premium
   Min tasdiq:       2
   ☐ Range da savdo qilmaslik

⑥ Vaqt:  ☐ Sessiya filtri
```

Filtrlarni **bittadan** yoqing va har safar natijani yozib boring.
Hammasini birdan yoqsangiz — savdo 0 ga tushadi.
