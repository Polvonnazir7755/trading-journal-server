# Gann Square of 9 — "STYLE FX calculator" formulasi

## Aniqlangan formula

Skrinshotdagi kalkulyator aynan shuni hisoblaydi:

```
sqrt(narx)  ->  +/- k/8  ->  kvadratga ko'tarish
```

## Tasdiqlash (11/11 aniq moslik)

Markaz **2704.00**, chunki `sqrt(2704) = 52.000` — aniq butun son.

| qadam | sqrt | narx | skrinshotda |
|---|---|---|---|
| −5 | 51.375 | 2639.39 | Support 4 ✓ |
| −4 | 51.500 | 2652.25 | Support 3 ✓ |
| −3 | 51.625 | 2665.14 | Support 2 ✓ |
| −2 | 51.750 | 2678.06 | Support 1 ✓ |
| −1 | 51.875 | 2691.02 | ✓ |
| **0** | **52.000** | **2704.00** | **MARKAZ** ✓ |
| +1 | 52.125 | 2717.02 | Resistance 1 ✓ |
| +2 | 52.250 | 2730.06 | Resistance 2 ✓ |
| +3 | 52.375 | 2743.14 | Resistance 3 ✓ |
| +4 | 52.500 | 2756.25 | Resistance 4 ✓ |
| +6 | 52.750 | 2782.56 | ✓ |

Farq: **0.004 dan kam**. Tasodif emas.

`0.125 = 1/8` = Gann doirasining 45 darajasi.

---

## Kuchli tomonlari

✅ **Obyektiv** — ikki kishi bir xil natija oladi
✅ **To'liq avtomatlashtiriladi** — sizning vaqtingiz ketmaydi
✅ **Backtest oson** — kompyuter 10 000 marta sinaydi
✅ **Parametri kam** — overfitting xavfi past

Photon subyektiv, bu obyektiv. **Yaxshi juftlik.**

---

## Zaif tomonlari

### 1. Nazariy asos yo'q
Nega narx `sqrt(P) + 1/8` nuqtasida to'xtashi kerak? Fizik yoki
iqtisodiy sabab yo'q. Bu "shunday deyilgan" darajasida.

### 2. Markaz tanlash subyektiv
Qaysi narxdan boshlanadi? Kunlik ochilish? Swing high? Butun son?
**Markazni o'zgartirsangiz, barcha darajalar siljiydi.**
Bu — yashirin erkinlik darajasi, ya'ni overfitting manbai.

### 3. Masshtab muammosi

| Aktiv | 1/8 qadam |
|---|---|
| XAUUSD 2700 | 13.0 punkt (**0.48%**) — mazmunli |
| Aksiya $100 | 2.5 dollar (2.5%) — katta |
| EURUSD 1.085 | 0.276 (**25%**) — **yaroqsiz** |

**Forex uchun Sq9 mos kelmaydi.** Faqat oltin, indeks, aksiya.

### 4. "Har joyda nishon" effekti

| div | qadam | ±0.1% zona qoplashi |
|---|---|---|
| 8 | 0.48% | 41% |
| 16 | 0.24% | 83% |
| 32 | 0.12% | **100%** |

Darajalarni zichlashtirsangiz, narx **doim** birortasining yonida bo'ladi.
Keyin har qaytishni "Gann ishladi" deb talqin qilish oson.

---

## Halol qayd: sintetik test ishlamadi

Men random walk'da permutatsiya testi o'tkazmoqchi edim.
**Adolatli nazorat qura olmadim:**

- Gann darajalari teng oraliqli emas (yuqoriga kengayadi)
- Teng oraliqli nazorat boshqa zichlikka ega bo'ladi
- Har xil seed'da p-qiymat 0.000 dan 0.485 gacha sakradi

Bu **testning o'zi ishonchsiz** ekanini bildiradi. Shuning uchun
sintetik natijani xulosa sifatida ishlatmayman.

**To'g'ri yo'l:** real XAUUSD ma'lumotida sinash, nazorat sifatida
**tasodifiy markazdan** qurilgan Sq9 setkasi. Shunda zichlik bir xil,
va yagona savol qoladi: *markaz to'g'ri tanlanganmi?*

---

## Backtest rejasi (real ma'lumot kelgach)

| # | Test | Nima aniqlanadi |
|---|---|---|
| 1 | Reaksiya chastotasi | Darajaga tegib qaytish % |
| 2 | **Tasodifiy markaz nazorati** | Gann markazi maxsusmi? |
| 3 | Turli div (8/16/32) | Qaysi zichlik yaxshi |
| 4 | Turli markaz qoidasi | Kunlik ochilish vs swing vs butun son |
| 5 | Savdo simulyatsiyasi | Spred bilan expectancy |
| 6 | Walk-forward | 2022-23 da sozlab, 2024-25 da sinash |

**Nazorat testi (#2) eng muhimi.** Agar tasodifiy markazdan qurilgan
setka ham xuddi shunday natija bersa — Gann formulasida sehr yo'q,
shunchaki "narx qandaydir setkaga tegadi" degan gap.

---

---

# 2-KALKULYATOR: "Gann Angle Calculator"

## Formula

```
daraja = ( sqrt(baza) ± burchak/180 ) ^ 2

DEGREE FACTOR = burchak / 180
```

## Tasdiqlash

**RESISTANCE, baza 2611** (o'rtacha farq 0.38 punkt):

| burchak | factor | hisoblangan | kalkulyator |
|---|---|---|---|
| 22.5° | 0.125 | 2623.79 | 2624 |
| 45° | 0.250 | 2636.61 | 2637 |
| 90° | 0.500 | 2662.35 | 2662 |
| 180° | 1.000 | 2714.20 | 2714 |
| 360° | 2.000 | 2819.39 | 2819 |

**SUPPORT, baza 2762** (o'rtacha farq 0.23 punkt) — xuddi shunday aniq.

Farqlar 0.5 punktdan kam — kalkulyator butun songa yaxlitlaydi.

**DEGREE FACTOR bloki:** `factor × 180 = 77.5102` (ekranda 77.51 deb yaxlitlangan).
Bu narxning eng yaqin 45-gradus belgisidan uzoqligini ko'rsatadi:
`sqrt(6349) − 79.25 = 0.430612` ✓

## MUHIM: ikkala kalkulyator BIR XIL tizim

| Sq9 qadam | Burchak | Factor |
|---|---|---|
| 1/8 | 22.5° | 0.125 |
| 2/8 | 45° | 0.250 |
| 4/8 | 90° | 0.500 |
| 8/8 | 180° | 1.000 |
| 16/8 | 360° | 2.000 |

**2-kalkulyator yangi narsa emas.** O'sha Square of 9, faqat qadamlar
burchak tilida yozilgan. `180° = 1.0` birlik = sqrt shkalasidagi to'liq qadam.

Yagona amaliy farq: 12.5° burchagi Sq9 setkasiga tushmaydi (0.56/8).

---

## Fayllar

| Fayl | Vazifasi |
|---|---|
| `gann_sq9.py` | 1-kalkulyator (Square of 9) |
| `gann_angle.py` | 2-kalkulyator (Angle) + ikkalasining bog'liqligi |
| `gann_reality.py` | Masshtab va zichlik tahlili |

```bash
python3 gann_sq9.py       # 1-kalkulyator
python3 gann_angle.py     # 2-kalkulyator
python3 gann_reality.py   # cheklovlar
```
