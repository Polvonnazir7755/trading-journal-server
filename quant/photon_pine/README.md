# Photon MTF v2

**Fayl:** `PHOTON_V2.pine`

---

## v1 dan farqi — 5 ta muhim o'zgarish

### 1. SWING va INTERNAL ajratildi ⭐

Bu eng muhim tuzatish. v1 da faza noto'g'ri hisoblanardi.

Photon'da swing va internal — bu **bir xil taymfreymda, turli fraktal
o'lchamida** aniqlanadigan struktura:

```
MTF SWING    = katta fraktal (default 5)  -> asosiy tuzilma
MTF INTERNAL = kichik fraktal (default 2) -> ichki harakat
```

Faza endi to'g'ri:
```
Pro Swing    = MTF swing bias == HTF bias
Pro Internal = MTF internal bias == MTF swing bias

A = Pro Swing + Pro Internal
B = Pro Swing + Counter Internal
C = Counter Swing + Pro Internal
D = Counter + Counter (AVOID)
```

### 2. Signal manbai kengaytirildi

v1 da faqat LTF sweep bor edi → 5 ta savdo chiqdi.

Endi 4 ta manba (④ bo'limda yoqib/o'chiriladi):

| Manba | Izoh |
|---|---|
| LTF sweep | joriy TF likvidlik olish |
| MTF sweep | MTF darajasida sweep |
| POI tap | OB/FVG zonaga tegish |
| LTF CHoCH | agressiv (default o'chiq) |

**Nega kerak:** hisoblab ko'rdim — A+B faza barcha holatlarning
atigi **~22%** ini tashkil qiladi. 50 savdo uchun ~225 ta signal kerak.

### 3. Entry / SL / TP grafikda

- Pozitsiya ochiq bo'lganda 3 ta chiziq: ko'k (entry), qizil (SL), yashil (TP)
- Kirish paytida yorliq: yo'nalish, faza, aniq narxlar

### 4. Faza bo'yicha statistika ⭐

Dashboard pastida:

```
FAZA STATISTIKASI     win/jami  WR
A  (Pro+Pro)          12/28  43%
B  (Pro+Counter)       8/22  36%
C  (Counter+Pro)          —
D  (AVOID)                —
JAMI savdo            50  ✓
```

Rang: yashil = musbat PnL, qizil = manfiy.

### 5. Default: faqat A + B

C va D o'chirilgan. Siz so'raganingizdek.

---

## Sozlash tartibi — 50 savdo yig'ish

**1-qadam: davrni kengaytiring**

Strategy Tester → Properties → Backtest date range: **2022.01.01** dan

**2-qadam: savdo sonini tekshiring**

Dashboard "JAMI savdo" qatorida ko'rinadi. 50 dan kam bo'lsa:

| Nima | Qanday |
|---|---|
| Signal manbalari | ④ da hammasini yoqing (CHoCH ham) |
| Cooldown | 5 → 2 ga tushiring |
| MTF | 60 → 30 |
| SWING fraktal | 5 → 4 |
| Sessiya | ⑦ o'chiq bo'lsin (default) |

**3-qadam: 50+ savdo bo'lgach**

Endi faza statistikasini o'qing. A va B ni solishtiring.

---

## SL rejimlari

⑥ bo'limda:

| Rejim | Qayerga qo'yadi |
|---|---|
| **Swing** | oxirgi swing low/high ortiga (default) |
| ATR | ATR × koeffitsient |
| Signal shami | joriy sham low/high |

---

## ⚠️ Ogohlantirish

Sozlamalarni "yaxshi natija" chiqquncha o'zgartirish — bu **overfitting**.

To'g'ri tartib:
1. Avval **savdo sonini** 50+ ga yetkazing (statistika uchun)
2. Keyin **hech narsani o'zgartirmasdan** natijani o'qing
3. Faza A va B ni solishtiring

Agar 20 ta sozlamani sinab, eng yaxshisini tanlasangiz — natija yolg'on
bo'ladi. Jonli savdoda takrorlanmaydi.

---

## Kutilgan natija

Halol aytaman: **A fazada win rate yaxshi chiqishi shart emas.**

Photon shunday da'vo qiladi, lekin bu **tekshirilmagan gipoteza** —
aynan shuning uchun sinaymiz.

Uch ehtimol:
- A > B → Photon nazariyasi tasdiqlanadi
- A ≈ B → faza filtri foydasiz
- A < B → nazariya teskari ishlaydi

Har uchalasi ham qimmatli ma'lumot.
