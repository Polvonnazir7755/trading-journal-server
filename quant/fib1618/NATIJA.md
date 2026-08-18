# 1.618 LEGENDA — o'lchangan natijalar

## TEST 1 — XAUUSD, Kunlik (D), OTE 0.5–0.618

**Sozlama:** risk $20 qat'iy, TP1 1.618 (70%), TP2 2.618 (30%), BE yoqiq
**Davr:** OANDA to'liq tarix (~2005–2026, 21 yil)

```
Net profit:       $1,330.07
Gross profit:     $1,899.33
Gross loss:       $  569.26
Profit factor:    3.336
Savdolar:         120   (55 yutuq / 63 zarar / 2 BE)
Win rate:         45.83%
O'rtacha yutuq:   $34.53   (1.727R)
O'rtacha zarar:   $ 9.04   (0.452R)
Expectancy:       $11.08/savdo  (+0.554R)
Break-even WR:    20.7%    <- katta zaxira
```

### Statistik tekshiruv

| Test | Natija | Talab | Holat |
|---|---|---|---|
| t-statistika | **5.59** | >2.0 | ✅ o'tdi |
| p-qiymat | **<0.0001** | <0.05 | ✅ o'tdi |
| WR 95% CI | 36.9% – 54.7% | — | |
| Bootstrap (20k) 5% | +$938 | >0 | ✅ |
| Bootstrap P(zarar) | **0.00%** | <5% | ✅ |

**Signal bo'yicha:**
- W (long) | OTE = **+$1,238.40**
- M (short) | OTE = **+$91.67**

Long tomon ancha kuchli — oltinning uzoq muddatli o'sish trendi bilan izohlanadi.

---

## "GARANT 1.618" da'vosining hukmi

Video: *"garantit degani bu aynan shu zonaga bormasdan qo'ymaydi degani"*

| Da'vo | Kutilgan | Haqiqiy | Xulosa |
|---|---|---|---|
| "Garant" | 100% | **45.8%** | ❌ **yolg'on** |
| Random walk chegarasi (OTE 0.5) | 31.7% | 45.8% | ✅ ustun |
| Break-even WR (RR 3.82) | 20.7% | 45.8% | ✅ ustun |

**Xulosa:** "garant" — sotuv gapi. Lekin strategiyaning o'zi tasodif chegarasidan
sezilarli ustun ishlaydi.

### Bashorat tasdiqlandi

Kod yozishdan oldin model hisoblagan edi (OTE 0.5, 70/30 chiqish):
- TP1 40% → +0.20R
- TP1 50% → +0.50R

Haqiqiy: TP1 **45.8%** → **+0.554R**. Model to'g'ri ishladi.

---

## RISK 5% — compounding simulyatsiyasi

21 yil (120 savdo), $1000 boshlang'ich, 20,000 marta Monte-Carlo:

| Risk | 5% eng yomon | MEDIAN | 95% eng yaxshi | DD 95% | CAGR |
|---|---|---|---|---|---|
| 1% | $1,586 | $1,927 | $2,342 | 4.9% | 3.2% |
| 2% | $2,479 | $3,627 | $5,329 | 9.5% | 6.3% |
| 3% | $3,871 | $6,802 | $12,117 | 13.9% | 9.6% |
| **5%** | **$8,697** | **$22,508** | **$58,255** | **22.2%** | **16.0%** |
| 8% | $27,102 | $120,964 | $520,364 | 33.3% | 25.7% |
| 10% | $51,922 | $345,736 | $2,098,750 | 39.9% | 32.1% |

### Sezgirlik: agar haqiqiy WR pastroq bo'lsa? (risk 5%)

| Haqiqiy WR | MEDIAN | 5% yomon | DD 95% | Portlash |
|---|---|---|---|---|
| 54.8% (CI yuqori) | $68,747 | $26,562 | 18.6% | 0.0% |
| **45.8% (o'lchangan)** | **$21,503** | **$8,308** | **22.9%** | **0.0%** |
| 36.9% (CI quyi) | $6,726 | $2,888 | 30.6% | 0.0% |
| 30.0% (pessimistik) | $2,888 | $1,240 | 40.9% | 0.0% |
| 20.7% (break-even) | $903 | $431 | 65.1% | 0.0% |

**Muhim:** hatto CI ning quyi chegarasida (36.9%) ham strategiya foydali qoladi
va hisob portlamaydi.

**Sabab:** o'rtacha zarar atigi **0.452R** (partial chiqish + breakeven tufayli).
Ya'ni "5% risk" aslida savdo boshiga ~2.3% haqiqiy yo'qotish.

---

## Foydalanuvchi kuzatuvi: kichik TF larda ishlamaydi

> "unda natija faqat dailyda yaxshi chiqqan edi, kichik tf larda yaxshi emasdi"

Bu kuzatuv **nazariya bilan mos keladi** va tasodif emas.

### Nega kunlik ishlaydi, M3/M5 ishlamaydi

| Sabab | Izoh |
|---|---|
| **Tranzaksiya xarajati** | XAUUSD spred ~$0.30. Kunlikda W bo'yi $30–80 → cost 0.4–1%. M3 da W bo'yi $2–5 → cost 6–15%. Xarajat signalni yeydi |
| **Shovqin/signal nisbati** | Kichik TF da narx harakatining katta qismi — mikrostruktura shovqini, iqtisodiy ma'no yo'q |
| **Pattern sifati** | W/M pattern — bu institutsional pozitsiya to'plash izi. Kunlik masshtabda real, M3 da tasodifiy shakl |
| **Akademik dalil** | Ishlashi isbotlangan effektlar (momentum, carry, mean-reversion) deyarli hammasi kunlik+ TF da |

Bu kuzatuv strategiyaga **ishonchni oshiradi** — agar M3 da ham "ajoyib" natija chiqsa,
bu overfitting belgisi bo'lardi.

---

## Keyingi qadamlar (bajarilmagan)

| № | Vazifa | Holat |
|---|---|---|
| 1 | Risk % ga o'tkazish (compounding) | ⬜ |
| 2 | Qolgan 4 ta kirish usulini sinash | ⬜ |
| 3 | Out-of-sample: 2005–2015 vs 2016–2026 | ⬜ |
| 4 | Boshqa aktivlar: EURUSD, US500, BTCUSD (kunlik) | ⬜ |
| 5 | H4 va H1 da sinash (D va M15 orasidagi chegara) | ⬜ |

### Kirish usullari jadvali (to'ldirish kerak)

| Kirish usuli | Savdo | WR | PF | Net | Expectancy |
|---|---|---|---|---|---|
| **4-OTE 0.5-0.618** | **120** | **45.83%** | **3.336** | **$1,330** | **+0.554R** |
| 1-Majburiy sham | | | | | |
| 2-Neckline retest | | | | | |
| 5-Imbalans (FVG) | | | | | |
| 6-Order block | | | | | |

**Model bashorati:** "Majburiy sham" ancha yomon chiqishi kerak (RR 0.61,
break-even uchun 62.3% WR kerak — bu deyarli imkonsiz).

---

## Cheklovlar va ogohlantirishlar

1. **120 savdo** — statistik jihatdan yetarli, lekin bitta bozor rejimi (oltinning
   21 yillik o'sish davri). Uzoq yon bozor kelsa natija boshqacha bo'lishi mumkin.
2. **Faqat XAUUSD** — boshqa aktivlarda sinalmagan. Agar faqat oltinda ishlasa,
   bu curve-fitting bo'lishi mumkin.
3. **Faqat 1 ta kirish usuli** sinalgan.
4. **OANDA ma'lumoti** — real broker (Exness) spredi boshqacha.
5. **Yiliga 5.7 savdo** — sabr talab qiladi. Bu "tez boyish" vositasi emas.
6. **DD 22.9%** (risk 5% da) — real hisobda bunga chidash psixologik jihatdan qiyin.
   Prop firmda (limit 10%) bu risk qabul qilinmaydi.
