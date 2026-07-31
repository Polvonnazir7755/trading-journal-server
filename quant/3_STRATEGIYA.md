# 3 strategiya — tuzatilgan reja

> **Oldingi maslahatim xato edi.** Men "namuna bo'linadi" deb aytdim, lekin
> siz to'g'ri savol berdingiz: nega bo'lish kerak? Har biriga to'liq 300 ta
> bersak bo'ladi-ku.

## Raqamlar (`why_time.py`)

| Holat | Aniqlash kuchi | Yolg'on xavf |
|---|---|---|
| 1 strategiya x 300 savdo | 47% | 2.8% |
| **3 strategiya x 300 savdo** | **32%** | **2.4%** |
| 5 strategiya x 300 savdo | 25% | 2.1% |

Kuch biroz tushadi (Bonferroni tuzatish tufayli), lekin **halokatli emas**.
Yolg'on xavf esa nazoratda qoladi.

**Xulosa: 3 strategiya mumkin.** Faqat 3 barobar ko'proq ish.

---

## BACKTEST — bu tez

| Ish | 1 strategiya | 3 strategiya |
|---|---|---|
| Setup topish (kompyuter) | 2 daqiqa | 6 daqiqa |
| **Siz ko'rib chiqasiz** | **10 soat** | **30 soat** |
| Statistik tahlil | 1 daqiqa | 3 daqiqa |

Kuniga 2 soat ishlasangiz: **3 strategiya = 15 kun.**

Backtest 12 oyning sababi emas.

---

## Har strategiya uchun alohida hujjat

Har biri uchun alohida `KESIMLAR_<nom>.md`:

- Asosiy gipoteza (1 ta)
- 5 ta oldindan belgilangan kesim
- Qabul mezoni: `t > 2.39` (3 strategiya uchun Bonferroni)
- Natija bo'limi (backtestdan keyin to'ldiriladi)

Har biriga alohida CSV, alohida statistika, alohida hisobot.

---

## Qaysi 3 tasi?

**1. Photon Trading** — sizda tayyor material bor

**2. va 3.** — sizdan taklif kutaman. Yaxshi nomzodlar:

| Nomzod | Nega mos |
|---|---|
| ICT / SMC | Photon'ga o'xshash, solishtirish qiziq |
| Trend-following (MA + ATR) | butunlay boshqa mantiq, obyektiv |
| Opening Range Breakout | to'liq avtomatlashtiriladi, tez backtest |
| Mean reversion (RSI/BB) | teskari mantiq — Photon bilan taqqoslash |

**Maslahatim:** 3 tadan kamida bittasi **to'liq avtomatik** bo'lsin
(masalan trend-following). Sababi:

- Kompyuter uni 10 000 marta backtest qiladi, sizning vaqtingiz ketmaydi
- **Nazorat guruhi** vazifasini bajaradi
- Agar Photon oddiy trend-following'dan yomon chiqsa — bu muhim ma'lumot

---

## Yangi vaqt jadvali

| Bosqich | 1 str | 3 str | Tezlashtirish |
|---|---|---|---|
| Kod (men) | 2 hafta | 3 hafta | ha |
| Backtest (siz) | 2 hafta | 5 hafta | ha |
| **Demo savdo** | **4-6 oy** | **4-6 oy** | **yo'q** |
| Forward | 2-3 oy | 2-3 oy | yo'q |

Demo bosqichida 3 strategiya **parallel** ketadi — bir vaqtda kuzatasiz.
Shuning uchun kalendar vaqt deyarli o'zgarmaydi: **12-13 oy**.
