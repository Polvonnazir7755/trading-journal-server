# NATIJA: LIMIT ORDER rejimi (bias tuzatilgandan keyin)

EURUSD M30, Jan 2 – Sep 11 2026, balans $1,000, risk 2%, xarajat ON.

---

## Asosiy raqamlar

```
Savdolar:          49   (29 yutuq / 19 zarar / 1 BE)
Win rate:          59.18%      95% CI: 45.2% – 71.8%
Profit factor:     2.302
Net PnL:           $579.27  (+57.93%)
Gross profit:      $1,024.32
Gross loss:        $445.05
Max drawdown:      $88.40  =  5.90%
Recovery factor:   6.55
Expectancy:        $11.82 = +0.59R
O'rtacha foyda:    +0.28%
O'rtacha zarar:    −0.17%
RR (fakt):         1.647
```

**Signal bo'yicha:**
| Signal | Net |
|---|---|
| M (SHORT) | +$391.65 |
| W (LONG) | +$187.62 |

Ikkalasi ham foydali — bu **muhim**. XAUUSD da M(short) zarar bergan edi,
bu yerda ikkala tomon ham ishlaydi.

---

## ESKI (biasli) vs YANGI (realistik)

| Ko'rsatkich | Eski | Yangi | Farq |
|---|---|---|---|
| Savdolar | 34 | **49** | +15 |
| Win rate | 73.53% | **59.18%** | **−14.35 pp** |
| Profit factor | 4.538 | **2.302** | **−2.236** |
| Net $ | 663.04 | 579.27 | −83.77 |
| Max DD | 4.57% | 5.90% | +1.33 pp |
| Recovery factor | 14.04 | **6.55** | −7.49 |
| Expectancy | +0.975R | **+0.59R** | −0.385R |

### Bias haqiqiy kattaligi

```
Monte-Carlo bashorati:  +8.21 pp
Haqiqiy o'lchov:        +14.35 pp
```

**Simulyatsiyam biasni 1.75 barobar KAM baholagan.** Ya'ni muammo men
o'ylagandan ham kattaroq edi. Siz to'g'ri vaqtda savol berdingiz.

---

## Bashorat vs haqiqat (mening tahminlarim)

| | Bashoratim | Haqiqat | Baho |
|---|---|---|---|
| Savdolar | 60–75 | 49 | **xato** (past chiqdi) |
| Win rate | 60–66% | 59.18% | deyarli mos (0.8 pp past) |
| Profit factor | 1.8–2.8 | **2.302** | **mos** — oraliqning o'rtasida |
| Max DD | 8–15% | **5.90%** | **kutilganidan yaxshi** |

Savdolar soni bashoratdan past — chunki `waitBars` expiry qo'shildi,
oyna ichida to'lmagan orderlar bekor qilinadi.

---

## Statistik ahamiyati

```
t = 3.167       n = 49       p = 0.0015

Bonferroni (26 test):  kritik t = 3.10   ->  O'TDI
Deflated Sharpe:       edge=0 da max t ~ 1.83
                       bizda 3.17, ortiqcha +1.34
```

**Bias tuzatilgandan keyin ham statistik ahamiyat saqlanib qoldi.**
Bu strategiya foydasiga eng kuchli dalil.

t eskiga qaraganda pasaydi (5.36 → 3.17), lekin n oshdi (34 → 49)
va kritik chegaradan hali ham yuqori.

---

## Bayes yangilanishi

| Dalil | LR |
|---|---|
| t = 3.167, 26 test tuzatilgan | ×18.0 |
| Bias tuzatildi, kod endi halol | ×2.5 |
| Pivot barqarorsizligi (PF 1.6→4.0→4.2→1.4) | ×0.43 |
| n = 49, CI hali keng (26.5 pp) | ×0.85 |
| **UMUMIY** | **×16.4** |

```
Prior 5%  ->  Posterior 46.4%
```

Oldingi 85% raqami **biasli ma'lumotga** asoslangan edi — u yaroqsiz.
46% — halol baho.

**Tanga tashlashdan yaxshiroq, lekin ishonch uchun yetarli emas.**

---

## Kutilgan daromad

Savdo chastotasi: 5.9/oy ≈ **71 savdo/yil**

| Stsenariy | Ehtimol | exp(R) | Yillik |
|---|---|---|---|
| Edge yo'q | 15% | 0.00 | 0% |
| Zaif | 35% | 0.20 | 28.3% |
| O'rta | 35% | 0.40 | 56.7% |
| Kuchli | 15% | 0.59 | 83.6% |
| **Kutilgan** | | | **42.3%/yil** |

Backtest fakti: **83.7%/yil** — bu o'tmish, in-sample.

---

## Qaror mezoni bo'yicha

| PF | Qaror | Bizda |
|---|---|---|
| > 2.0 | strategiya kuchli, demo davom | ✅ **2.302** |
| 1.5–2.0 | ishlaydi, ehtiyot bilan | |
| 1.2–1.5 | zaif | |
| < 1.2 | to'xtatish | |

**PF 2.302 → davom etamiz.**

---

## Nima yaxshi

1. **Bias tuzatilgandan keyin ham ishlaydi.** PF 4.5 dan 2.3 ga tushdi,
   lekin 2.3 hali ham yaxshi raqam. Ko'p strategiyalar bias tuzatilgach
   1.0 dan pastga tushadi.
2. **t = 3.167 Bonferroni'dan o'tdi** — 26 ta test qilganimiz hisobga olingan holda.
3. **Max DD 5.90%** — bashoratimdan (8–15%) yaxshiroq.
4. **Ikkala yo'nalish ham foydali** (M +$391, W +$187).
5. **Savdolar 49 ta** — 34 dan ko'proq, statistika ishonchliroq.

## Nima hali muammo

1. **CI hali keng: 45.2% – 71.8%.** Haqiqiy WR 45% bo'lishi ham mumkin.
   RR 1.647 da breakeven WR = 37.8%, ya'ni 45% da ham foyda bor —
   lekin juda kichik.
2. **Pivot barqarorsizligi tekshirilmagan.** Yangi rejimda pivot 3/4/5/6
   testini qayta o'tkazish kerak.
3. **Walk-forward yangilanmagan.** Ikki yarimga bo'lib tekshirish kerak.
4. **In-sample.** Strategiya shu ma'lumotda sozlangan.
5. **Demo savdolar: hali 0 ta.**

---

## Keyingi qadamlar

### 1. Pivot barqarorsizligini qayta tekshirish (MUHIM)
Yangi limit rejimida pivot 3, 4, 5, 6 ni sinang.
Agar PF hali ham 1.4 → 4.2 → 1.4 kabi sakrasa — overfitting saqlanib qolgan.
Agar tekisroq bo'lsa (masalan 1.8 / 2.1 / 2.3 / 2.0) — strategiya barqaror.

### 2. Walk-forward
```
Jan 2 – Apr 30   (1-yarim)
May 1 – Sep 11   (2-yarim)
```
Ikkalasida ham PF > 1.5 bo'lishi kerak.

### 3. Demo davom
Risk 2%, 30 savdo. Endi backtest bilan **adolatli** taqqoslanadi —
chunki kod sizning limit orderingiz kabi ishlaydi.

**Demo kutilmasi:** WR ~59%, PF ~2.3, 30 savdoda DD ~6-10%.
