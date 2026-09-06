# DEMO SINOV — to'liq qo'llanma

**Maqsad:** 1.618 strategiyasini real vaqtda, real pulsiz sinash.
**Muddat:** 30+ savdo (~3-4 oy)
**Nima kerak:** TradingView (bepul), Exness demo hisob, Telegram, Excel

---

## 1-QADAM — Demo hisob ochish (10 daqiqa)

1. `exness.com` → ro'yxatdan o'ting
2. **Demo hisob** oching (real emas!)
3. Sozlamalar:
   ```
   Hisob turi:  Raw Spread yoki Pro
   Balans:      $500       (real rejaga mos)
   Leverage:    1:200
   Valyuta:     USD
   ```
4. MT5 ilovasini yuklab oling (telefon yoki kompyuter)

**Nega $500?** Real hisobda ham shundan boshlaymiz. Demo balansi real
rejaga mos bo'lishi kerak — aks holda lot hisobi noto'g'ri chiqadi.

---

## 2-QADAM — TradingView alert qo'yish (5 daqiqa)

Strategiya kodida alert tayyor. Signal kelganda telefonga xabar keladi.

1. Grafikni oching: **EURUSD, M30**
2. Strategiya ishlab turganiga ishonch hosil qiling
3. Strategiya nomi yonidagi **⏰ (Alert)** tugmasini bosing
   yoki klaviaturada **Alt+A**

4. Alert oynasida:
   ```
   Condition:    1.618 LEGENDA — W/M Fibo Strategy
   →             Order fills only          ← MUHIM
   Options:      Once Per Bar Close
   Expiration:   Open-ended
   ```

5. **Notifications** tabida:
   ```
   ☑ Notify on app        (telefon ilovasi)
   ☑ Show pop-up
   ☑ Send email          (ixtiyoriy)
   ```

6. **Create** bosing

**Bepul tarifda 1 ta alert** beriladi — bu bizga yetadi.

> **Telegram'ga ulash** (ixtiyoriy): Webhook URL faqat Pro tarifda.
> Bepulda telefon ilovasi bildirishnomasi yetarli.

---

## 3-QADAM — Signal kelganda nima qilish

Alert kelganda **shoshilmang**. Tartib:

### a) Grafikni oching va tekshiring

Grafikda uchta chiziq ko'rinadi:
- 🔵 ko'k — **Entry** (kirish narxi)
- 🔴 qizil — **SL**
- 🟢 yashil — **TP1**

Bu raqamlarni yozib oling.

### b) Lot hajmini hisoblang

```
Risk $     = balans × 2%
SL masofa  = |kirish − SL| pipda
Lot        = risk$ / (SL_pip × 10)
```

**Misol:**
```
Balans $500 → risk = $10
Kirish 1.16500, SL 1.16200 → 30 pip
Lot = 10 / (30 × 10) = 0.033 → yaxlitlash 0.03
```

> EURUSD da 1 lot = 100,000. 1 pip = $10 (1 lot uchun).
> 0.01 lot = $0.10/pip.

### c) MT5 da order oching

```
Symbol:      EURUSD
Type:        Market Execution
Volume:      hisoblangan lot
Stop Loss:   grafikdagi qizil chiziq
Take Profit: grafikdagi yashil chiziq
```

**SL va TP ni DARHOL qo'ying.** "Keyin qo'yaman" demang — bu eng ko'p
uchraydigan xato.

### d) Jurnalga yozing

`SAVDO_JURNALI.xlsx` → "Savdolar" varag'i → sariq katakchalar:

| Ustun | Nima yoziladi |
|---|---|
| Sana / Vaqt | savdo ochilgan payt |
| Aktiv / TF | EURUSD / M30 |
| Yo'nalish | LONG yoki SHORT |
| Kirish | haqiqiy ochilgan narx (grafikdagi emas!) |
| SL / TP | qo'ygan darajalaringiz |
| Chiqish | **savdo yopilgandan keyin** |
| Risk $ | hisoblangan summa |
| Izoh | nima bo'lgani |

**Chiqish narxini savdo yopilgandan keyin kiritasiz.** O'shanda
Natija (R) va Foyda $ avtomatik hisoblanadi.

---

## 4-QADAM — Har hafta tekshirish

"Statistika" varag'ini oching. Uchta raqamga qarang:

| Ko'rsatkich | Mezon |
|---|---|
| Profit factor | > 1.5 yashil, < 1.0 qizil |
| Expectancy (R) | > +0.2R |
| Eng uzun zarar seriya | **8 ga yetsa — TO'XTATING** |

---

## 5-QADAM — 30 savdodan keyin qaror

"Taqqoslash" varag'i backtest bilan yonma-yon ko'rsatadi.

| Demo PF | Qaror |
|---|---|
| **> 1.5** | ✅ Real pulga o'tish: $300-500, risk 2% |
| **1.0 – 1.5** | ⏸ Davom etish, yana 30 savdo |
| **< 1.0** | ❌ To'xtatish — backtest aldagan |

### Darhol to'xtatish shartlari

- Real DD > 25%
- Ketma-ket 8 zarar
- 3 oy davomida signal yo'q

---

## MUHIM QOIDALAR

### 1. Faqat alert bergan savdolarni oching
"Menimcha bu yerda ham yaxshi setup" degan savdolar **jurnalga
kirmasin va ochilmasin**. Aks holda strategiyani emas, o'zingizni
sinaysiz.

### 2. Har savdoni yozing
Yutuqni ham, zararni ham. Faqat yutuqni yozish — o'zini aldash.

### 3. Sozlamani o'zgartirmang
30 savdo tugamaguncha pivot, TP, risk — hech narsaga tegmang.
O'zgartirsangiz — statistika nolga qaytadi.

### 4. Izoh ustuni eng qimmatli
30 savdodan keyin o'qib chiqing. Naqsh topasiz:
*"yangilik paytida hamma savdo zarar"*, *"payshanba yomon"*.
Buni backtest hech qachon ko'rsatmaydi.

### 5. Savdo chastotasi
EURUSD M30 da o'rtacha **oyiga 4-8 savdo**. Ya'ni 30 savdo uchun
**4-6 oy** kerak. Sabr qiling — bu normal.

---

## YAKUNIY SOZLAMA (TradingView)

```
Aktiv:      EURUSD
TF:         M30

PATTERN ANIQLASH
  Pivot uzunligi           5
  W/M eni (max/min bar)    60 / 5
  Ikki minimum farqi       25%
  Razvorot sharti          YOQ
  Neckline TANA bilan      YOQ

KIRISH
  Kirish usuli             4-OTE 0.5-0.618
  OTE quyi / yuqori        0.5 / 0.618

CHIQISH
  TP1                      1.618
  TP1 da yopish            100%        ← MUHIM
  SL bufer                 2%

REALISTIK XARAJAT
  ☑ Yoqilgan
  ☑ pip AVTOMATIK
  Spred/Komissiya/Slip/Swap  0.2 / 0.7 / 0.4 / 0.6

RISK
  Risk turi                Foiz %
  Risk %                   2.0

RADAR                      O'CHIQ
```

---

## KUTILMA — halol raqamlar

Backtest (33 savdo, 8 oy):
```
Win rate:       72.73%
Profit factor:  4.506
Expectancy:     +0.683R
```

**Demo natijasi bundan PAST bo'lishi normal.** Sabablari:
- Backtest 33 savdo — kichik namuna (WR CI: 57.5% – 87.9%)
- Pivot parametri barqaror emas (3 va 6 da PF 1.4-1.6)
- Real bozorda slippage, rekvot, psixologiya bor

**Realistik kutilma:**
```
Win rate:       55 – 65%
Profit factor:  1.8 – 2.8
Max DD:         10 – 20%
Yiliga:         ~30-50% (risk 2% bilan)
```

Agar demo PF 2.0 chiqsa — bu **ajoyib natija**. 4.5 kutmang.
