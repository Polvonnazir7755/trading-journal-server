# 1.618 LEGENDA — W/M pattern + Fibonachi kengaytmasi

**Manba:** TIGERS TRADING (MUSLIM ALI) YouTube efiri, 11.01.2026
https://www.youtube.com/watch?v=G9HxpUnBAGY (1:16:58, 8792 ko'rish)

---

## Video qoidalari (aynan ko'chirilgan)

1. **Faqat razvorot** (trend burilishi) holatida
2. **W pattern** (long): downtrend → 2 ta minimum → neckline
   **M pattern** (short): uptrend → 2 ta maksimum → neckline
3. **Neckline TANA bilan yorilishi shart** — soya bilan emas
4. **Fibonachi:** yorgan shamning **tanasidan** → **oxirgi minimumgacha**
5. **6 ta kirish nuqtasi:**
   | № | Nuqta |
   |---|---|
   | 1 | Yorib yopilgan sham ("majburiy") |
   | 2 | Neckline ustiga retest |
   | 3 | Trend chizig'i retest |
   | 4 | **OTE 0.5–0.618** ("optimalniy trade zone") |
   | 5 | Imbalans (FVG) |
   | 6 | Order block |
6. **TP1 = 1.618** ("garant") — 70% yopiladi
   **TP2 = 2.618** ("prognoz") — qolgan 30%, SL breakevenga

---

## Matematik tahlil (kodni yozishdan oldin hisoblangan)

W ning bo'yi = 1.0 birlik, SL minimumdan 2% pastda:

| Kirish nuqtasi | Kirish | RR (TP1) | BE win rate | RR (TP2) | BE WR |
|---|---|---|---|---|---|
| **1-Majburiy sham** | 1.000 | **0.61** | **62.3%** | 1.59 | 38.7% |
| 2-Neckline retest | 1.000 | 0.61 | 62.3% | 1.59 | 38.7% |
| 6-Order block | ~0.75 | 1.13 | 47.0% | 2.43 | 29.2% |
| 5-Imbalans | ~0.70 | 1.28 | 44.0% | 2.66 | 27.3% |
| 4-OTE 0.618 | 0.618 | 1.57 | 38.9% | 3.13 | 24.2% |
| **4-OTE 0.5** | 0.500 | **2.15** | **31.7%** | **4.07** | **19.7%** |

### 70/30 qismli chiqish bilan expectancy

| Kirish | TP1 yetish 30% | 40% | 50% | 60% |
|---|---|---|---|---|
| **OTE 0.5** | −0.10R | **+0.20R** | **+0.50R** | **+0.80R** |
| OTE 0.618 | −0.26R | −0.01R | +0.24R | +0.48R |
| Imbalans 0.7 | −0.34R | −0.12R | +0.11R | +0.33R |
| **Majburiy sham** | −0.52R | −0.35R | **−0.19R** | **−0.03R** |

**Bashorat:** OTE 0.5–0.618 eng yaxshi, "majburiy sham" hatto 60% WR bilan ham zarar.

### "Garant 1.618" da'vosi

Video: *"garantit degani bu aynan shu zonaga bormasdan qo'ymaydi degani"*

Bu **matematik jihatdan imkonsiz**. Agar 100% bo'lsa, SL hech qachon urilmaydi.

Random walk (tasodifiy narx) da:
- OTE 0.5 dan **1.618 ga yetish: 31.7%**
- **2.618 ga yetish: 19.7%**

Strategiya foyda berishi uchun haqiqiy ehtimol 31.7% dan yuqori bo'lishi kerak.

**Kod aynan shuni o'lchaydi** — dashboardda "TP1 1.618 'GARANT'" qatori.

---

## Kod nima qiladi

`FIB1618_STRATEGY.pine` — video qoidalarini aynan bajaradi, lekin **o'lchov qo'shadi**:

| Dashboard qatori | Nima ko'rsatadi |
|---|---|
| W / M topildi | Nechta pattern aniqlandi |
| Savdo ochildi | Nechtasi savdoga aylandi (% patterndan) |
| **TP1 1.618 'GARANT'** | **Nechtasi 1.618 ga yetdi — "garant" ning haqiqiy foizi** |
| TP2 2.618 'prognoz' | Nechtasi 2.618 ga yetdi |
| Win rate, PF, Recovery, Expectancy | Standart o'lchovlar |

---

## Qanday sinash — TEST REJASI

### Sozlamalar (hamma testda bir xil)
```
Symbol:     XAUUSD
TF:         M15 (videoda shu ishlatilgan) — keyin M3/M5 ni ham sinang
Risk:       $20 (yoki 1%)
Pivot:      5
Razvorot:   YOQ
Tana bilan: YOQ
```

### TEST A — 6 ta kirish nuqtasini solishtirish

**Faqat "Kirish usuli" ni o'zgartiring**, qolgani bir xil:

| Kirish usuli | W/M topildi | Savdo | **TP1 %** | TP2 % | WR | Net | Max DD | PF | Recovery | Exp (R) |
|---|---|---|---|---|---|---|---|---|---|---|
| 1-Majburiy sham | | | | | | | | | | |
| 2-Neckline retest | | | | | | | | | | |
| 4-OTE 0.5-0.618 | | | | | | | | | | |
| 5-Imbalans (FVG) | | | | | | | | | | |
| 6-Order block | | | | | | | | | | |

**Kutilayotgan natija (mening hisobim):** OTE eng yaxshi, majburiy sham eng yomon.
Agar teskari chiqsa — mening modelim xato, sabab qidiramiz.

### TEST B — "Garant" tekshiruvi

TEST A dagi eng yaxshi kirish usulini oling. **TP1 % qatoriga qarang.**

| Natija | Xulosa |
|---|---|
| 99–100% | Video haq, "garant" haqiqat (kutilmagan) |
| 60–80% | Kuchli edge bor, lekin garant emas |
| 35–50% | Normal strategiya, foydali bo'lishi mumkin |
| ~32% | Random walk darajasi — **edge yo'q** |
| <32% | Tasodifdan yomon |

### TEST C — Out-of-sample

Eng yaxshi sozlamani **boshqa davrda** sinang (Sana oralig'i guruhi orqali).

| Davr | Savdo | TP1 % | Net | PF | Recovery |
|---|---|---|---|---|---|
| In-sample (tanlov qilingan) | | | | | |
| Out-of-sample | | | | | |

---

## Qabul mezonlari

| Ko'rsatkich | Minimal | Yaxshi |
|---|---|---|
| Savdolar soni | 30+ | 100+ |
| Profit factor | 1.2 | 1.5+ |
| Recovery factor | 1.5 | 2.0+ |
| Expectancy | +0.1R | +0.3R |
| Out-of-sample PF | >1.1 | >1.3 |

**Agar OTE rejimida 50+ savdoda PF < 1.1 bo'lsa** — strategiya ishlamaydi.

---

## Kodning cheklovlari (halol ro'yxat)

1. **3-kirish nuqtasi (trend chizig'i retest) qo'shilmagan** — trend chizig'ini avtomatik chizish sub'ektiv, aniq qoida yo'q
2. **Imbalans va Order block soddalashtirilgan** — video ularni aniq ta'riflamagan:
   - Imbalans = 1-sham maksimum soyasi ↔ 3-sham minimum soyasi orasi (FVG)
   - Order block = yorishdan oldingi oxirgi qarama-qarshi shamning tanasi
3. **Pivot 5 bar kechikish beradi** — real vaqtda pattern 5 bar keyin tasdiqlanadi (look-ahead yo'q, lekin kechikish bor)
4. **W ning "ikki oyog'i tengligi" 25% tolerantlik bilan** — video aniq raqam bermagan
5. **Razvorot sharti sodda** — 30 bar oldingi narx bilan solishtirish

Bu cheklovlar natijani **pasaytiradi**, oshirmaydi. Ya'ni agar kod foyda ko'rsatsa, haqiqiy strategiya undan yaxshiroq bo'lishi mumkin.

---

## Videoning zaif tomonlari (tanqid)

| Muammo | Izoh |
|---|---|
| "Garant" — yolg'on | Kafolat yo'q, faqat ehtimollik |
| 6 ta kirish nuqtasi | 6 ta erkinlik darajasi = orqaga qarab har doim to'g'ri ko'rinadi |
| Statistika yo'q | 77 daqiqada bironta raqam aytilmagan |
| Faqat ishlagan misollar | Tanlangan namuna (cherry-picking) |
| SL aniq emas | "kichikroq TF ga o'tib qisqartirish mumkin" — noaniq |
| Kurs sotiladi | Video davomida "professional kursimizga kelsangiz" |

**Ijobiy:** matematikasi ichki ziddiyatsiz, grid/martingale emas, OTE mantiqiy.
