# Photon indikatori — BETA 1 dan farqi

## Ochiq gap: men BETA 1 dek MURAKKAB yozmayman

BETA 1 da 640 xil signal turi va 44 ta parametr bor. Men buni
**kamchilik** deb baholadim, shuning uchun o'zim takrorlamayman.

| | BETA 1 + LAOL | Photon (meniki) |
|---|---|---|
| Kod hajmi | ~2000 qator | ~600 qator |
| Taymfreymlar | 25 ta | 3 ta (HTF/MTF/LTF) |
| Signal turlari | 640 | ~8 |
| Parametrlar | ~44 | ~12 |
| Repainting | bor (yopilmagan sham) | **yo'q** (faqat yopilgan) |
| Backtest | yo'q (`indicator`) | bor (`strategy` versiyasi ham) |

**Murakkablik ≠ samaradorlik.** Har qo'shimcha shart — yana bitta
overfitting imkoniyati va yana bitta statistik gipoteza.

---

## Nima kodlanadi (obyektiv qism)

✅ Swing High/Low (fraktal, tasdiqlangan)
✅ BOS / CHoCH — har 3 taymfreymda
✅ Premium / Discount (P&D) zonalari
✅ Order Block (demand/supply)
✅ FVG / imbalance
✅ Likvidlik hovuzlari (equal highs/lows)
✅ MTF faza taxmini (A / A2 / B / C / D)
✅ LC-1 (LID sweep) va LC-2A (fake break) entry modellari
✅ Sessiya oynalari (LDN / NY)
✅ Risk kalkulyatori (0.5% risk, 3R TP)
✅ Dashboard jadval

## Nima KODLANMAYDI (subyektiv qism)

❌ "Bu POI kuchlimi?" — sizning qaroringiz
❌ "R:R yetarlimi?" — sizning qaroringiz
❌ "HTF narrativi nima?" — sizning qaroringiz
❌ Probability bahosi (HIGH/MED/LOW) — sizniki

**Indikator signal bermaydi.** U grafikni tayyorlaydi, siz qaror qabul
qilasiz. Bu Photon falsafasiga mos: *"These are all suggestions."*

---

## Repaint himoyasi — asosiy farq

BETA 1 da:
```pine
request.security(..., [.., open, high, low, close, ..])
                          ^^^^^^^^^^^^^^^^^^^^^^ yopilmagan sham
```

Menda:
```pine
request.security(..., expr[1], lookahead=barmerge.lookahead_off)
                            ^^^ faqat yopilgan
```

Natija: tarixda va jonli savdoda **bir xil** ko'rinadi.
Signal titramaydi, "vaay ishlayapti" illyuziyasi yo'q.
