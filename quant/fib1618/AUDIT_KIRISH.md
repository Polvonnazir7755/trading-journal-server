# AUDIT: robot savdoni to'g'ri hisoblaydimi?

Savol: "narx zonaga kelmagan bo'lsa ham robot savdoga kirildi deb hisobladimi?"

Javob ikki qismli. Birinchisi tinchlantiradi, ikkinchisi yo'q.

---

## 1-QISM: Yo'q, robot havodan savdo yaratmaydi ✅

Kirish sharti (`FIB1618_STRATEGY.pine`, 487-qator):

```pine
mEntry := high >= zLo and high <= zHi and bar_index > mBreakBar
```

`high >= zLo` — sham maksimumi zona **quyi chegarasiga yetishi SHART**.
Narx zonaga umuman kelmasa `mEntry` hech qachon `true` bo'lmaydi.

Qo'shimcha himoyalar:
- `barstate.isconfirmed` — faqat **yopilgan** shamda hisoblaydi (repaint yo'q)
- `bar_index > mBreakBar` — yorilgan barning o'zida kirmaydi
- `ta.pivothigh(high, pivLen, pivLen)` — pivot `pivLen` bar kechikish bilan tasdiqlanadi, kelajakka qaramaydi
- `process_orders_on_close = true`

**Xulosa: bo'lmagan savdo yaratilmagan. 34 savdoning har biri real narx harakatiga asoslangan.**

---

## 2-QISM: Lekin JIDDIY SELEKSIYA BIASI bor ❌

### Muammo: `high <= zHi`

Shart ikki tomonlama:

```pine
high >= zLo   // zonaga yetdi          <- to'g'ri
high <= zHi   // zonadan OSHIB KETMADI  <- MUAMMO SHU YERDA
```

`zHi` = fib 0.5 (zona yuqori chegarasi).
Agar narx zonaga kirib, **yuqoriga otilib chiqsa** — robot bu savdoni
**butunlay e'tiborsiz qoldiradi**. Statistikaga kirmaydi.

### Nega bu yomon

Siz Exness'da **limit order** qo'yasiz. Limit `zLo` da turadi.
Narx `zLo` ga ko'tarilsa — **order to'ladi**, keyin narx qayerga
ketishidan qat'i nazar.

```
HOLAT A: narx zonaga kirdi, ichida qoldi
   Robot:  savdo hisoblanadi
   Limit:  to'ladi
   -> MOS

HOLAT B: narx zonaga kirdi va yuqoriga otildi (SL tomon)
   Robot:  E'TIBORSIZ QOLDIRADI
   Limit:  TO'LADI, keyin ko'pincha SL
   -> MOS EMAS
```

**Holat B ko'pincha ZARARLI savdolar.** Robot ularni hisoblamaydi.
Ya'ni backtest **yutuqlarni saqlab, zararlarning bir qismini tashlab yuboradi.**

### O'lchov (Monte-Carlo, 55,457 holat)

Tasodifiy yurish modeli (edge = 0), real zona o'lchamlari:
zona 4.5 pip, SL 24.3 pip, TP 38.3 pip, M30 volatilligi.

| | Soni | Ulush | Win rate |
|---|---|---|---|
| Robot HISOBLAYDI (`high<=zHi`) | 26,247 | 47.3% | **46.09%** |
| Robot TASHLAYDI (`high>zHi`) | 29,210 | 52.7% | **30.49%** |
| **Hammasi (real limit order)** | 55,457 | 100% | **37.87%** |

```
SELEKSIYA BIASI = 46.09 − 37.87 = +8.21 foiz punkt
```

Robot zonaga tekkan holatlarning **yarmidan ko'pini (52.7%) tashlab yuboradi**,
va tashlanganlarning win rate'i qolganidan **15.6 pp past**.

> Eslatma: bu simulyatsiya edge'siz tasodifiy yurish. **Mutlaq
> raqamlar (46%/38%) ma'noga ega emas** — faqat ULARNING FARQI muhim.
> Bias kattaligi ~8 pp, yo'nalishi aniq: backtest optimistik.

### Ikkinchi, kichikroq bias: kirish narxi

```pine
mPx := math.max(close, zLo)
```

SHORT uchun **yuqoriroq narxda sotish yaxshiroq**. Agar sham
zona ichida yopilsa, robot `close` da sotadi — bu `zLo` dan yaxshiroq.
Real limit esa aynan `zLo` da to'ladi.

Robot bir necha pip yaxshiroq kirish narxini oladi. 24 pip SL da
har 1 pip = 4% R.

---

## Bu 34 savdoga qanday ta'sir qiladi

| Ko'rsatkich | Backtest | Limit order bilan kutilishi |
|---|---|---|
| Win rate | 73.53% | **~65%** (8 pp past) |
| Savdolar soni | 34 | **~72** (2 barobar ko'p) |
| Profit factor | 4.538 | **sezilarli past** |

Savdolar soni ortadi, chunki tashlangan 52.7% ham savdoga aylanadi.

Konversiya 45.2% (73 setup → 33 savdo) raqami ham shundan:
setuplarning bir qismi "narx qaytmadi" emas, "narx qaytdi lekin
zonadan oshib ketdi" — bular ham hisoblanmagan.

---

## Nega demo orderingiz to'lmadi (11-sent)

Bu alohida masala, biasga aloqasi yo'q:

```
Sizning limit:      1.16313
Backtest entry:     1.16303
Farq:               1 pip
```

Zona qayta hisoblangan (yangi M pattern shakllandi, `mFib0` o'zgardi:
1.16549 → 1.16554). Sizning orderingiz **eski setupning** zonasida edi.
Narx ~1.16305 gacha ko'tarilib qaytdi — backtest zonasiga tegdi,
sizning limitingizga **1 pip yetmadi**.

Ya'ni backtest bu savdoni oldi, siz olmadingiz. **Sabab: zona siljigan.**

---

## Nima qilish kerak

### Variant A — kodni haqiqatga moslashtirish (TAVSIYA)

`high <= zHi` shartini olib tashlash. Kirish narxini `zLo` ga qattiq bog'lash:

```pine
mEntry := high >= zLo and bar_index > mBreakBar
mPx    := zLo
```

Bu **aynan limit order** xatti-harakati. Backtest raqami tushadi,
lekin **haqiqatni ko'rsatadi**.

Xarajat: PF 4.538 dan ancha pastga tushadi. Foyda: raqamga ishonch.

### Variant B — savdo usulini kodga moslashtirish

Limit emas, **shamning yopilishini kutib** bozor narxida kirish.
Sham zona ichida yopildimi — kirasiz. Oshib ketdimi — kirmaysiz.

Muammo: kuniga 48 ta M30 shami, har birini kuzatib bo'lmaydi.
Bepul tarifda alert yo'q. **Amalda imkonsiz.**

### Variant C — hech narsa qilmaslik

Backtest optimistik ekanini bilib, demo natijasini kutish.
Demo `SAVDO_JURNALI.xlsx` da yig'iladi va **haqiqatni o'zi ko'rsatadi**.

---

## Tavsiyam: A + C

1. Kodni tuzatish (`high <= zHi` olib tashlash) → **haqiqiy** backtest raqami
2. Demo savdolarni davom ettirish → mustaqil tekshiruv
3. 30 savdodan keyin ikkalasini solishtirish

Agar tuzatilgan backtest PF < 1.5 chiqsa — strategiya ishlamaydi,
va buni **demo pulini sarflashdan oldin** bilib olamiz.

---

## Bayes yangilanishi

Bu kashfiyot P(edge) ni pasaytiradi:

```
Oldingi posterior:              85%
LR (seleksiya biasi topildi):   ~0.5x
Yangi posterior:                ~74%
```

Kutilgan yillik daromad 27.5% dan **~20%** ga tushadi.

Aniq raqam kodni tuzatib qayta test qilgandan keyin ma'lum bo'ladi.

---

## Xulosa

| Savol | Javob |
|---|---|
| Robot bo'lmagan savdoni hisobladimi? | **YO'Q** — `high >= zLo` sharti bor |
| Repaint bormi? | **YO'Q** — `barstate.isconfirmed`, pivot kechikishi |
| Backtest raqami haqiqiymi? | **YO'Q** — ~8 pp optimistik seleksiya biasi |
| 73.53% WR ga ishonish mumkinmi? | **YO'Q** — limit order bilan ~65% kutiladi |

**Siz to'g'ri savol berdingiz. Bias kichik emas.**
