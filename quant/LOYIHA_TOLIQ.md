# Loyiha to'liq tavsifi — 12 oy, qadam-baqadam

> Bu hujjat: kim nima qiladi, qachon, va oxirida nima bo'ladi.
> Barcha raqamlar `projection.py` va `photon_math.py` bilan hisoblangan.

---

## Qisqacha mohiyat

Biz **pul topish mashinasi** qurmayapmiz. Biz **haqiqatni aniqlaydigan asbob** quryapmiz.

Savol bitta: **Photon usuli sizning qo'lingizda pul keltiradimi yoki yo'q?**

12 oydan keyin bu savolga aniq raqam bilan javob bo'ladi. Javob "ha" ham,
"yo'q" ham bo'lishi mumkin — ikkalasi ham qimmatli.

---

## VAQT JADVALI

| Oy | Bosqich | Men qilaman | Siz qilasiz | Sarf |
|---|---|---|---|---|
| 1 | Asos | Backtest vositasi, skaner | Ma'lumot eksporti | 0 |
| 2–4 | Backtest | Tahlil, statistika | 300 setup ko'rib chiqish | 0 |
| 5 | Qaror | Hisobot | To'xtash yoki davom | 0 |
| 5–6 | Kundalik | Telegram bot, MT5 import | Sinov | 0 |
| 6–9 | Demo savdo | Haftalik tahlil | 100+ savdo (demo) | 0 |
| 10 | Qaror | Forward vs backtest | To'xtash yoki davom | 0 |
| 10–12 | Kichik real | Kuzatuv | 50+ savdo (kichik pul) | $200–500 |
| 12+ | Kengaytirish | Avtomatlashtirish | — | ? |

**Muhim: 10-oygacha hech qanday jiddiy pul tikilmaydi.**

---

## BOSQICH 1 — Asos (1-oy)

### Men qilaman
- Ma'lumot yuklovchi va sifat tekshiruvchi
- Setup skaner — Photon POI nomzodlarini avtomatik topadi
- **Ko'r-rejim backtest vositasi** (eng muhim qism)
- Look-ahead testlari

### Siz qilasiz
- MT5 dan EURUSD + GBPUSD M1 eksport (2022–2026)
- Vositani sinab ko'rish, fikr bildirish

### Ko'r-rejim nima?

Ekranda faqat **chap tomon** ko'rinadi — kelajak yopiq.

```
[Grafik: HTF + MTF + LTF]     Savol: kirasizmi?
                              [HA]  [YO'Q]
   Kelajak YOPIQ
                              Faza: [A][A2][B][C][D]
                              Model: [LC-1][LC-2A]
```

Qaror bosgandan keyingina natija ochiladi. Uch qoida:
1. Kelajak ko'rinmaydi
2. Qaror qaytarilmaydi
3. Setuplar **tasodifiy tartibda** beriladi

Bularsiz backtest o'z-o'zini aldash mashqiga aylanadi.

---

## BOSQICH 2 — Backtest (2–4 oy)

### Siz qilasiz
Kuniga 30–60 daqiqa, 5–10 ta setup ko'rib chiqasiz.
Jami **300 ta qaror**. Bu ~10 haftalik ish.

Har setupda: HA/YO'Q, MTF faza, entry model, probability.

### Men qilaman
Har 50 tadan keyin oraliq tahlil. Oxirida to'liq hisobot.

### 🛑 QAROR NUQTASI (5-oy)

| Natija | Nima qilamiz |
|---|---|
| exp > +0.15R, t > 2.0 | Davom etamiz |
| exp 0 … +0.15R | Filtrlarni qattiqlashtiramiz, yana 150 setup |
| exp < 0 | **To'xtaymiz.** Sababini qidiramiz |

---

## BOSQICH 3 — Kundalik + Demo savdo (5–9 oy)

### Men qilaman
- Telegram bot: savdo 30 soniyada yoziladi
- MT5 avtomatik import — 30 maydondan 25 tasi o'zi to'ladi
- Pine Script indikator (grafikni tayyorlaydi, signal bermaydi)

### Siz qilasiz
**Demo hisobda** Photon bo'yicha savdo. Kuniga 1–2 savdo, 4 oyda 100+.

### 🛑 QAROR NUQTASI (10-oy)

Solishtiramiz: backtest natijasi vs demo natijasi.

| Holat | Ma'nosi |
|---|---|
| Demo ≈ Backtest | Edge haqiqiy ✓ |
| Demo << Backtest | Hindsight bias bor edi |
| Demo < 0 | To'xtaymiz |

**Bu eng muhim tekshiruv.** Odatda demo backtestdan 30–50% yomonroq chiqadi.

---

## BOSQICH 4 — Kichik real (10–12 oy)

Faqat oldingi bosqichlar o'tsa. Depozit **$200–500** — yo'qotsangiz og'rimaydigan pul.

Demo va real farqi: slippage, rekvot, va eng muhimi — **psixologiya**.
Real pulda qo'l titraydi. Buni faqat real pulda o'rganasiz.

---

## NATIJALAR — halol raqamlar

### Edge darajasiga qarab (200 savdo/yil, risk 0.5%, $1000)

| Edge | Median | 5% (yomon) | 95% (yaxshi) | DD95 |
|---|---|---|---|---|
| 0.00R (yo'q) | $994 | $808 | $1223 | 13% |
| 0.05R | $1045 | $847 | $1287 | 11% |
| 0.10R | $1098 | $889 | $1349 | 10% |
| **0.20R** | **$1212** | $984 | $1494 | 8% |
| 0.35R (kuchli) | $1406 | $1148 | $1728 | 6% |

**Diqqat:** 0.20R — bu **yaxshi** natija. Yiliga +21%.

Bu Renaissance darajasidan past emas — ular 50.75% win rate bilan ishlaydi.
Lekin "oyiga 100%" va'da qilganlar bilan solishtirsangiz, kamtarona ko'rinadi.
Chunki ular yolg'on gapiradi.

### Risk foizining ta'siri (0.20R edge, $1000)

| Risk | Median | 5% | DD median | DD95 | Ruin |
|---|---|---|---|---|---|
| 0.25% | $1103 | $992 | 4% | 8% | 0% |
| **0.5%** | **$1212** | $981 | 8% | 15% | 0% |
| 1.0% | $1443 | $951 | 16% | 28% | 0% |
| 2.0% | $1934 | $833 | 30% | 50% | 1.6% |
| 3.0% | $2475 | $491 | 43% | 63% | 8% |

Photon'ning **0.5% tavsiyasi to'g'ri**. 2% dan yuqori — qimor.

---

## DEPOZIT — qancha kerak?

0.5% risk, o'rtacha SL 15 pip:

| Depozit | Risk $ | Lot | 1 pip | Baho |
|---|---|---|---|---|
| $100 | $0.50 | 0.003 | $0.03 | cent-hisob kerak |
| $500 | $2.50 | 0.017 | $0.17 | juda kichik |
| $1000 | $5.00 | 0.033 | $0.33 | ishlaydi, daromad kichik |
| **$3000** | $15 | 0.100 | $1.00 | **normal** |
| $10000 | $50 | 0.333 | $3.33 | normal |

### Mening tavsiyam

| Bosqich | Depozit | Nega |
|---|---|---|
| 6–9 oy | **$0** (demo) | o'rganish bosqichi |
| 10–12 oy | **$200–500** | psixologiya sinovi |
| 13+ oy | **$1000–3000** | faqat 12 oy musbat bo'lsa |

⚠️ **Qarz olib, uy pulidan, oxirgi puldan savdo qilmang.**
Yo'qotsangiz hayotingizga ta'sir qilmaydigan miqdor bo'lsin.

---

## PROP FIRM haqida

Modelim ko'rsatgan raqamlar (soddalashtirilgan, $10k challenge):

| Edge | risk 0.5% | risk 1% | risk 2% |
|---|---|---|---|
| 0.00R | 40% | 41% | 43% |
| 0.20R | 85% | 69% | 59% |

**Lekin bu raqamlarga ishonmang** — modelim juda optimistik.
Real hayotda challenge pass rate **5–10%**, chunki:
- kunlik zarar limiti bor
- vaqt cheklovi bor
- consistency qoidalari bor
- psixologik bosim

Haqiqiy xulosa modeldan: **risk oshirish PASS ehtimolini biroz oshiradi,
lekin funded hisobni saqlab qolishni keskin pasaytiradi.** Ya'ni omad bilan
o'tasiz, keyin kuyasiz.

Prop firm haqida 12 oydan keyin gaplashamiz.

---

## EHTIMOLLAR — ochiq baho

Menimcha natijalar shunday taqsimlanadi:

| Natija | Ehtimol | Izoh |
|---|---|---|
| Edge topilmaydi (exp ≈ 0) | **~50%** | eng ehtimolli |
| Kichik edge (0.05–0.15R) | ~30% | ishlaydi, lekin sekin |
| Yaxshi edge (0.15–0.30R) | ~15% | juda yaxshi natija |
| Kuchli edge (>0.30R) | ~5% | kamdan-kam |

**50% ehtimol bilan javob "yo'q" bo'ladi.**

Bu muvaffaqiyatsizlik emas. Bu — **pul tejash**. Muqobil variant: bilmasdan
2 yil savdo qilib, $5000 yo'qotish. Biz buni 12 oyda, deyarli bepul aniqlaymiz.

---

## NIMANI KUTMASLIK KERAK

❌ Oyiga 50–100% — bunday narsa barqaror emas
❌ 90% win rate — matematik jihatdan ma'nosiz
❌ Har oy foyda — drawdown muqarrar, 3 oy ketma-ket minus normal
❌ To'liq avtomatik robot — Photon diskretsion, avtomatlashmasligi mumkin
❌ Tez natija — 12 oy minimal muddat

## NIMANI KUTISH MUMKIN

✅ Aniq raqam: edge bormi, qancha
✅ Qaysi faza/model/sessiya ishlayotgani
✅ Tahlil 5x tezroq (Pine indikator)
✅ Intizom: har savdo yozilgan, emotsiya kamayadi
✅ **Halol javob** — eng qimmatli natija

---

## XARAJATLAR

| Nima | Narx |
|---|---|
| Kod, tahlil, vositalar | $0 (men) |
| MT5, Python, Obsidian | $0 |
| Demo hisob | $0 |
| Kichik real (10-oy) | $200–500 |
| Vaqt (siz) | ~200 soat |

Eng katta xarajat — **vaqtingiz**. Buni jiddiy o'ylab ko'ring.

---

## MENING MAJBURIYATLARIM

1. **Yaxshi natijaga shubha bilan qarayman.** Backtest 0.5R bersa,
   birinchi savolim "qayerda xato qildik?" bo'ladi
2. **Yomon natijani yashirmayman.** Minus chiqsa — aytaman
3. **Sinovsiz bot yozmayman**
4. **Har kodda look-ahead testi**

## SIZDAN KUTILADIGANI

1. **Halollik** — backtestda "bilardim" demaslik
2. **Barqarorlik** — haftada 3–5 kun, oz-ozdan
3. **Sabr** — 3 oyda natija bo'lmaydi
4. **To'xtashga tayyorlik** — raqamlar yomon bo'lsa, tan olish

---

## BUGUNGI QADAM

1. `check_setup.py` tugashini kuting
2. Natijani yuboring
3. EURUSD + GBPUSD M1 eksport
4. Men backtest vositasini yozaman

Savol bo'lsa — so'rang. Tushunmagan joyingiz qolmasin.
