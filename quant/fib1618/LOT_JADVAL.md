# LOT HISOBI — tez jadval

**Balans $500, risk 2% = $10 har savdoda**

---

## EURUSD

```
1 lot = 100,000 EUR
1 pip = $10  (1 lot uchun)
Formula:  lot = risk$ / (SL_pip × 10)
```

| SL (pip) | Aniq lot | **Qo'yiladigan lot** | Haqiqiy risk | % |
|---|---|---|---|---|
| 10 | 0.1000 | **0.10** | $10.00 | 2.0% |
| 15 | 0.0667 | **0.07** | $10.50 | 2.1% |
| 20 | 0.0500 | **0.05** | $10.00 | 2.0% |
| 25 | 0.0400 | **0.04** | $10.00 | 2.0% |
| 30 | 0.0333 | **0.03** | $9.00 | 1.8% |
| 40 | 0.0250 | **0.02** | $8.00 | 1.6% |
| 50 | 0.0200 | **0.02** | $10.00 | 2.0% |
| 60 | 0.0167 | **0.02** | $12.00 | 2.4% |
| 80 | 0.0125 | **0.01** | $8.00 | 1.6% |
| 100 | 0.0100 | **0.01** | $10.00 | 2.0% |

**Diqqat:** SL 60 pip da yaxlitlash riskni 2.4% ga oshiradi. Bu qabul
qilinadi, lekin 3% dan oshsa savdoni o'tkazib yuboring.

---

## XAUUSD (keyinroq qo'shilsa)

```
1 lot = 100 unsiya
Narx $1 siljisa = $100  (1 lot uchun)
Formula:  lot = risk$ / (SL_dollar × 100)
```

| SL ($) | Aniq lot | Qo'yiladigan | Haqiqiy risk |
|---|---|---|---|
| 3 | 0.0333 | 0.03 | $9.00 |
| 5 | 0.0200 | 0.02 | $10.00 |
| 8 | 0.0125 | 0.01 | $8.00 |
| 10 | 0.0100 | **0.01** | $10.00 |
| 15 | 0.0067 | 0.01 | **$15.00** ⚠️ |
| 20 | 0.0050 | 0.01 | **$20.00** ⚠️ |

**XAUUSD da SL 15$ dan katta bo'lsa — $500 balansda risk 3%+ bo'ladi.**
Minimal lot 0.01 dan pastga tushib bo'lmaydi. Bunday savdolarni
o'tkazib yuboring yoki balans o'sguncha oltinni qo'shmang.

---

## Balans o'zgarganda

Risk har doim **balansning 2%** i. Balans o'sgach qayta hisoblang:

| Balans | Risk 2% |
|---|---|
| $500 | $10 |
| $600 | $12 |
| $750 | $15 |
| $1,000 | $20 |

Formula o'zgarmaydi, faqat `risk$` boshqa bo'ladi.

---

## Tez tekshiruv

Order ochishdan oldin MT5 o'zi ko'rsatadi:
- **Margin** — bloklanadigan summa
- Agar margin balansning 50% idan oshsa — lot juda katta, qayta hisoblang

Va SL qo'yilgach MT5 da "potential loss" ko'rinadi — u **$10 atrofida**
bo'lishi kerak. Agar $30 chiqsa — lot noto'g'ri.
