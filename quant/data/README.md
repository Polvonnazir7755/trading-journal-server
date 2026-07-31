# Ma'lumot eksporti (Exness MT5)

## Nima kerak

- **Windows** kompyuter (MT5 Python API faqat Windows'da ishlaydi)
- Exness MT5 terminal **ochiq** va hisobga kirgan
- Python 3

## Qadamlar

**1. Kutubxonalarni o'rnating**
```
pip install MetaTrader5 pandas
```

**1.5. Muhitni tekshiring** (tavsiya qilinadi)
```
python check_setup.py
```
Bu skript hamma narsa joyidamikanini aytadi: Python arxitekturasi,
MT5 ulanishi, simvol nomlari, spred va tarix chuqurligi.

**2. MT5 da tarixni yuklab oling** (bu qadam MUHIM, aks holda CSV bo'sh chiqadi)

MT5 → `View` → `Symbols` (yoki Ctrl+U) → EURUSD tanlang → `Bars` tab
→ Period: **M1** → Request tugmasi → 2022.01.01 dan bugungacha

Xuddi shuni GBPUSD uchun ham qiling.

**3. Skriptni ishga tushiring**
```
python export_mt5.py
```

Yoki muayyan juftlik/yillar:
```
python export_mt5.py EURUSD 2023 2026
```

## Natijada nima chiqadi

| Fayl | Nima |
|---|---|
| `EURUSD_M1.csv` | M1 shamlar (time, OHLC, volume, spread) |
| `EURUSD_meta.txt` | Spred, digits, kontrakt hajmi, swap |

**Hajmi:** 3 yillik M1 ≈ 1.1 mln sham ≈ **60–80 MB** har juftlik uchun.

## ⚠️ Muhim eslatmalar

**Exness simvol nomlari.** Hisob turiga qarab `EURUSDm`, `EURUSDz` bo'lishi mumkin.
Skript buni avtomatik topadi.

**Meta fayl juda muhim.** Backtestda spred/swap hisobga olinmasa, natija
soxta chiqadi. Shuning uchun skript bu ma'lumotni ham saqlaydi.

**Git'ga qo'ymang.** CSV fayllar katta. `.gitignore` ga qo'shilgan.
Menga yuborish uchun: arxivlab (zip) yuboring yoki Google Drive linki bering.

## Ma'lumot kelgach nima bo'ladi

1. Sifat tekshiruvi — bo'shliqlar, anomaliyalar, hafta oxiri
2. Struktura funksiyalarini real ma'lumotda sozlash
3. Setup skaner — "mana bu 400 ta joyda MTF POI mitigatsiya bo'lgan"
4. Ko'r-rejim backtest vositasi
