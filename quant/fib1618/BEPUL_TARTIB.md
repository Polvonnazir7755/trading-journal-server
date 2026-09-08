# BEPUL REJIMDA DEMO — kunlik tartib

**Qaror:** obuna olinmaydi. Sabab — matematik:
$500 depozitda 4 oylik kutilgan foyda ~$35, Essential obunasi $52.
Kutilgan sof natija **−$10**. Obuna $600+ depozitda oqlanadi.

---

## ASOSIY DALIL: alert shart emas

```
Kirish oynasi = 30 bar (M30) = 15 SOAT
```

Setup paydo bo'lgach **15 soat** vaqt bor. Ya'ni kuniga ikki marta
tekshirsangiz (12 soat oraliq), **birorta setup o'tkazib yuborilmaydi**.

| Tekshirish | Oraliq | Qamrov | O'tkazib yuborish |
|---|---|---|---|
| Kuniga 1 marta | 24 soat | 62% | **38%** ❌ |
| **Kuniga 2 marta** | **12 soat** | **100%** | **0%** ✅ |
| Kuniga 3 marta | 8 soat | 100% | 0% |

---

## KUNLIK JADVAL (Toshkent, UTC+5)

| Vaqt | Nima bo'layapti | Nima qilasiz |
|---|---|---|
| **07:00** | Osiyo tugayapti | tungi setuplarni ko'rish, limit order |
| 13:00 | London ochiq (ixtiyoriy) | yangi setup bormi |
| **19:00** | NY o'rtasi | order ishladimi, jurnalga yozish |

**Minimal: 07:00 va 19:00** — har biri 5 daqiqa.

---

## 5 DAQIQALIK TEKSHIRUV — aniq qadamlar

### 1. Grafikni oching
TradingView → EURUSD → M30 → 1.618 LEGENDA

### 2. Setup bormi?

Grafikda **yashil** yoki **qizil ikki chiziq** ko'rinsa — OTE zonasi faol.

| Chiziq | Ma'nosi |
|---|---|
| 🟢 yashil ikki chiziq | W setup — **BUY LIMIT** |
| 🔴 qizil ikki chiziq | M setup — **SELL LIMIT** |
| chiziq yo'q | setup yo'q, yopish |

### 3. Setup bo'lsa — raqamlarni yozing

Grafikdan o'qing:
- OTE zonasining **yuqori** chegarasi (LONG uchun kirish narxi)
- 🔴 **SL** darajasi
- 🟢 **TP1** darajasi

### 4. Lot hisoblang

```
SL masofa (pip) = |kirish − SL| × 10000
lot = 10 / (SL_pip × 10)
```

| SL (pip) | Lot |
|---|---|
| 20 | 0.05 |
| 25 | 0.04 |
| 30 | 0.03 |
| 40 | 0.02 |
| 50 | 0.02 |
| 80–100 | 0.01 |

### 5. MT5 da PENDING ORDER

```
Type:    Buy Limit  (yoki Sell Limit)
Price:   OTE zonasining yuqori chegarasi
SL:      qizil daraja
TP:      yashil daraja
Expiry:  16 soat        ← MUHIM
Volume:  hisoblangan lot
```

**Expiry qo'yish shart.** Aks holda eski order osilib qoladi va
setup eskirgach ham ishlab ketishi mumkin.

### 6. Kechqurun tekshiring

- Order **ishladi** → jurnalga yozing (kirish narxi, keyin chiqish)
- Order **ishlamadi** (narx zonaga tushmadi) → jurnalga
  "o'tkazib yuborilgan" deb yozing, R ustunini bo'sh qoldiring
- Muddat tugagan orderni o'chiring

---

## JURNALDA NIMA YOZILADI

Har **setup** yoziladi, faqat savdo emas:

| Holat | R ustuni | Izoh |
|---|---|---|
| TP ga yetdi | +1.62 | "toza TP" |
| SL urildi | −1.00 | "SL, yangilik chiqdi" |
| Order ishlamadi | **bo'sh** | **"narx zonaga tushmadi"** |

Uchinchisi ham ma'lumot: backtest 46.5% setup savdoga aylanganini
ko'rsatgan edi. Real ham shundaymi — tekshiramiz.

---

## HAFTALIK RITM

**Yakshanba oqshomi** (10 daqiqa):
1. Jurnalning "Statistika" varag'ini oching
2. Uchta raqamga qarang:
   - Profit factor (yashil bo'lsa yaxshi)
   - Expectancy > +0.2R
   - Eng uzun zarar seriya — **8 ga yetsa TO'XTATING**
3. "Izoh" ustunini o'qing — takrorlanadigan naqsh bormi

---

## BEPUL REJIMNING CHEKLOVLARI — halol ro'yxat

| Cheklov | Ta'siri | Yechim |
|---|---|---|
| Texnik alert = 0 ta | xabar kelmaydi | kuniga 2 marta qo'lda |
| 5,000 bar | ~4 oy tarix | demo uchun muhim emas |
| 2 indikator/grafik | boshqasi sig'maydi | faqat 1.618 qoldiring |
| 1 grafik/tab | ko'p aktiv qiyin | 1 aktivda qolamiz |

**Hech biri demo uchun to'sqinlik qilmaydi.**

---

## QACHON OBUNA OLISH KERAK

Faqat shu shartlar bajarilsa:

| Shart | Qiymat |
|---|---|
| Demo savdolar | 30+ |
| Demo Profit factor | > 1.5 |
| Depozit | **$600+** |

O'shanda **Essential ($12.95/oy)** oling — Premium emas.
Premium $2,600 depozitda oqlanadi.

---

## ESLATMA

Bepul rejim — bu chegaralanish emas, **intizom mashqi**.

Kuniga ikki marta 5 daqiqa — bu treyding uchun **normal ritm**.
Ekranga yopishib o'tirish natijani yaxshilamaydi, aksincha
ortiqcha savdoga olib keladi.
