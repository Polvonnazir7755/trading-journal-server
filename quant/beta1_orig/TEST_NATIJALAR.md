# BETA 1 + LAOL — Test natijalari (XAUUSD, M3, OANDA)

## Tasdiqlangan faktlar

### Repaint testi — O'TDI ✅
Sana: 14.08.2026, davr Jul 27 – Aug 14, M3, FINAL ENTRY, risk $20

| | Eski kod | Yangi (TEZKOR) | F5 dan keyin |
|---|---|---|---|
| Max drawdown | 760.65 | 760.65 | **760.65** |
| Savdolar | 139 | 139 | **139** |
| Yutuqlar | 26 (18.71%) | 26 (18.71%) | **26 (18.71%)** |
| Profit factor | 1.321 | 1.321 | **1.321** |
| Total PnL | 917.15 | 918.27 | 919.59 |

**Xulosa:** DD/savdo/yutuq/PF uch marta bir xil → repaint yo'q.
PnL siljishi ($917→$919, 30 daqiqada) = ochiq savdoning joriy foydasi, normal.

**Oldingi $338 vs $902 farqining sababi:** timeout (skript 20 soniya limitiga urilib,
o'rtada to'xtagan). `showViz` (TEZKOR REJIM) bilan hal qilindi.

### showViz mantiqqa ta'sir qilmaydi — ISBOTLANDI ✅
Grafik yoniq va o'chiq holatda DD/savdo/yutuq/PF **100% bir xil**.

---

## BAZAVIY natija (nazorat nuqtasi)

**Sozlama:** M3, FINAL ENTRY, risk $20, TP SL×8, BE o'chiq, partial o'chiq, radar o'chiq
**Davr:** Jul 27 – Aug 14, 2026 (18 kun, in-sample)

```
Total PnL:       +$902.77 (yopilgan)   +90.28%
Max drawdown:     $760.65               43.68%
Savdolar:         139   (26 yutuq = 18.71%)
Profit factor:    1.321
Gross profit:     $3,711.77
Gross loss:       $2,809.00
O'rtacha yutuq:   $142.76  (7.14R)
O'rtacha zarar:   $24.86   (1.24R)
Expectancy:       +$6.49/savdo  (+0.325R)
Recovery factor:  1.19          ← kerak 2.0+
t-statistika:     1.17          ← kerak 2.0+
p-qiymat:         0.241         ← kerak <0.05
Break-even WR:    14.8%  (bizda 18.71% — tor ustunlik)
Bootstrap:        P(net<0) = 11.5%
```

---

## OGOHLANTIRISH: timeframe fitting

Foydalanuvchi M1, M3, M5 sinab, M3 ni tanlagan ("m5 da natija yaxshi emas").

Bitta test uchun p = 0.241. Bir necha TF sinalganda haqiqiy p:

| Sinalgan TF | Tasodifan shunday natija chiqish ehtimoli |
|---|---|
| 1 ta | 24.1% |
| 2 ta | 42.5% |
| **3 ta (M1/M3/M5)** | **56.3%** |
| 5 ta | 74.9% |

Bonferroni (3 ta test): kerakli p < 0.0167, bizda 0.241 → **o'tmadi**.

**Shuning uchun out-of-sample test majburiy.**

---

## TEST 1 — OUT-OF-SAMPLE (avval shu!)

Sozlama BAZAVIY bilan **aynan bir xil**, faqat davr boshqa.
Maqsad: M3 tanlovi haqiqiymi yoki fittingmi?

| Davr | PnL | Max DD | Savdo | WR | PF | Recovery |
|---|---|---|---|---|---|---|
| **A. Jul 27–Aug 14** (in-sample) | +902.77 | 760.65 | 139 | 18.71% | 1.321 | 1.19 |
| **B. Jul 1–26** (out-of-sample) | | | | | | |
| C. Iyun (agar ma'lumot bo'lsa) | | | | | | |

**Talqin:**
- B da PF > 1.1 va foyda → strategiyada nimadir bor, davom etamiz
- B da PF ~1.0 (nol atrofida) → M3 tanlovi tasodif, edge isbotlanmagan
- B da zarar → strategiya ishlamaydi, BE testining ma'nosi yo'q

---

## TEST 2 — BREAKEVEN

Faqat TEST 1 ijobiy bo'lsa. Davr: **ikkalasida ham** (in-sample va out-of-sample).

Sozlamalar (`POZITSIYA BOSHQARUVI` guruhi):
```
useBE = ON,  beOffset = 0.1
useTrail = OFF, usePartial = OFF, useRadar = OFF
```

### Jul 27 – Aug 14 (in-sample)

| Sozlama | PnL | Max DD | PF | Recovery | WR | BE surildi | BE'da yopildi | 4R+ yo'qotildi |
|---|---|---|---|---|---|---|---|---|
| BE o'chiq (bazaviy) | 902.77 | 760.65 | 1.321 | 1.19 | 18.71% | — | — | |
| BE @ 1.0R | | | | | | | | |
| BE @ 2.0R | | | | | | | | |

### Jul 1 – 26 (out-of-sample)

| Sozlama | PnL | Max DD | PF | Recovery | WR | BE surildi | BE'da yopildi |
|---|---|---|---|---|---|---|---|
| BE o'chiq | | | | | | — | — |
| BE @ 1.0R | | | | | | | |
| BE @ 2.0R | | | | | | | |

---

## Modelning bashorati (MFE taqsimotidan)

MFE >= X R ga yetgan savdolar ulushi:

| Chegara | Ulush |
|---|---|
| 1R | 82.8% |
| 2R | 65.8% |
| 3R | 54.5% |
| 4R | 43.2% |
| 8R (TP) | 18.8% |

Kutilgan expectancy:

| Sozlama | Optimistik | Realistik | Pessimistik |
|---|---|---|---|
| BE o'chiq | +0.694R | +0.694R | +0.694R |
| BE @ 1R | +1.307R | **+1.111R** | +0.869R |
| BE @ 2R | +1.018R | +0.873R | +0.682R |

Hatto pessimistik holatda ham BE zarar keltirmaydi → sinashga arziydi.

**Nimaga qarash:**
- `BE'da yopildi / BE surildi` > 80% → BE juda erta, yutuqlarni bo'g'yapti
- 40–60% → normal
- Net PnL keskin tushsa (902 → 300) → BE katta yutuqlarni kesyapti, R ni oshirish kerak

---

## Qabul qilish mezonlari

| Ko'rsatkich | Hozir | Kerak |
|---|---|---|
| Recovery factor | 1.19 | **2.0+** |
| Max DD | 43.68% | **<25%** |
| Profit factor | 1.321 | 1.3+ ✅ |
| t-statistika | 1.17 | **2.0+** |
| Out-of-sample PF | ? | **>1.1** |

Agar BE + partial bilan ham Recovery 2.0 ga chiqmasa va OOS ijobiy bo'lmasa —
strategiya hozirgi ko'rinishida yaroqsiz.

---

## Texnik eslatmalar

- **Broker:** OANDA (TradingView). Real hisob Exness — spread farq qiladi, natija boshqacha bo'ladi.
- **M3 bar soni:** 18 kun ≈ 5,900 bar; 26 kun ≈ 8,500 bar; 3 oy ≈ 29,600 bar
  (bepul tarifda 3 oydan uzun davr bar limitiga urilishi mumkin)
- **TEZKOR REJIM** yoqiq bo'lsin (`Grafik chizish` = o'chiq), aks holda timeout.
