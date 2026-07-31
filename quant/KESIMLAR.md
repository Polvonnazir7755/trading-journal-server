# Oldindan e'lon qilingan kesimlar (pre-registration)

> **MUZLATILGAN RO'YXAT.** Backtest boshlanishidan OLDIN yozilgan.
> Keyin o'zgartirilmaydi. Bu p-hacking'ning oldini oladi.

Sana: backtest boshlanishidan oldin
Strategiya: **Photon Trading — MTF POI + LC entry model**

---

## Asosiy gipoteza (1 ta)

**H1:** Photon usuli bo'yicha olingan savdolar musbat kutilmaga ega
(expectancy > 0, spred va komissiya hisobga olingan holda).

Qabul mezoni: `exp_R > +0.10` va `t > 2.0` va `n >= 200`

---

## Oldindan belgilangan kesimlar (5 ta, ko'p emas)

Faqat shu 5 tasi asosiy tahlilda ko'riladi.
Bonferroni tuzatish: p < 0.05/5 = **0.01** (t > 2.58)

| # | Kesim | Gipoteza | Nega tanlandi |
|---|---|---|---|
| K1 | MTF faza A/C vs B/D | A va C yaxshiroq | Photon o'zi shunday da'vo qiladi |
| K2 | LC-2A vs LC-1 | LC-2A yaxshiroq | Photon "80% LC-2A" deydi |
| K3 | Probability HIGH vs MED/LOW | HIGH yaxshiroq | o'z bahoyingiz to'g'rimi? |
| K4 | LDN vs NY sessiya | farq bor | likvidlik farqi |
| K5 | SL < 10 pip vs >= 10 pip | katta SL yaxshiroq | spred solig'i (photon_math.py) |

---

## Ikkilamchi (exploratory) — NATIJA EMAS, GIPOTEZA

Bulardan chiqqan har qanday narsa **keyingi bosqichda alohida tekshiriladi**.
Ular asosida qaror qabul qilinmaydi.

- POI stacked HTF bilanmi
- POI unmitigated (toza) mi
- LQ swept bo'lganmi
- Well-priced (P&D) holati
- EURUSD vs GBPUSD
- LONG vs SHORT
- Entry candle o'lchami
- Yangilik yaqinligi
- Hafta kuni
- Oy / mavsum

---

## Qat'iy qoidalar

1. **Backtest tugagunча statistika ko'rilmaydi.**
   Oraliq natijalar faqat "nechta setup qoldi" ni ko'rsatadi.

2. **Qoidalar o'zgartirilmaydi.** Backtest o'rtasida "aslida bu setupni
   olmasligim kerak edi" degan tuzatish kiritilmaydi.

3. **Ikkilamchi topilmalar — gipoteza.** "GBPUSD yaxshiroq ekan" degan
   xulosa faqat yangi ma'lumotda tasdiqlansa qabul qilinadi.

4. **Salbiy natija ham e'lon qilinadi.** exp < 0 chiqsa, hujjatga yoziladi.

---

## Nima uchun 5 ta, 20 ta emas?

`multi_strategy.py` hisobi:

```
Oldindan 3 ta kesim         -> yolg'on topilma xavfi ~7%
Keyin 20 ta kesim qidirish  -> ~64%   <-- p-hacking
Bonferroni bilan 10 kesim   -> ~5%
```

20 ta kesim ko'rsangiz, ulardan bittasi **deyarli kafolatlangan tarzda**
tasodifan "ajoyib" chiqadi. Keyin unga ishonib pul tikasiz.
