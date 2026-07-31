# 3-strategiya: QM + FIBO + OB + IMB + LIQ

> Sizning tushuntirishingiz asosida formalizatsiya.
> ❓ belgisi — aniqlashtirish kerak bo'lgan joylar.

---

## Umumiy oqim (men tushunganim)

```
1. HTF da kuchli S/R zona topiladi        (H4 / H1 / M30 / M15)
        ↓
2. LTF ga tushamiz — struktura buzilishini kutamiz
        H4 zona  → M15 da kutamiz
        H1/M30   → M5 / M1 da CHoCH kutamiz
        ↓
3. CHoCH bo'ldi → bozor orqaga qaytadi
        ↓
4. Orqada FVG / Breaker / OB qoldirganmi? → o'shani test qilamiz
        ↓
5. Istorik MAX ni bitta sham yorib o'tadi (proboy)
        ↓
6. FIB tortiladi:
     0 = oxirgi istorik MIN shamining eng past SOYASI
     1 = yorib o'tgan shamning TANASI yuqorisi (soya emas!)
        ↓
7. Narx qaytadi → 5 ta kirish zonasidan biriga
        ↓
8. Retest → KIRISH
        ↓
9. TP = 1.618
```

---

## 5 ta kirish zonasi

| # | Zona | Aniqlik |
|---|---|---|
| 1 | **1.0** (proboy darajasi) | aniq ✓ |
| 2 | **0.5** | aniq ✓ |
| 3 | **0.618** | aniq ✓ |
| 4 | **IMB** (imbalance / FVG) | ❓ qaysi FVG? |
| 5 | **OB** (max soya – min tana oralig'i) | ❓ qaysi shamning? |

---

## Hisoblangan misol (XAUUSD bullish)

```
Istorik MIN soyasi (fib 0)  : 2640.00
Yorgan sham O=2698.5 C=2704.2 H=2707.8
Tanasi yuqorisi (fib 1)     : 2704.20   ← soya emas
Diapazon                    : 64.20

FIB DARAJALARI
   0.0   : 2640.00
   0.5   : 2672.10
   0.618 : 2679.68
   1.0   : 2704.20
   1.618 : 2743.88   ← TP
```

---

## ⚠️ ENG MUHIM MUAMMO: SL qayerda?

Siz SL haqida aytmadingiz. Men fib 0 deb faraz qilib hisobladim:

| Kirish zonasi | Entry | Risk | Reward | **RR** |
|---|---|---|---|---|
| 1.0 zonasi | 2704.20 | 64.20 | 39.68 | **0.62** ❌ |
| 0.5 zonasi | 2672.10 | 32.10 | 71.78 | **2.24** ✓ |
| 0.618 zonasi | 2679.68 | 39.68 | 64.20 | **1.62** ✓ |
| IMB | 2685.75 | 45.75 | 58.13 | 1.27 |
| OB | 2703.15 | 63.15 | 40.73 | **0.64** ❌ |

**Muammo ko'rinib turibdi:** agar SL fib 0 da bo'lsa, 1.0 va OB
zonalarida RR **1 dan past** — ya'ni yo'qotish yutuqdan katta.

Demak SL boshqa joyda bo'lishi kerak. Ehtimoliy variantlar:

- ❓ Kirish zonasining ostida (masalan OB ning pastki chegarasi)
- ❓ Oxirgi swing low ostida
- ❓ Qat'iy pip masofa
- ❓ Har zona uchun boshqacha

**Bu eng muhim savol.** SL'siz backtest qilib bo'lmaydi.

---

## ❓ Aniqlashtirish kerak (12 savol)

### A. HTF zona topish

1. **"Kuchli S/R zona"** — qanday aniqlanadi?
   - Necha marta teginish kerak?
   - Zona qalinligi qancha? (sham tanasi / soyasi / ATR × N)
   - Qancha vaqt orqaga qaraymiz?

2. **H4 zona topilsa M15 ga tushamiz, H1/M30 topilsa M5/M1 ga** —
   bu qoida to'g'rimi? M15 zona topilsa qaysi TF ga tushamiz?

### B. CHoCH

3. **CHoCH ta'rifi** — swing nuqtalari qanday belgilanadi?
   - Fraktal (2 chap, 2 o'ng)?
   - Yoki boshqa usul?

4. CHoCH **yopilish** bilan tasdiqlanadimi yoki teginish yetarlimi?

### C. Proboy shami

5. **"Istorik max"** — qancha orqaga qaraymiz?
   - Oxirgi 20 sham? 50? Butun sessiya?

6. Proboy **yopilish** bilanmi yoki soya tegsa yetarlimi?

7. **"Bitta sham yorib o'tadi"** — agar 2-3 sham asta-sekin yorsa,
   bu setup hisoblanmaydimi?

### D. Fib ankorlari

8. **"Oxirgi istorik minimum"** — qaysi oraliqda qidiramiz?
   Proboydan oldingi eng past nuqtami, yoki swing low mi?

### E. Kirish zonalari

9. **IMB** — qaysi FVG? Proboy shamidan keyingi 3-sham FVG mi?
   Yoki CHoCH dan keyingi?

10. **OB "max soya va min tana oralig'i"** — bu qaysi shamning?
    Proboy shamining o'zimi? Yoki oldingi qarama-qarshi sham?

11. **Bir vaqtda bir necha zona shakllansa** — qaysi biriga kiramiz?
    - Birinchi teginganigami?
    - Eng chuqurigami?
    - Har biriga alohida savdomi?

12. **"Retest bergandan keyin kiramiz"** — retest qanday aniqlanadi?
    - Zonaga tegib qaytish?
    - Zonada sham yopilishi?
    - LTF da tasdiq (CHoCH) kerakmi?

### F. Boshqa

13. **"Fib 1.618 gacha bir nechta shamni o'zida chiqib berishi kerak"** —
    bu qismni tushunmadim. Iltimos qayta tushuntiring.

14. **QM pattern** (Quasimodo) — uni qanday aniqlaymiz?
    Yoki u CHoCH bilan bir xilmi?

15. Qaysi juftlik/aktiv? Qaysi sessiya? Yangilik filtri bormi?

---

## Kuchli tomonlari (oldindan)

✅ **Fib ankorlari juda aniq** — "tanasi, soya emas" degan detal muhim
✅ **TP qat'iy** (1.618) — subyektivlik yo'q
✅ **Ko'p tasdiq** — HTF zona + CHoCH + FVG/OB + fib
✅ **Obyektiv qismi ko'p** — kodlanishi mumkin

## Xavflar

⚠️ **Ko'p shart = kam signal.** 5 ta filtr birga kelishi kamdan-kam.
   Backtestda 300 savdo topilmasligi mumkin.

⚠️ **5 ta kirish zonasi = 5 ta alohida gipoteza.** Ularni birlashtirib
   emas, alohida o'lchash kerak (`stats.py` kesimlari).

⚠️ **1.618 TP ko'p bo'lishi mumkin.** Hisobga ko'ra 1.0 zonasidan
   kirsangiz RR 0.62 — bu yutqazadigan matematika.

---

## Keyingi qadam

Yuqoridagi savollarga javob bering (ayniqsa **SL** va **13-savol**),
men to'liq kodni yozaman:

1. `qm_scanner.py` — setuplarni avtomatik topadi
2. `qm_backtest.py` — spred/slippage bilan sinaydi
3. Har kirish zonasi bo'yicha alohida statistika

Javoblar noaniq bo'lsa ham yozing — men bir necha variantni sinab,
qaysi biri sizning tasavvuringizga mos kelishini ko'rsataman.
