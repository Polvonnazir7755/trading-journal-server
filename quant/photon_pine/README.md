# Photon MTF — All in One

**Bitta fayl:** `PHOTON_ALL_IN_ONE.pine`

Ichida ham vizual (OB / FVG / likvidlik / P&D / dashboard),
ham **backtest** (win rate, profit factor, drawdown).

---

## O'rnatish

1. TradingView → pastdagi **Pine Editor**
2. `Open` → `New strategy`
3. Kodni to'liq nusxalab qo'ying (eski kodni o'chiring)
4. `Save` → nom bering → `Add to chart`

Xato chiqsa — matnini menga yuboring.

---

## Ikki rejim

Sozlamalarning birinchi bo'limida:

| Rejim | Nima qiladi |
|---|---|
| **Backtest** | Savdo ochadi → Strategy Tester raqamlarni ko'rsatadi |
| **Faqat indikator** | Savdo ochmaydi, faqat grafikni tayyorlaydi |

Kundalik ishda "Faqat indikator", tekshirishda "Backtest".

---

## Dashboard

| Qator | Ma'nosi |
|---|---|
| HTF / MTF / LTF | Har taymfreymda bias + oxirgi BOS/CHoCH |
| **MTF Faza** | A / B / C / D — Photon jadvali |
| Izoh | Faza tavsifi |
| P&D | Premium / Discount + foiz |
| Oxirgi LC | LC-1 yoki LC-2A, necha bar oldin |
| Sessiya | London / New York |
| SL / Risk | Taxminiy SL pip va risk summasi |
| **Real RR** | Spred hisobga olingan RR |
| Rejim | Joriy rejim + bugungi zararlar |

### Faza mantiqi

```
A = HTF = MTF = LTF        Pro Swing + Pro Internal
B = HTF = MTF, MTF != LTF  Pro Swing + Counter Internal
C = HTF != MTF, MTF = LTF  Counter Swing + Pro Internal
D = hech biri              AVOID (Photon: "avoid until profitable")
```

---

## Grafikdagi elementlar

| Element | Ko'rinishi |
|---|---|
| **OB** | Yashil/qizil quti, "OB" yozuvi |
| **FVG** | Teal/maroon quti |
| **EQH / EQL** | Nuqtali chiziq + yorliq |
| **P&D** | Yuqorida qizil (premium), pastda yashil (discount) |
| **LC-1 / LC-2A** | Sweep nuqtasida yorliq |
| **Sessiya** | Ko'k (LDN) / binafsha (NY) fon |

**Zona chegarasi punktir** = hali teginilmagan (fresh)
**Zona chegarasi qalin** = mitigatsiya bo'lgan

---

## Backtest sozlamalari

Ichiga qo'yilgan:

```
Komissiya    : $3.5 / order
Slippage     : 2 tick
Risk         : 0.5% har savdo
TP           : 3R
Kunlik limit : 3 zarar
Sessiya      : 07-10 va 12-16
```

### Filtrlar bilan tajriba

| Filtr | Savol |
|---|---|
| A / B / C / D | Qaysi faza pul keltiradi? |
| LC-1 / LC-2A | Qaysi entry model kuchli? |
| "Faqat discount/premium" | P&D filtri yordam beradimi? |

⚠️ Har tajriba — alohida gipoteza. Ko'p sinasangiz, bittasi tasodifan
yaxshi chiqadi. `quant/KESIMLAR.md` dagi ro'yxatga amal qiling.

---

## Repaint himoyasi

```pine
f_htf(simple string tf, series float src) =>
    request.security(syminfo.tickerid, tf, src[1],
         lookahead = barmerge.lookahead_off)
                            ^^^ [1] = faqat YOPILGAN sham
```

**Tekshirish:** indikatorni qo'ying, bir kun ishlating, keyin F5 bosing.
Signallar joyida qolishi kerak.

---

## Cheklovlar — halol ro'yxat

- "Bu POI kuchlimi?" — kodlanmaydi, sizning qaroringiz
- HTF narrativi — kodlanmaydi
- Probability bahosi — sizniki
- Faza soddalashtirilgan — Photon ta'rifi murakkabroq
- LC-1/LC-2A soddalashtirilgan — asl materialda ko'proq shart bor

Bu **yordamchi vosita**, Photon'ning o'rnini bosmaydi.

---

## BETA 1 dan farqi

| | BETA 1 + LAOL | Photon (bu) |
|---|---|---|
| Kod | ~2000 qator | ~420 qator |
| Taymfreym | 25 ta | 3 ta |
| Signal turi | 640 | ~8 |
| **Repaint** | **bor** | **yo'q** |
| **Backtest** | **yo'q** | **bor** |

Ataylab soddaroq qildim: 640 gipotezani 300 savdoda tekshirib bo'lmaydi.

---

## Keyingi qadam

1. Faylni TradingView'ga qo'ying
2. XAUUSD yoki EURUSD **M15** da sinang
3. Strategy Tester natijasini menga yuboring (skrinshot)

**Kutilgan natija:** birinchi urinishda yomon chiqadi. Bu normal.
