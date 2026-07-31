# Photon MTF — TradingView indikatori va strategiyasi

## Ikki fayl

| Fayl | Nima uchun |
|---|---|
| `photon_mtf.pine` | **Indikator** — grafikni tayyorlaydi, dashboard ko'rsatadi |
| `photon_strategy.pine` | **Strategy** — backtest, win rate, PF, drawdown beradi |

---

## O'rnatish

1. TradingView → **Pine Editor** (pastda)
2. `Open` → `New indicator`
3. Kodni to'liq nusxalab qo'ying
4. `Save` → nom bering → `Add to chart`

⚠️ Xato chiqsa — menga xato matnini yuboring, tuzataman.

---

## `photon_mtf.pine` — indikator

### Nima ko'rsatadi

| Element | Izoh |
|---|---|
| **Dashboard** | HTF/MTF/LTF bias, faza, P&D, sessiya, risk |
| **MTF Faza** | A / B / C / D — Photon jadvali bo'yicha |
| **OB** | Order Block (BOS/CHoCH dan oldingi qarama-qarshi sham) |
| **FVG** | Imbalance (3 shamli bo'shliq) |
| **EQH/EQL** | Likvidlik hovuzlari |
| **P&D** | Premium (qizil) / Discount (yashil) zonalari |
| **LC-1 / LC-2A** | Likvidlik olish nuqtalari |
| **Sessiya** | London (ko'k) / NY (binafsha) fon |

### Faza mantiqi

```
A = HTF bias == MTF bias == LTF bias        (Pro Swing + Pro Internal)
B = HTF == MTF,  MTF != LTF                 (Pro Swing + Counter Internal)
C = HTF != MTF,  MTF == LTF                 (Counter Swing + Pro Internal)
D = HTF != MTF,  MTF != LTF                 (AVOID)
```

Photon materialida D faza *"very aggressive — avoid until already
consistently profitable"* deb yozilgan. Dashboard uni qizil ko'rsatadi.

### Zona mitigatsiyasi

Zona chegarasi **punktir** → hali teginilmagan (fresh)
Zona chegarasi **qalin, uzluksiz** → mitigatsiya bo'lgan

---

## `photon_strategy.pine` — backtest

### Nima beradi

TradingView'ning **Strategy Tester** panelida:
- Net profit, win rate, profit factor
- Max drawdown
- Trade list (har savdo alohida)
- Equity curve

### Ichida nima bor

```
Komissiya   : $3.5 / order
Slippage    : 2 tick
Risk        : 0.5% har savdo
TP          : 3R
Kunlik limit: 3 zarar
Sessiya     : 07-10 va 12-16
```

### Filtrlar bilan tajriba

Inputs orqali yoqib/o'chirib ko'ring:

| Filtr | Savol |
|---|---|
| A / B / C / D faza | Qaysi faza pul keltiradi? |
| LC-1 / LC-2A | Qaysi entry model yaxshi? |
| "Faqat discount/premium" | P&D filtri yordam beradimi? |
| Sessiya | LDN va NY farqi bormi? |

**Muhim:** har bir tajriba — alohida gipoteza. Ko'p sinasangiz,
bittasi tasodifan yaxshi chiqadi (p-hacking). Shuning uchun
`quant/KESIMLAR.md` dagi oldindan belgilangan ro'yxatga amal qiling.

---

## Repaint himoyasi

Barcha HTF ma'lumot **faqat yopilgan shamdan** olinadi:

```pine
f_htf(simple string tf, series float src) =>
    request.security(syminfo.tickerid, tf, src[1],
         lookahead = barmerge.lookahead_off)
                            ^^^ [1] = oldingi, yopilgan sham
```

BETA 1 da bu himoya yo'q edi — u yopilmagan shamni o'qiydi va
tarixda mukammal ko'rinadi.

**Tekshirish usuli:** indikatorni qo'shing, bir kun ishlating,
keyin grafikni yangilang (F5). Signallar joyida qolishi kerak.

---

## BETA 1 dan farqi

| | BETA 1 + LAOL | Photon (bu) |
|---|---|---|
| Kod | ~2000 qator | ~360 qator |
| Taymfreym | 25 ta | 3 ta |
| Signal turi | 640 | ~8 |
| Parametr | ~44 | ~21 |
| Repaint | **bor** | **yo'q** |
| Backtest | yo'q | **bor** |

Men ataylab soddaroq qildim. Sabab: 640 gipotezani 300 savdoda
tekshirib bo'lmaydi. Kamroq shart = ishonchliroq statistika.

---

## Cheklovlar — halol ro'yxat

❌ **"Bu POI kuchlimi?"** — kodlanmaydi, sizning qaroringiz
❌ **HTF narrativi** — kodlanmaydi
❌ **Probability bahosi** — sizniki
⚠️ **Faza taxminiy** — Photon'ning A/B/C/D ta'rifi murakkabroq,
   men soddalashtirdim (3 taymfreym bias solishtirish)
⚠️ **LC-1/LC-2A soddalashtirilgan** — asl materialda ko'proq shart bor

Bu indikator **yordamchi**, Photon'ning o'rnini bosmaydi.

---

## Keyingi qadam

1. Ikkala faylni TradingView'ga qo'ying
2. XAUUSD yoki EURUSD M15 da sinab ko'ring
3. Strategy Tester natijasini menga yuboring (skrinshot)
4. Nima to'g'ri/noto'g'ri ekanini ayting — sozlayman

**Kutilgan natija:** birinchi urinishda natija yomon chiqadi.
Bu normal. Sozlash kerak bo'ladi.
