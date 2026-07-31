# MTF dvigateli (ko'p taymfreym)

## Asosiy g'oya

**Bitta M1 oqimi → barcha taymfreymlar undan quriladi.**

Brokerdan H4/D1 tortish shart emas. Aksincha zararli:
- broker serverida vaqt zonasi boshqacha bo'lishi mumkin
- ba'zi shamlar to'liq bo'lmaydi
- turli brokerda turli natija chiqadi

M1 dan qurish = aniq, takrorlanuvchan, brokerdan mustaqil.

## Look-ahead bias — eng katta xavf

`lookahead_demo.py` ni ishga tushiring:

```
XATO  (yopilmagan H4 ni o'qiydi)    WR=76.0%  exp=+0.520R
TO'G'RI (faqat yopilgan H4)         WR=36.0%  exp=-0.280R
                                    farq: +40 foiz punkt
```

**Bir xil ma'lumot, bir xil strategiya.** Farq faqat shundaki, birinchisi
hali yopilmagan H4 shamni o'qiydi — ya'ni kelajakni ko'radi.

Bu xato robot yozganda juda oson qilinadi va backtestda ajoyib natija beradi.
Jonli savdoda esa hammasi quladi.

## Himoya mexanizmi

`MTFEngine` klassi ikkita narsani ajratadi:

| Metod | Nima qaytaradi | Ishlatish |
|---|---|---|
| `closed(tf)` | faqat **yopilgan** shamlar | ✅ qaror qabul qilish uchun |
| `forming(tf)` | hozir shakllanayotgan sham | ⚠️ faqat joriy narx uchun |

Qaror qabul qilishda **hech qachon** `forming()` ishlatmang.

## Fayllar

| Fayl | Vazifasi |
|---|---|
| `resample_demo.py` | M1 → M5/M15/H1/H4/D1 konvertatsiya |
| `lookahead_demo.py` | Look-ahead bias namoyishi |
| `mtf_engine.py` | Asosiy dvigatel + Photon struktura funksiyalari |

## Photon funksiyalari (`structure.py`)

```python
find_swings(bars)                  # fraktal swing + confirmed_at
detect_events(bars, swings)        # BOS / CHoCH aniqlash
find_fvg(bars)                     # Fair Value Gap (imbalance)
find_order_blocks(bars, events)    # OB (demand/supply)
mark_mitigation(zones, bars)       # zona qachon teginilgan
find_liquidity(swings, tol)        # equal highs/lows (LQ hovuzlari)
premium_discount(hi, lo, price)    # P&D zonasi
current_bias(events, upto)         # joriy yo'nalish
```

Har bir natijada `confirmed_at` bor — qaysi shamda **tasdiqlangani**.
Backtestda faqat `confirmed_at <= joriy_indeks` bo'lganlarini ishlating.

## Look-ahead testi

```bash
python3 test_no_lookahead.py
```

Bir xil ma'lumotni to'liq va kesilgan holda beradi, natijalarni solishtiradi:

```
[OK]   find_swings: 37 ta element mos
[OK]   detect_events: 14 ta element mos
[OK]   find_fvg: 41 ta element mos
[OK]   find_order_blocks: 14 ta element mos

NATIJA: LOOK-AHEAD TOPILMADI ✓
```

**Kod o'zgartirilganda shu testni qayta ishga tushiring.**

## Keyingi bosqich

MTF faza (A/B/C/D) taxmini, i-BOS, LC-1 / LC-2A entry modellari —
real ma'lumot kelgach sozlanadi.

## Ishga tushirish

```bash
python3 resample_demo.py    # TF qurish namoyishi
python3 lookahead_demo.py   # bias namoyishi
python3 mtf_engine.py       # dvigatel testi
```
