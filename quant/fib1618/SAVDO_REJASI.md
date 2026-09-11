# SAVDO REJASI — grafikdagi ENTRY / SL / TP chiziqlari

`FIB1618_STRATEGY.pine` ga qo'shildi. Endi setup paydo bo'lishi bilan
grafikda **uchta rangli chiziq yozuvi bilan** chiqadi.

## Nima ko'rinadi

| Chiziq | Rang | Yozuv | Ma'nosi |
|---|---|---|---|
| ENTRY | 🔵 ko'k `#2962FF` | `ENTRY 1.16313` | limit order narxi (OTE 0.618) |
| SL | 🔴 qizil `#F23645` | `SL 1.16556` | stop loss |
| TP | 🟢 yashil `#089981` | `TP 1.15932` | take profit (fib 1.618) |
| zona | kulrang quti | — | OTE 0.5–0.618 kirish zonasi |

Chiziqlar neckline yorilgan bardan boshlanib, joriy bardan **14 bar o'ngga**
cho'ziladi — narx qaytishini kutayotgan joyni ko'rsatadi.

## Panel (pastki o'ng burchak)

```
SAVDO REJASI  |  SHORT (sotish)
Holat         |  SELL LIMIT qo'ying
ENTRY         |  1.16313
SL            |  1.16556   24.3 pip
TP            |  1.15932   38.3 pip
RR            |  1 : 1.58
LOT           |  0.08
Risk          |  $19.44  (1.94%)
Foyda         |  $30.64
Oyna          |  9 bar qoldi
```

**Lot avtomatik hisoblanadi.** Sozlamalarda balansni kiriting —
`planBal` = 1000, `planRisk` = 2.0 (default). Formula: `lot = (balans × risk%) / (SL_pip × 10)`.

**"Oyna" qatori** — 30 bardan nechtasi qolgani. Yashil = vaqt bor,
to'q sariq = 3 bardan kam qoldi, qizil "OYNA YOPILDI" = order qo'ymang.

## Ustuvorlik tartibi

1. **Savdo ochiq** → real Entry/SL/TP1 ko'rsatiladi
2. **Faol M setup** → SELL LIMIT rejasi
3. **Faol W setup** → BUY LIMIT rejasi

Ikkalasi bir vaqtda bo'lsa M (SHORT) ustun — kod tartibi shunday.

## Sozlamalar (Settings → KO'RINISH → SAVDO REJASI)

| Sozlama | Default | Izoh |
|---|---|---|
| Savdo rejasini ko'rsatish | ✅ | umumiy yoqish/o'chirish |
| Chiziqlar o'ngga cho'zilishi | 14 bar | uzun qilsangiz kelajakka ko'proq cho'ziladi |
| Chiziq qalinligi | 2 | 1–4 |
| Yozuv o'lchami | normal | tiny / small / normal / large |
| Hisob balansi ($) | 1000 | **balansingizni kiriting** |
| Risk (%) | 2.0 | |
| Panelni ko'rsatish | ✅ | |

## Ish tartibi (o'zgargan)

1. Grafikni ochasiz → ko'k/qizil/yashil chiziq bormi?
2. Panelda **"Oyna: N bar qoldi"** — N > 0 bo'lsa order qo'yiladi
3. Paneldan Entry / SL / TP / Lot ni **ko'chirib** Exness'ga kiritasiz
4. **Expiry** = `N × 30 daqiqa`
5. Screenshot yuborasiz — tekshiraman

Endi men hisoblab berishimni kutish shart emas: barcha raqam grafikda.
