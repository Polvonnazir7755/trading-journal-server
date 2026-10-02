# Namunani tezlashtirish — korrelyatsiya hisobi

Muammo: EURUSD da 30 savdo yig'ish **5.1 oy** oladi.
Yechim: boshqa juftliklar qo'shish. Lekin 4 juftlik 4 barobar ma'lumot bermaydi.

---

## 1. Nega bermaydi — korrelyatsiya

EURUSD bilan kunlik daromad korrelyatsiyasi:

| Juftlik | r | Izoh |
|---|---|---|
| USDCHF | **−0.93** | EURUSD ning oyna aksi — yangi ma'lumot ~0 |
| GBPUSD | +0.85 | deyarli bir xil |
| AUDUSD | +0.72 | |
| NZDUSD | +0.66 | AUDUSD bilan o'zaro **+0.88** |
| USDCAD | −0.62 | |
| EURJPY | +0.52 | |
| XAUUSD | +0.42 | |
| EURGBP | +0.28 | **mustaqil** |
| USDJPY | **−0.22** | **eng mustaqil** |

Ikki juftlik korrelyatsiyasi yuqori bo'lsa, ular bir vaqtda yutadi yoki
bir vaqtda yutqazadi. Statistik jihatdan bu **bitta savdo**, ikkita emas.

### Samarali namuna formulasi
```
N_eff = N_jami / (1 + (m−1) × ρ̄)
```
`m` = juftliklar soni, `ρ̄` = o'rtacha mutlaq korrelyatsiya.

---

## 2. Tanlovlarni solishtirish (har juftlikda 10 savdo)

| Tanlov | Jami | ρ̄ | **N_eff** | Samara |
|---|---|---|---|---|
| Faqat EURUSD | 10 | — | 10.0 | 100% |
| EURUSD + GBPUSD | 20 | 0.85 | **10.8** | 54% |
| EURUSD + USDJPY | 20 | 0.22 | **16.4** | 82% |
| EUR/GBP/AUD/NZD (hammasi USD-major) | 40 | 0.73 | **12.5** | **31%** |
| **EURUSD + USDJPY + EURGBP + AUDUSD** | 40 | 0.25 | **23.1** | **58%** |
| + XAUUSD o'rniga AUDUSD | 40 | 0.21 | 24.5 | 61% |
| Tarqoq 5 ta | 50 | 0.31 | 22.2 | 44% |

**Asosiy xulosa:** EURUSD+GBPUSD qo'shish 20 savdo beradi, lekin
samarali qiymati **10.8** — ya'ni qo'shimcha juftlik deyarli **behuda**.

---

## 3. Vaqt yutug'i

| Tanlov | Xom savdo/oy | N_eff/oy | **30 ga yetish** |
|---|---|---|---|
| Faqat EURUSD | 5.9 | 5.92 | **5.1 oy** |
| + GBPUSD | 11.8 | 6.40 | 4.7 oy |
| + USDJPY | 11.8 | 9.70 | 3.1 oy |
| USD-major 4 ta | 23.7 | 7.39 | 4.1 oy |
| **Tarqoq 4 ta** | 23.7 | **13.65** | **2.2 oy** |
| Tarqoq 5 ta | 29.6 | 13.12 | 2.3 oy |

**5.1 oy → 2.2 oy.** Ikki yarim barobar tez.

5 ta juftlik 4 tadan **yomonroq** — qo'shilgan USDCAD korrelyatsiyani oshiradi.

---

## 4. Spred solig'i — amaliy cheklov

| Juftlik | Spred | ATR(D) | Spred/ATR | SL 25 pip da |
|---|---|---|---|---|
| EURUSD | 1.1 | 78 | 1.41% | 4.4% |
| USDJPY | 1.3 | 74 | 1.76% | 5.2% |
| AUDUSD | 1.4 | 62 | 2.26% | 5.6% |
| **EURGBP** | 1.6 | 46 | **3.48%** | **6.4%** |

EURGBP eng qimmat — volatilligi past, spredi yuqori. Lekin
korrelyatsiyasi eng past, shuning uchun saqlanadi.

**XAUUSD qo'shilmaydi** — allaqachon sinalgan va yiqilgan:
t=2.50 (kerak 3.09), M(short) −$105 zarar.

---

## 5. TAVSIYA

```
EURUSD  +  USDJPY  +  EURGBP  +  AUDUSD
```

| | |
|---|---|
| ρ̄ | 0.25 (past) |
| Samarali namuna | 58% |
| 30 ga yetish | **2.2 oy** |
| Risk | har savdoda 2% (o'zgarmaydi) |

### Nega aynan shular
- **USDJPY** — EURUSD bilan −0.22, eng mustaqil
- **EURGBP** — kross juftlik, USD ta'siridan tashqarida
- **AUDUSD** — commodity valyuta, boshqa drayver

---

## 6. QAT'IY QOIDALAR (buzilsa tahlil yaroqsiz)

### a) Oldindan e'lon
Bu to'rt juftlik **hozir** tanlandi, natijaga qaramasdan.
Keyin "GBPUSD ham qo'shaylik" deyish **taqiqlanadi**.

### b) Birlashtirib hisoblash
Barcha savdolar **bitta jurnalda**, bitta statistika.
"EURUSD yaxshi ishladi, unga o'tamiz" — bu cherry-picking, **taqiqlanadi**.

Bonferroni jazosi:
| Holat | k | Kritik t | t=3.167 |
|---|---|---|---|
| Hozir | 26 | 3.10 | o'tadi |
| +4 juftlik **alohida** baholansa | 30 | 3.14 | o'tadi |
| +9 juftlik alohida | 35 | 3.19 | **o'tmaydi** |

**Birlashtirib hisoblasak — bu bitta test, jazo yo'q.**

### c) Bir vaqtda ochiq pozitsiya chegarasi
Ikkitadan ko'p **bir yo'nalishli** (hammasi LONG yoki hammasi SHORT)
pozitsiya ochmaslik. Korrelyatsiya tufayli bu yashirin 2× risk.

### d) Parametrlar o'zgarmaydi
```
pivot 5  |  waitBars 30  |  OTE 0.5-0.618  |  limitMode YOQ
```
Har juftlikda **bir xil**. "USDJPY uchun pivot 4 yaxshiroq" — **taqiqlanadi**.

---

## 7. Amaliy tartib

1. TradingView'da 3 ta yangi grafik: USDJPY M30, EURGBP M30, AUDUSD M30
2. Har biriga strategiyani qo'shing (sozlamalar bir xil)
3. Kuniga 2 marta (07:00 / 19:00) — 4 ta tabni ko'rib chiqasiz
4. Panel `Oyna: N bar qoldi` ko'rsatsa → limit order
5. Hammasi bitta `SAVDO_JURNALI.xlsx` ga

**Diqqat:** USDJPY da pip = 0.01. Strategiyada `pipAuto` yoqilgan,
avtomatik aniqlaydi. Lot hisobida panel raqamiga ishoning.

---

## 8. Nazorat nuqtasi

```
N_eff = 30 ga yetganda (taxminan 2.2 oy, ~52 xom savdo):

PF > 2.0   -> real pulga o'tish muhokamasi
PF 1.5-2.0 -> davom, yana 30
PF 1.2-1.5 -> zaif, sozlamalar qayta ko'riladi
PF < 1.2   -> TO'XTATISH
```

Oraliq natijalarga qarab qaror qabul qilinmaydi.
