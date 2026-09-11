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

---

# YANGILANISH — 11-sent 15:52

## Order #2351247956 natijasi: ISHLAMADI

Narx 1.16077 dan pastga ketdi (1.15910 gacha), Sell Limit 1.16313 ga
**qaytmadi**. Order to'lmagan.

### Jurnalga:
Yozuv #2 dagi **G, H, I, L ustunlarini o'chiring** (Kirish/SL/TP/Risk).
Faqat sana, aktiv, yo'nalish va izoh qolsin:

```
Izoh: SELL LIMIT #2351247956 (1.16313) ISHLAMADI - narx zonaga qaytmadi.
      Order oynadan tashqarida qo'yilgan edi (39-bar / 30). Zarar YO'Q.
```

Bu **backtestdagi 54.8% savdosiz setup** guruhiga tushadi — normal natija.

---

## Setup konversiya jadvali (yangilangan)

| # | Sana | Yo'nalish | Order | Natija | Izoh |
|---|---|---|---|---|---|
| 1 | ~28.08 | — | Yo'q | — | eskirgan setup |
| 2 | ~05.09 | — | Yo'q | — | eskirgan setup |
| 3 | 10.09 | SHORT | Yo'q | zonaga tegdi | agent xatosi — imkoniyat ketdi |
| 4 | 11.09 | SHORT | Ha (kech) | **to'lmadi** | oynadan tashqari |

**Holat: 4 setup, 0 savdo, 0 zarar, 0 foyda.**

---

## Backtest yangilandi (34-savdo)

| Ko'rsatkich | 33 savdo | 34 savdo |
|---|---|---|
| Net PnL | $623.11 | **$663.04** (+66.30%) |
| Profit factor | 4.506 | **4.538** |
| Max DD | $47.22 (4.57%) | $47.22 (**4.57%**) |
| Win rate | 72.73% | **73.53%** (25/34) |
| Zarar | 7 | 7 |
| BE | 2 | 2 |
| Recovery factor | 13.2 | **14.04** |
| Expectancy | +0.944R | **+0.975R** |
| O'rtacha foyda | — | +0.27% |
| O'rtacha zarar | — | −0.16% |

**WR 95% CI:** 61.2% – 89.0% (kenglik 27.7 pp; oldin 28.4 pp).
Bitta savdo CI ni atigi **0.7 punktga** toraytirdi.

### DIQQAT — bu yangi dalil EMAS

34-savdo ham **o'sha in-sample ma'lumotda**. Strategiya shu ma'lumotda
sozlangan (pivot 5 tanlangan). Backtest natijasining yaxshilanishi
kelajakdagi natija haqida yangi ma'lumot bermaydi.

Yangi dalil = **demo savdo**. Bizda hozircha **0 ta**.

---

## Risk qarori: 2%

`RISK_TAHLIL.md` asosida. Bosqichli oshirish:

| n (demo) | Shart | Risk |
|---|---|---|
| 0 → 30 | hozir | **2%** |
| 30 | PF > 1.5 | 3% |
| 60 | PF > 1.8 | 5% |
| 100 | PF > 2.0, DD < 15% | 5% + real pul |

TradingView panelida: `Hisob balansi ($)` = 1000, `Risk (%)` = 2.0
