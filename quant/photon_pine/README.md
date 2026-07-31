# Photon MTF v2

**Fayl:** `PHOTON_V2.pine`

---

## Grafikda nima ko'rinishi kerak

| Element | Ko'rinishi |
|---|---|
| **Dashboard** (o'ng yuqorida) | HTF/MTF swing/internal, faza, faza statistikasi |
| **DEBUG panel** (chap pastda) | Nega savdo yo'q — bosqichma-bosqich |
| **Zonalar** | OB / FVG qutilari (qisqa, cheksiz cho'zilmaydi) |
| **▲ / ▼** | Kirish signallari |
| **3 chiziq** | Entry (ko'k), SL (qizil), TP (yashil) — pozitsiya ochiqda |

Agar dashboard **ko'rinmasa** → ⑧ bo'limda "Dashboard" yoqilganini tekshiring.

---

## DEBUG panel — eng muhim vosita

Chap pastda chiqadi. Nega savdo yo'qligini **bosqichma-bosqich** ko'rsatadi:

```
DEBUG — nega savdo yo'q?          soni
Xom signal (sweep/POI)            847
  + faza filtridan o'tdi          198
  + yo'nalish mos                  96
  + sessiya/guard/cooldown         54
JAMI OCHILGAN SAVDO                54

Faza barlar soni                  bar
A / B                        1240 / 1180
C / D                        1190 / 1200
RANGE                        6300  (56%)
```

### Qanday o'qish

Qaysi qatorda raqam **keskin tushsa** — muammo o'sha yerda:

| Qator kam bo'lsa | Yechim |
|---|---|
| **Xom signal** kam | ④ da ko'proq manba yoqing (CHoCH ham) |
| **Faza filtri** ko'p kesyapti | ⑤ da C fazani ham yoqing |
| **Yo'nalish** ko'p kesyapti | MTF swing bias tez o'zgaryapti → SWING fraktalni oshiring |
| **Sessiya/cooldown** | ⑦ sessiyani o'chiring, cooldown 5→2 |
| **RANGE 70%+** | SWING fraktalni kamaytiring (5→4) |

---

## v1 dan farqi

### 1. SWING va INTERNAL ajratildi ⭐

v1 da faza **noto'g'ri** hisoblanardi. Photon'da swing va internal —
bir xil TF da, **turli fraktal o'lchamida**:

```
MTF SWING    = katta fraktal (5)  -> asosiy tuzilma
MTF INTERNAL = kichik fraktal (2) -> ichki harakat

Pro Swing    = MTF swing == HTF bias
Pro Internal = MTF internal == MTF swing
```

### 2. Signal manbai kengaytirildi

A+B faza barcha holatlarning atigi **~22%** ini tashkil qiladi.
50 savdo uchun ~225 signal kerak. Shuning uchun 4 ta manba:

LTF sweep · MTF sweep · POI tap · LTF CHoCH

### 3. Zonalar endi ekranni to'ldirmaydi

- `extend.right` olib tashlandi
- Teginilgach — kulrang bo'lib **to'xtaydi**
- Maks soni va uzunligi sozlanadi (⑧ bo'lim)

### 4. Entry / SL / TP chiziqlari

### 5. Faza bo'yicha statistika

---

## Sozlash tartibi — 50 savdo

**1.** Properties → Backtest date range → **2022.01.01**

**2.** DEBUG panelga qarang, qaysi bosqichda tushib qolganini toping

**3.** Yuqoridagi jadval bo'yicha **bittadan** o'zgartiring

**4.** 50+ bo'lgach — **hech narsani o'zgartirmasdan** faza statistikasini o'qing

---

## ⚠️ Ogohlantirish

Sozlamalarni "yaxshi natija" chiqquncha burash — **overfitting**.

To'g'ri: avval savdo sonini oshiring, keyin natijani **o'qing**.
Natija yomon bo'lsa ham — bu javob.

---

## Kutilgan natija

**A fazada win rate yaxshi chiqishi shart emas.**

Photon shunday da'vo qiladi, biz buni **sinayapmiz**:

- A > B → nazariya tasdiqlanadi
- A ≈ B → faza filtri foydasiz
- A < B → nazariya teskari ishlaydi

Har uchalasi ham qimmatli ma'lumot.
