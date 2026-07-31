# Photon savdo kundaligi + statistika

## Tez boshlash

```bash
# 1. Namuna ma'lumot yaratish (sinov uchun)
python3 make_sample.py

# 2. Tahlil qilish
python3 stats.py trades_sample.csv 0.04
#                 ^fayl            ^spred solig'i (R da)
```

## O'z ma'lumotingiz bilan

`trades.csv` faylini `schema.py` dagi `CSV_COLUMNS` tartibida to'ldiring,
yoki Google Sheets dan CSV eksport qiling.

```bash
python3 stats.py trades.csv 0.04
```

## Spred solig'ini qanday hisoblash

```
spread_cost_r = (spred + slippage, pipda) / o'rtacha SL pips
```

Masalan: spred 0.6 pip, o'rtacha SL 15 pip → `0.6 / 15 = 0.04`

## Hisobotni qanday o'qish

| Ko'rsatkich | Ma'nosi |
|---|---|
| **Expectancy** | Har savdodan o'rtacha necha R. **Eng muhim raqam** |
| **95% CI** | Win rate qayerda yotishi mumkin. Keng bo'lsa — namuna kichik |
| **t-statistika** | `>2.0` va `n>=30` bo'lsa edge ehtimoli bor. Aks holda shovqin |
| **Profit factor** | Yutuq/yo'qotish nisbati. `>1.3` yaxshi |
| **Max DD** | Eng chuqur cho'kish, R da |
| **Monte Carlo** | "Omadim kelgan bo'lsa-chi?" degan savolga javob |

## ⚠️ Diqqat

- `n < 30` bo'lsa hech qanday xulosa chiqarmang
- `trades_sample.csv` — **sun'iy** ma'lumot, faqat vositani sinash uchun
- Kesim tahlilida ko'p kesim ko'rsangiz, tasodifan "yaxshi" chiqadigani topiladi
  (multiple comparisons problem). Shuning uchun kesimni oldindan tanlang.
