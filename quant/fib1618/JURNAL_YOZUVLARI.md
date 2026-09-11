# Jurnal yozuvlari — qo'lda kiritish uchun

`SAVDO_JURNALI.xlsx` → varaq **"Savdolar"**, 3-qatordan boshlab.
Sariq (och-sariq) kataklar — qo'lda. Ko'k kataklar — formula, tegmang.

---

## YOZUV #1 — 10-sent setup (o'tkazib yuborilgan)

| Ustun | Qiymat |
|---|---|
| B Sana | `10.09.2026` |
| C Vaqt | `07:00` |
| D Aktiv | `EURUSD` |
| E TF | `M30` |
| F Yo'nalish | `SHORT` |
| G Kirish | *(bo'sh)* |
| H SL | *(bo'sh)* |
| I TP | *(bo'sh)* |
| J Chiqish | *(bo'sh)* |
| L Risk $ | *(bo'sh)* |
| N Izoh | `SETUP KO'RILDI, ORDER QO'YILMADI. Zona 1.16313-1.16358, neckline 1.16200. Narx zonaga TEGDI (~1.16330, 10-sent ~12:00) - oyna ichida edi. Agent xato "o'tkazib yuboring" dedi. YO'QOTILGAN IMKONIYAT.` |

> **G–L bo'sh qoldiring.** Shunda K (Natija R) hisoblanmaydi va statistikaga kirmaydi — to'g'ri, chunki savdo bo'lmagan. Bu qator faqat protsess xatosini qayd qiladi.

---

## YOZUV #2 — 11-sent limit order (Exness #2351247956)

| Ustun | Qiymat |
|---|---|
| B Sana | `11.09.2026` |
| C Vaqt | `12:36` *(Toshkent; Exness UK 07:36)* |
| D Aktiv | `EURUSD` |
| E TF | `M30` |
| F Yo'nalish | `SHORT` |
| G Kirish | `1.16313` |
| H SL | `1.16556` |
| I TP | `1.15932` *(qoida). Agar 1.15833 da qoldirsangiz — shuni yozing* |
| J Chiqish | **hozircha bo'sh** — natija chiqqach to'ldiriladi |
| L Risk $ | `19.44` |
| N Izoh | `Sell Limit #2351247956, lot 0.08. QOIDA BUZILDI: oyna 30 bar 11-sent 08:00 (Tashkent) da tugagan, order 12:36 da qo'yilgan = 39-bar. Expiry qo'yilmagan. TP dastlab 1.15833 (fib 1.879) - agent xatosi, qoida 1.15932 (fib 1.618).` |

### J (Chiqish) ni keyin qanday to'ldirish

| Natija | J ga yoziladi | K avtomatik |
|---|---|---|
| TP urildi | `1.15932` | +1.58R |
| SL urildi | `1.16556` | −1.00R |
| Order ishlamadi / o'chirdingiz | **G, H, I, L ni ham o'chiring**, faqat izoh qolsin | — |

---

## Setup konversiya hisobi (alohida yuritiladi)

Backtest: **73 setup → 33 savdo = 45.2%**. Demoda ham shu nisbat kuzatilishi kerak.

| # | Sana | Yo'nalish | Order qo'yildimi | Ishladimi | Izoh |
|---|---|---|---|---|---|
| 1 | ~28.08 | — | Yo'q | — | eskirgan setup, oyna yopiq |
| 2 | ~05.09 | — | Yo'q | — | eskirgan setup, oyna yopiq |
| 3 | 10.09 | SHORT | Yo'q | (zonaga tegdi) | agent xatosi — imkoniyat qo'ldan ketdi |
| 4 | 11.09 | SHORT | Ha (kech) | ? | #2351247956, oynadan tashqarida |

**Hozirgi holat: 4 setup ko'rildi, 0 savdo yopildi.**

---

## Hisoblash tekshiruvi (11-sent setup)

```
zHi (fib 0.5)   = 1.16358
zLo (fib 0.618) = 1.16313
mRange = (1.16358 - 1.16313) / (0.618 - 0.5) = 0.00381 = 38.1 pip
mFib0 (M cho'qqisi) = 1.16358 + 0.5 * 0.00381 = 1.16549

SL  = mFib0 + 2% * mRange = 1.16549 + 0.00008 = 1.16556   ✅
TP1 = mFib0 - 1.618 * mRange = 1.16549 - 0.00616 = 1.15932

Entry 1.16313 dan:
  SL masofa = 24.3 pip
  TP masofa = 38.3 pip
  RR = 1 : 1.58        BE win rate = 38.9%
  Lot = 20 / (24.3 * 10) = 0.082 -> 0.08
  Risk = $19.44 (1.94%)     Foyda = $30.64
  Expectancy (WR 72.7%) = 0.727*1.58 - 0.273 = +0.87R
```

TP 1.15833 bilan: 48.0 pip, RR 1:1.98, foyda $38.40, exp +1.16R —
**lekin 72.7% WR fib 1.618 da o'lchangan, 1.879 da emas.**

---

## Oyna hisobi

```
Neckline yorilishi (katta qizil sham) ~ 10-sent 12:00 UTC
30 bar x 30 daq = 15 soat
Oyna tugashi = 11-sent 03:00 UTC = 08:00 Toshkent

Order qo'yildi: 11-sent 07:36 UTC = 39-bar  ->  9 bar KECH
```

Keyingi setuplarda **Expiry majburiy**: `qolgan bar x 30 daqiqa`.
