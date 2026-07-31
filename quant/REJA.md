# Photon tizimini o'lchash va avtomatlashtirish — REJA

> Maqsad: Photon metodologiyasini **his-tuyg'udan** → **raqamga** o'tkazish.
> Keyin faqat isbotlangan qismini avtomatlashtirish.

---

## Nima uchun bu tartib?

Ko'pchilik teskarisini qiladi: avval bot yozadi, keyin nega yo'qotayotganini tushunmaydi.

Biz shunday qilamiz:

```
1. O'LCHASH      → Nima ishlayotganini bilib olamiz
2. FILTRLASH     → Ishlamaydiganini tashlaymiz
3. TEZLASHTIRISH → Grafik tayyorlashni avtomatlashtiramiz
4. TEKSHIRISH    → Oldinga qarab sinaymiz
5. (ehtimol) AVTOMATLASHTIRISH → faqat isbot bo'lsa
```

Har bosqichda **to'xtash nuqtasi** bor. Agar raqamlar yomon bo'lsa — keyingi bosqichga o'tmaymiz.

---

## BOSQICH 0 — Boshlang'ich holat (BAJARILDI ✅)

| Fayl | Vazifasi |
|---|---|
| `quant/winrate_demo.py` | Win rate qopqonini ko'rsatadi |
| `quant/photon_math.py` | Photon parametrlarini tekshiradi (2 pip SL muammosi) |
| `quant/journal/schema.py` | Savdo yozuvi sxemasi |
| `quant/journal/stats.py` | Statistik tahlil dvigateli |
| `quant/journal/make_sample.py` | Sinov uchun sun'iy ma'lumot |

**Ishga tushirish:**
```bash
cd quant/journal
python3 make_sample.py                    # namuna yaratish
python3 stats.py trades_sample.csv 0.04   # tahlil
```

---

## BOSQICH 1 — Kundalik (1–2 hafta)

### Nima qilamiz
- Telegram bot: savdoni 30 soniyada yozish
- Yoki Google Sheets → CSV eksport → `stats.py`
- Screenshot avtomatik saqlanadi

### Avtomatlashtirish darajasi
| Maydon | Qanday to'ldiriladi |
|---|---|
| sana, vaqt, sessiya | **avtomatik** |
| juftlik, yo'nalish, narxlar | **avtomatik** (MT5/broker API) |
| SL pips, R natija, MAE, MFE | **avtomatik** (hisoblanadi) |
| MTF faza (A/B/C/D) | qo'lda — 1 ta tugma |
| Entry model (LC-1/LC-2A) | qo'lda — 1 ta tugma |
| POI xususiyatlari | qo'lda — checkbox |

**Ya'ni 30 ta maydondan faqat 4-5 tasi qo'lda.** Qolgani o'zi to'ladi.

### Natijada nima olasiz
Har savdodan keyin avtomatik hisobot. Hech narsani hisoblab o'tirmaysiz.

### ⛔ To'xtash nuqtasi yo'q
Bu bosqich shartsiz bajariladi. Usiz qolgan hammasi ko'r-ko'rona.

---

## BOSQICH 2 — Ma'lumot to'plash (3–6 oy)

### Nima qilamiz
**Demo yoki minimal real hisobda** Photon bo'yicha savdo qilasiz. Har savdo yoziladi.

### Necha savdo kerak?

Hisoblab chiqdim (`photon_math.py`):

| Sizning WR | Breakeven WR | Kerakli savdo |
|---|---|---|
| 30% | 25% | **323 ta** |
| 35% | 25% | **87 ta** |
| 40% | 25% | **41 ta** |

**Minimal chegara: 100 ta savdo.** Undan kam bo'lsa — statistika yolg'on gapiradi.

### Natijada nima olasiz

Aniq javoblar:
- Qaysi MTF faza pul keltiryapti? (Photon D fazani "avoid" degan — sizda ham shunaqami?)
- LC-1 vs LC-2A — qaysi biri kuchli?
- Sizning "HIGH probability" bahoyingiz haqiqatan yaxshi natija beryaptimi?
- Qaysi sessiyada yaxshi savdo qilasiz?
- SL o'lchami natijaga qanday ta'sir qilyapti?

### 🛑 TO'XTASH NUQTASI

100 savdodan keyin qaraymiz:

```
Expectancy > 0  VA  t-statistika > 2.0   →  BOSQICH 3 ga o'tamiz
Expectancy > 0  VA  t < 2.0              →  yana 100 savdo yig'amiz
Expectancy < 0                            →  TO'XTAYMIZ, sababini qidiramiz
```

Bu yerda halol bo'lish kerak. Agar raqamlar yomon bo'lsa — davom etish pul yo'qotish demakdir.

---

## BOSQICH 3 — Grafik tayyorlashni avtomatlashtirish (2–3 hafta)

### Nima qilamiz — Pine Script indikator

Photon'ning **obyektiv** (aniq ta'riflanadigan) qismlarini kodlaymiz:

| Element | Avtomatlashtirish mumkinmi |
|---|---|
| Swing High/Low (fraktal) | ✅ ha |
| BOS / CHoCH | ✅ ha (ta'rif aniq bo'lsa) |
| Premium / Discount zonalari | ✅ ha |
| Order Block nomzodlari | ✅ ha |
| FVG / imbalance | ✅ ha |
| Likvidlik hovuzlari (equal highs/lows) | ✅ ha |
| Sessiya oynalari | ✅ ha |
| Yangilik vaqtlari | ✅ ha |
| **"Bu POI kuchlimi?"** | ❌ yo'q — bu sizning qaroringiz |
| **"MTF fazasi qaysi?"** | ⚠️ qisman |

### ❗ Muhim
Bu **signal bermaydi**. Grafikni tayyorlab beradi, siz qaror qabul qilasiz.

Foydasi: tahlil vaqti 15 daqiqadan 3 daqiqaga tushadi, subyektivlik kamayadi.

---

## BOSQICH 4 — Oldinga qarab tekshirish (3+ oy)

### Nima qilamiz
Bosqich 2 statistikasidan **eng yaxshi kesimni** olamiz.

Masalan (sun'iy misol): *"Faqat A va C faza + LC-2A + LDN sessiya"*

Keyin **faqat shu filtr bo'yicha** yangi savdo qilasiz.

### Nima uchun bu muhim?
Bosqich 2 da topilgan pattern **o'tmishga moslashtirilgan** bo'lishi mumkin (overfitting). Yangi ma'lumotda ham ishlasa — demak haqiqiy.

### 🛑 TO'XTASH NUQTASI
```
Yangi natija ≈ eski natija   →  edge haqiqiy, Bosqich 5
Yangi natija ancha yomon     →  overfitting edi, Bosqich 2 ga qaytamiz
```

---

## BOSQICH 5 — Avtomatlashtirish (faqat 1-4 o'tsa)

### Nima qilamiz
- Signal → Telegram xabar (siz tasdiqlaysiz)
- Keyinroq: yarim-avtomatik order qo'yish
- To'liq avtomatik — faqat 6+ oy barqaror natijadan keyin

### ⚠️ Ogohlantirish
Photon diskretsion tizim. Uni to'liq avtomatlashtirish **hech qachon mumkin bo'lmasligi** ham mumkin. Bu normal — ko'p muvaffaqiyatli treyderlar qo'lda savdo qiladi.

---

## Vaqt jadvali (realistik)

| Bosqich | Muddat | Kim ishlaydi |
|---|---|---|
| 1. Kundalik | 1–2 hafta | men (kod) |
| 2. Ma'lumot yig'ish | **3–6 oy** | siz (savdo) |
| 3. Pine indikator | 2–3 hafta | men (kod) |
| 4. Forward test | 3+ oy | siz (savdo) |
| 5. Avtomatlashtirish | 1 oy | men (kod) |

**Jami: 8–14 oy.**

Agar kimdir sizga "1 oyda tayyor bot" desa — u aldayapti.

---

## Nimani KUTMASLIK kerak

❌ 90% win rate — bunday narsa yo'q
❌ Har kuni foyda — drawdown muqarrar
❌ AI bozorni bashorat qiladi — qilmaydi
❌ Backtest = kelajak natija — deyarli hech qachon
❌ Tez boyish — bu 8–14 oylik loyiha, foyda esa kafolatlanmagan

## Nimani KUTISH mumkin

✅ Aniq raqamlar: qaysi setup ishlayapti, qaysi yo'q
✅ Vaqt tejash: tahlil 5x tezroq
✅ Intizom: emotsional qarorlar kamayadi
✅ Halol javob: agar edge bo'lmasa — buni bilib olasiz (bu ham qimmatli)

---

## Eng muhim ogohlantirish

Bu rejaning **eng ehtimolli natijasi** — 100–200 savdodan keyin expectancy nolga yaqin chiqishi.

Bu muvaffaqiyatsizlik emas. Bu **pulni tejash**. Chunki muqobil variant — bilmasdan 2 yil savdo qilib, hisobni bo'shatish.

Agar edge topilsa — u kichik bo'ladi (0.1–0.3R). Renaissance ham 50.75% bilan ishlaydi. Kichik edge + intizom + vaqt = natija.
