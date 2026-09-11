# 2% vs 5% risk — Monte-Carlo tahlili

Savol: "$1000 balans, 5% risk qilsak bo'lmaydimi?"
Javob raqamlar bilan. Har jadval 60,000–200,000 simulyatsiya.

Kirish parametrlari: RR = 1:1.58 (fib 1.618, o'lchangan), compounding (har savdo joriy balansdan).

---

## 1. Agar backtest WR (72.7%) HAQIQAT bo'lsa — 100 savdo

| Risk | Median foyda | 5% (yomon holat) | Median DD | DD 95% | P(DD>20%) |
|---|---|---|---|---|---|
| 1% | +139% | +95% | 3.0% | 5.2% | 0.0% |
| **2%** | **+462%** | **+273%** | **5.9%** | **10.4%** | **0.0%** |
| 3% | +1,191% | +599% | 8.7% | 15.3% | 0.5% |
| **5%** | **+6,343%** | **+2,227%** | **14.3%** | **24.6%** | **15.2%** |
| 8% | +62,393% | +12,276% | 22.1% | 35.7% | 78.8% |
| 10% | +260,079% | +34,537% | 27.1% | 44.6% | 83.5% |

Bu jadvalga qarab "5% zo'r ekan" degan xulosa chiqadi. **Bu xato** — chunki 72.7% WR n=33 dan olingan va 95% CI = 57.5%–87.9%.

---

## 2. Agar edge zaifroq bo'lsa (WR 60%) — 100 savdo

| Risk | Median | 5% (yomon) | Median DD | DD 95% | P(DD>20%) |
|---|---|---|---|---|---|
| 2% | +188% | +91% | 9.6% | 15.7% | 0.7% |
| 3% | +376% | +158% | 14.1% | 22.8% | 11.3% |
| **5%** | +1,131% | +345% | **22.6%** | **35.5%** | **64.5%** |
| 8% | +4,399% | +791% | 34.1% | 51.7% | 98.9% |

5% da: **DD 20% dan oshishi ehtimoli 64.5%**, 2% da atigi 0.7%. **92 barobar farq.**

---

## 3. Agar edge YO'Q bo'lsa (WR 38.8% = breakeven) — 100 savdo

| Risk | Median natija | Median DD | DD 95% |
|---|---|---|---|
| 2% | −1.9% | 24.3% | 42.5% |
| **5%** | **−15.1%** | **52.6%** | **76.8%** |
| 10% | −50.6% | 81.3% | 95.9% |

Bayes tahlilida **P(edge yo'q) = 15%**. Ya'ni bu ustunga tushish ehtimoli 1/7.
5% risk bilan bu holatda balansning **yarmi yo'qoladi** (median DD 52.6%).

---

## 4. ENG MUHIM JADVAL — edge NOANIQ (Bayes aralashmasi)

Stsenariylar: 15% edge yo'q (WR 38.8) / 35% zaif (55) / 35% o'rta (65) / 15% kuchli (72.7).
O'rtacha WR = 58.7%. **Bu bizning haqiqiy bilim holatimiz.**

### 30 savdo (demo bosqichi)

| Risk | 5% (yomon holat) | Median | Median DD | DD 95% | P(DD>30%) | P(zarar) |
|---|---|---|---|---|---|---|
| 1% | −4.3% | +17.5% | 3.0% | 8.6% | 0.0% | 8.4% |
| **2%** | **−8.9%** | **+37.4%** | **5.9%** | **16.6%** | **0.2%** | 8.6% |
| 3% | −13.6% | +59.7% | 8.7% | 24.0% | 2.0% | 8.4% |
| **5%** | **−23.3%** | +112.4% | **14.4%** | **37.4%** | **12.0%** | 12.2% |
| 10% | −47.3% | +296.0% | 28.7% | 64.5% | 49.5% | 12.5% |

### 100 savdo

| Risk | 5% (yomon holat) | Median | Median DD | DD 95% | P(DD>30%) |
|---|---|---|---|---|---|
| **2%** | **−11.5%** | +188% | 9.6% | 28.9% | **4.5%** |
| 3% | −18.6% | +376% | 14.1% | 40.8% | 10.7% |
| **5%** | **−34.2%** | +1,131% | 22.6% | 59.7% | **28.9%** |
| 8% | −57.2% | +4,399% | 34.1% | 79.0% | 61.6% |

---

## 5% ning aniq zarari — uch nuqta

### a) Yomon holat 3 barobar chuqurlashadi
100 savdo, edge noaniq:
```
2% risk -> eng yomon 5% holat: -11.5%   ($885 qoladi)
5% risk -> eng yomon 5% holat: -34.2%   ($658 qoladi)
```

### b) Ketma-ket zararlar
100 savdoda maksimal zarar seriyasi (simulyatsiya):

| WR | Median | 95% | 99% |
|---|---|---|---|
| 72.7% | 3 | 5 | 6 |
| 60% | 4 | 7 | 9 |
| 50% | 6 | 9 | 12 |

Nima bo'ladi:

| Ketma-ket zarar | 2% risk | 5% risk |
|---|---|---|
| 4 | −7.8% ($922) | −18.5% ($815) |
| 6 | −11.4% ($886) | −26.5% ($735) |
| 8 | −14.9% ($851) | **−33.7% ($663)** |
| 10 | −18.3% ($817) | **−40.1% ($599)** |

**Tiklanish assimetriyasi:** 5% risk bilan 8 ta zarardan keyin balansni qaytarish uchun **+50.7%** kerak, 2% da atigi **+17.5%**.

WR 60% bo'lsa 7 ta ketma-ket zarar 100 savdoda **20% ehtimol bilan** kutiladi. Bu kamdan-kam emas, **normal**.

### c) Kelly mezoni — 5% qayerda turadi

```
Kelly = (p×b − q)/b,  b = 1.58

WR 72.7% (backtest)  -> Kelly 55.4%   1/4 Kelly = 13.9%
WR 60%   (CI pastki) -> Kelly 34.7%   1/4 Kelly =  8.7%
WR 57.5% (CI 95%)    -> Kelly 30.6%   1/4 Kelly =  7.7%
WR 50%   (pessimist) -> Kelly 18.4%   1/4 Kelly =  4.6%
```

Kelly bo'yicha 5% **haddan tashqari emas** — hatto eng pessimistik holatda ham 1/4 Kelly = 4.6%.

**LEKIN Kelly ikkita shartni talab qiladi:**
1. `p` **aniq ma'lum** bo'lishi kerak. Bizda n=33, CI kengligi 30 foiz punkt.
2. Cheksiz ko'p savdo. Bizda 0 ta demo savdo.

Kelly `p` ni ortiqcha baholaganda **kvadratik jazolaydi**. WR ni 72.7% deb o'ylab 5% qo'ysangiz, aslida 55% bo'lib chiqsa — sizning haqiqiy risk darajangiz optimaldan 2 barobar yuqori.

---

## Asosiy sabab: hozir 0 ta demo savdo bor

| | Backtest | Demo |
|---|---|---|
| Savdolar | 33 | **0** |
| WR | 72.73% | noma'lum |
| PF | 4.506 | noma'lum |

Backtest — **o'tmish ma'lumotida optimallashtirilgan** natija. Pivot barqarorsizligi (PF 1.6→4.0→4.2→1.4) overfitting borligini ko'rsatadi.

**5% risk faqat bitta narsani sotib oladi: tezlik. To'lovi — noaniqlik davrida chuqur DD.**

---

## Tavsiya — bosqichli

| Bosqich | Shart | Risk |
|---|---|---|
| 1 | Hozir → 30 demo savdo | **2%** |
| 2 | 30 savdo, PF > 1.5 | **3%** |
| 3 | 60 savdo, PF > 1.8 | **5%** |
| 4 | 100 savdo, PF > 2.0, DD < 15% | 5% + real pul |

Har bosqichda WR CI torayadi:

| n | 95% CI kengligi (WR 65% da) |
|---|---|
| 33 | ±16.3 pp |
| 60 | ±12.1 pp |
| 100 | ±9.3 pp |

**n=100 da WR ni ±9 pp aniqlikda bilamiz** — o'shanda 5% asosli bo'ladi.

---

## Agar baribir 5% qilsangiz

Bu sizning pulingiz va sizning qaroringiz. Men "yo'q" demayman — faqat raqamni ko'rsataman.

Shart qo'yaman: **to'xtatish qoidasi**.

```
DD 20% ga yetsa (balans $800)  -> risk 2% ga tushiriladi
DD 30% ga yetsa (balans $700)  -> savdo TO'XTATILADI, tahlil qilinadi
```

5% risk bilan 100 savdoda DD>30% ehtimoli **28.9%**. Ya'ni har 3-4 urinishdan bittasi to'xtatish nuqtasiga boradi.

Demo hisobda bu faqat raqam. Real pulda bu $300.
