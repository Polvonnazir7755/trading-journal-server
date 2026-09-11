# "Chiziq chizilishi bilan darhol kirish" — tahlil va test

Foydalanuvchi kuzatuvi: *"2 ta yashil yoki 2 ta qizil zona chizilgan zahoti
savdoga kirilsa, 8 tadan 1 tasi o'xshamagan, qolgani barchasi o'xshagan"*

---

## Bu rejim kodda ALLAQACHON BOR

`Settings -> KIRISH NUQTASI -> Kirish usuli -> "1-Majburiy sham"`

```pine
if entryMode == "1-Majburiy sham"
    mEntry := bar_index == mBreakBar    // neckline yorilgan barning O'ZIDA
    mPx := close                        // yopilish narxida
```

Yangi kod yozish shart emas. Kalitni almashtirib backtest qilsangiz —
haqiqiy javob 30 soniyada chiqadi.

---

## Lekin avval geometriyaga qarang

Fibonachi darajalarida (`mRange` = 1R birlik):

```
fib 0.000  = M cho'qqisi          <- SL shu yerda (+2% bufer)
fib 0.500  = OTE yuqori
fib 0.618  = OTE quyi             <- OTE kirish
fib 1.000  = neckline yorgan sham <- DARHOL kirish
fib 1.618  = TP1
```

| | Darhol (fib 1.0) | OTE kutib (fib 0.618) |
|---|---|---|
| Entry | 1.000 | 0.618 |
| SL masofa | **1.020R** | 0.638R |
| TP masofa | **0.618R** | 1.000R |
| **RR** | **1 : 0.606** | **1 : 1.567** |
| **Breakeven WR** | **62.3%** | **38.9%** |

### Muhim nuqta

Darhol kirishda **SL TP dan 1.65 barobar UZOQ**.

Sababi: SL har doim cho'qqida (fib 0), TP har doim 1.618 da.
Kech kirsangiz — SL uzoqlashadi, TP yaqinlashadi. Ikkalasi ham yomonlashadi.

---

## 8 ta kuzatuv nimani isbotlaydi?

**Deyarli hech narsani.** Hisob:

| Haqiqiy WR | 8 tadan 7+ yutuq chiqishi ehtimoli |
|---|---|
| 62.3% (breakeven) | **13.3%** |
| 55% | 6.3% |
| 50% (tanga) | 3.5% |

7/8 natija **edge umuman yo'q bo'lganda ham har 8 urinishdan bittasida**
uchraydi. Bu dalil emas — shovqin.

95% CI: **52.9% – 97.8%** (kenglik 44.8 pp).
Pastki chegara 52.9% — breakeven 62.3% dan **PAST**.

Ya'ni bu 8 ta savdo strategiya foyda berishini **isbotlamaydi**.

---

## Ko'rish xatosi (eng muhim qism)

Siz grafikda ko'rasiz: *narx TP tomon ketdi*.

Ko'rmaysiz: **narx TP ga yetishdan oldin SL ga tegdimi?**

```
Darhol kirish:  SL = 1.020R   TP = 0.618R
```

Narx "to'g'ri" tomonga ketayotgan bo'lsa ham, avval SL tomon 1R chayqalishi
mumkin — va savdo yopiladi. Grafikda esa keyin narx TP ga yetgani ko'rinadi.

Bu **retrospektiv xato**. Faqat backtest to'g'ri javob beradi, chunki u
har barning ichida SL/TP dan qaysi biri birinchi urilganini biladi.

---

## Expectancy taqqoslash

| WR | Darhol (RR 0.606) | OTE (RR 1.567) |
|---|---|---|
| 50% | **−0.197R** | +0.284R |
| 55% | **−0.117R** | +0.412R |
| **59.18%** (o'lchangan) | **−0.036R** | **+0.540R** |
| 62.3% | 0.000R | +0.599R |
| 70% | +0.124R | +0.797R |
| 80% | +0.285R | +1.054R |
| 87.5% | +0.405R | +1.246R |

**Diqqat:** hatto WR 87.5% bo'lganda ham darhol kirish (+0.405R)
OTE dan (+1.246R) **3 barobar yomon**.

Darhol kirish OTE ni yengishi uchun WR **97%+** bo'lishi kerak —
bu real emas.

---

## Nega OTE ustun (mantiq)

Ikkala usul bir xil setupdan kelib chiqadi va bir xil TP ga boradi.
Farq faqat **kirish narxida**.

- OTE: yaxshiroq narx, lekin ~55% hollarda narx qaytmaydi (savdo yo'q)
- Darhol: har setupda savdo, lekin yomonroq narx

Savol: **kamroq savdo yaxshi narx bilanmi, ko'proq savdo yomon narx bilanmi?**

O'lchangan javob: OTE expectancy +0.59R. Darhol kirish uchun bu darajaga
yetish uchun WR 74% kerak. Backtestda OTE WR 59.18% — darhol kirish
WR undan 15 pp yuqori bo'lishi uchun sabab yo'q.

---

## TEST QILING (aniq qadamlar)

Men "bo'lmaydi" demayman. Raqam aytadi.

### 1-test: darhol kirish
```
Settings -> KIRISH NUQTASI -> Kirish usuli = "1-Majburiy sham"
Sana: Jan 2 2026 – Sep 11 2026
Balans 1K, risk 2%, xarajat ON
```

### 2-test: neckline retest (o'rta variant)
```
Kirish usuli = "2-Neckline retest"
```
Bu fib 1.0 ga qaytishni kutadi — darhol va OTE orasidagi variant.

### Solishtirish jadvali

| Usul | Savdolar | WR | PF | Expectancy | Max DD |
|---|---|---|---|---|---|
| 4-OTE 0.5-0.618 | 49 | 59.18% | **2.302** | +0.59R | 5.90% |
| 1-Majburiy sham | ? | ? | ? | ? | ? |
| 2-Neckline retest | ? | ? | ? | ? | ? |

### Qaror mezoni

```
Agar darhol kirish PF > 2.302  ->  o'tamiz (kuzatuvingiz to'g'ri edi)
Agar PF < 2.302                ->  OTE da qolamiz
```

**Muhim:** bitta test = bitta gipoteza. Natijani ko'rib "unda 3-usulni
ham sinaymiz" deb ketaversak — ko'p test muammosi (Bonferroni) kuchayadi.
Hozirgacha 26 ta test qilganmiz.

---

## Mening bashoratim (yozib qo'yaman, keyin tekshiramiz)

```
1-Majburiy sham:
  Savdolar:   ~73  (har setup savdoga aylanadi)
  Win rate:   58-64%
  PF:         1.0-1.4
  Expectancy: -0.05R dan +0.10R gacha
```

Sababi: WR biroz oshadi (yaqinroq TP), lekin RR 0.606 gacha tushadi.
Ikkinchi ta'sir birinchisidan kuchli.

**Agar adashsam — ochiq tan olaman va OTE dan voz kechamiz.**

---

## Terminal haqida

*"terminaldagi savdolar o'zgarmagandek tuyilyabdi"*

To'g'ri — Exness demo hisobingizda **hali 0 ta savdo**. Backtest o'zgardi,
demo emas. Ikkalasi alohida narsa:

| | Backtest | Demo |
|---|---|---|
| Savdolar | 49 | **0** |
| Manba | tarixiy ma'lumot | real vaqt |
| Maqsad | strategiyani tekshirish | backtestni tasdiqlash |

Demo savdolar faqat siz limit order qo'yganingizda va narx unga
tekkanda paydo bo'ladi.
