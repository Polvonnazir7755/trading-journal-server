# TERMINAL ART — grafik bezagi va HUD

**Robotga bog'liq emas.** Bu alohida indikator — savdo signali bermaydi.
Faqat ko'rinish va foydali ma'lumot.

Fayl: `TERMINAL_ART.pine`

---

## 5 ta modul — har biri alohida yoqiladi

| № | Modul | Nima qiladi | Turi |
|---|---|---|---|
| 1 | **Sessiya zonalari** | Osiyo / London / NY — rangli quti, yuqori-quyi chizig'i | foydali |
| 2 | **HUD panel** | ATR, sessiya, kunlik diapazon, volatillik | foydali |
| 3 | **Odamchalar** | polyline stickman, narxga qarab holat | bezak |
| 4 | **Watermark** | nom + shior, shaffof | bezak |
| 5 | **Sham glow** | kuchli shamlarga nur + fon | bezak |

---

## 5 ta rang sxemasi

```
Neon (qora)     — yashil/pushti, ko'k urg'u   (default)
Oltin (qora)    — oltin/qizil
Muz (ko'k)      — moviy/pushti
Qon (qizil)     — qizil ohanglar
Yumshoq (och)   — oq fon uchun
```

---

## HUD panelda nima ko'rinadi

```
┌──────────────────────────┐
│  EURUSD          30      │
│  Sessiya    LONDON + NY  │
│  Kun          Dushanba   │
│  ATR(14)       0.00087   │
│  Kunlik diapazon 62.4 pip│
│  Diapazonda ▰▰▰▰▰▰▱▱▱▱ 64%│
│  Volatillik      normal  │
│  Narx          1.16142   │
└──────────────────────────┘
```

**"Diapazonda"** — narx kunlik diapazonning qaysi qismida turgani.
70% dan yuqori yashil, 30% dan past qizil.

**"Volatillik"** — ATR 50-kunlik o'rtachadan qanchalik farq qiladi.
YUQORI bo'lsa ehtiyot bo'ling, PAST bo'lsa harakat kutilmaydi.

---

## Odamchalar — holatlar

Narx oxirgi 50 barning qayerida turganiga qarab tanlanadi:

| Holat | Qachon | Ko'rinish |
|---|---|---|
| Qo'l ko'targan | narx yuqori 25% da | g'alaba |
| Yiqilgan | narx quyi 25% da | yotgan |
| Yugurayotgan | o'rtada | qo'llar yoyilgan |
| Tik turgan | o'rtada | oddiy |

Rang ham o'zgaradi: yuqorida yashil, pastda qizil.

---

## Sozlash

```
Odamchalar soni:  0–14   (default 6)
Hajm:             0.3–3.0
```

Ko'p qo'ysangiz grafik chalkashadi. 4–8 optimal.

---

## Texnik eslatmalar

**Limitlar** (Pine cheklovlari va bizning ishlatishimiz):

| Element | Limit | Bizda |
|---|---|---|
| box | 200 | ~60 |
| polyline | 100 | ~14 |
| label | 300 | ~40 |
| line | 300 | ~30 |

Timeout xavfi yo'q.

**`lookahead_on`** — HUD dagi kunlik diapazon uchun ishlatilgan.
Bu **bezak** ma'lumoti, savdo qaroriga ta'sir qilmaydi.
Real vaqtda joriy kunning hozirgi diapazonini ko'rsatadi.

---

## O'rnatish

1. Pine Editor → yangi skript
2. `TERMINAL_ART.pine` mazmunini qo'ying
3. Save → Add to chart

**Diqqat:** bepul tarifda grafikda **2 ta indikator** chegarasi bor.
Agar 1.618 LEGENDA ishlab tursa, TERMINAL ART ikkinchi bo'ladi —
uchinchisiga joy qolmaydi.

Demo davomida faqat 1.618 kerak. TERMINAL ART ni **alohida grafikda**
yoki demo tugagach ishlatish tavsiya etiladi.

---

## Nima YO'Q va nega

**SMC yorliqlari (BSLQ, FVG, OB, BoS)** qo'shilmadi.

Sabab: ular "foydali ko'rinadi", lekin biz EQH/EQL radar testida
ko'rgandik — statistik farq **topilmadi** (p = 0.285).

Agar keyinroq qo'shsak, har element uchun **statistika bloki**
majburiy bo'ladi: "nechta marta ishladi / nechta marta ishlamadi".
Aks holda bu ham "pretend trading" bo'lib qoladi.
