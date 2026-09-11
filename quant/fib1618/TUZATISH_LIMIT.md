# TUZATISH: LIMIT ORDER rejimi

`AUDIT_KIRISH.md` da topilgan seleksiya biasi tuzatildi.

---

## Nima o'zgardi

### 1. Yangi kalit: "LIMIT ORDER rejimi (realistik)"

`Settings -> KIRISH NUQTASI -> LIMIT ORDER rejimi` — **default YOQ**.

| | YOQ (yangi, realistik) | O'CHIQ (eski, biasli) |
|---|---|---|
| Trigger | setup boshlanishida order qo'yiladi | sham zona ichida yopilishini kutadi |
| Shart | `bar_index == mBreakBar + 1` | `high >= zLo and high <= zHi` |
| Kirish narxi | `zLo` (limit narxi) | `math.max(close, zLo)` |
| Buyruq turi | `strategy.entry(..., limit = e)` | `strategy.entry(...)` market |
| Muddat | `waitBars` dan keyin bekor | — |

### 2. Uch xato tuzatildi

**a) Seleksiya biasi** — `high <= zHi` sharti olib tashlandi.
Endi narx zonaga kirib yuqoriga otilsa ham savdo hisoblanadi
(chunki real limit order to'lgan bo'lardi).

**b) Kirish narxi** — `math.max(close, zLo)` -> `zLo`.
Eski kod sham zona ichida yopilsa `close` da sotardi, bu limitdan
yaxshiroq narx. Endi aynan limit narxida.

**c) Market -> haqiqiy limit order.**
`strategy.entry(..., limit = e)` ishlatiladi. TradingView orderni
bar ichida narx `e` ga tegganda to'ldiradi, sham yopilishida emas.

### 3. Expiry qo'shildi

```pine
if lifeBars > waitBars
    strategy.cancel(pendLong ? "L" : "S")
```

Order `waitBars` (30 bar) ichida to'lmasa **bekor qilinadi** —
xuddi Exness'dagi Expiry kabi. Busiz to'lmagan order abadiy osilib
qolar va kelajakda tasodifan to'lardi (bu ham bias bo'lardi).

### 4. Statistika jadvaliga qator qo'shildi

```
KIRISH REJIMI | LIMIT ORDER (realistik)      <- ko'k
KIRISH REJIMI | sham ichida (BIASLI +8pp)    <- qizil
```

---

## Nima kutilyapti

| Ko'rsatkich | Eski (biasli) | Yangi (kutilma) |
|---|---|---|
| Savdolar | 34 | **60–75** |
| Win rate | 73.53% | **60–66%** |
| Profit factor | 4.538 | **1.8–2.8** |
| Max DD | 4.57% | **8–15%** |

Savdolar soni ~2 barobar oshadi (tashlangan 52.7% qaytadi).
WR ~8 pp tushadi. PF sezilarli pasayadi.

**Bu yomonlashuv emas — bu haqiqat.** Eski raqam noto'g'ri edi.

---

## Qanday ishlatish

1. Yangi kodni TradingView'ga joylang (eskisini butunlay o'chirib)
2. `Settings -> KIRISH NUQTASI -> LIMIT ORDER rejimi` = **YOQ** ekanini tekshiring
3. Statistika jadvalining oxirgi qatorida ko'k `LIMIT ORDER (realistik)` turishi kerak
4. Sana oralig'i: Jan 2 2026 – Sep 11 2026, balans 1K, risk 2%
5. Natijani screenshot qiling

### Solishtirish uchun

Kalitni **o'chirib** qayta ishga tushiring — eski biasli raqam chiqadi.
Ikkalasining farqi = bias kattaligi.

Bu `AUDIT_KIRISH.md` dagi Monte-Carlo bashoratini (+8.21 pp)
**real ma'lumotda** tekshiradi.

---

## Qaror mezoni (o'zgarmagan)

Tuzatilgan backtest natijasiga qarab:

| PF | Qaror |
|---|---|
| > 2.0 | strategiya kuchli, demo davom |
| 1.5 – 2.0 | ishlaydi, ehtiyot bilan |
| 1.2 – 1.5 | zaif, xarajat yeb qo'yishi mumkin |
| < 1.2 | **to'xtatish, boshqa strategiya qidirish** |

Muhimi: bu raqam **hozir** ma'lum bo'ladi, 4 oy demo sarflagandan keyin emas.

---

## Boshqa kirish usullariga ta'sir

Tuzatish **faqat `4-OTE 0.5-0.618`** rejimiga tegishli.
Qolgan usullar (majburiy sham, neckline retest, FVG, order block)
o'zgarmadi — ular ham shunga o'xshash biasga ega bo'lishi mumkin,
lekin biz OTE ni ishlatamiz.
