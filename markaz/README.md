# Biologiya Kimyo O'quv Markazi — Boshqaruv paneli

`index.html` — bitta fayl, tashqi kutubxonasiz. Barcha ikonka inline SVG.
Ochish: faylni brauzerda ochish kifoya (internet shart emas).

## Tuzilishi

```
1568 x 952
├── Sidebar 440px   — navy gradient
│   ├── Brand (logo + nom + edit tugma)
│   ├── Qidiruv
│   ├── 6 ta chat (1-si faol, badge bilan)
│   ├── Promo karta (flask + leaf)
│   └── Admin qatori
└── Main            — och-ko'k gradient
    ├── Header (eyebrow + h2 + tagline | bell + chip + sun)
    ├── 4 stat karta (yashil / ko'k / binafsha / to'q sariq)
    ├── 2 panel (muhim vaziyatlar | ta'lim jarayoni)
    ├── Dars jadvali qatori
    └── 7 ta pastki navigatsiya
```

## Rang tizimi (CSS o'zgaruvchilar)

| O'zgaruvchi | Qiymat | Ishlatilishi |
|---|---|---|
| `--navy-1/2/3` | `#0A1834` `#0D2149` `#123064` | sidebar fon |
| `--blue` | `#2563EB` | faol element, havola |
| `--green` | `#10B981` | brend, muvaffaqiyat |
| `--purple` | `#8B5CF6` | mavzu topshirish |
| `--orange` | `#F59E0B` | ogohlantirish |
| `--red` | `#EF4444` | muammo |
| `--ink / ink-2 / ink-3` | `#0F172A` `#475569` `#94A3B8` | matn ierarxiyasi |

## Tafsilotlar

- **Shrift:** Inter (tizimda bo'lmasa Segoe UI → system-ui)
- **Radius:** karta 24px, element 15-19px, tag 9px
- **Soya:** 3 daraja (`--shadow-sm/shadow/shadow-lg`)
- **Hover:** karta `translateY(-3px)`, qator fon o'zgarishi, `Barchasi →` gap kengayishi
- **Dekoratsiya:** DNA spirali + barglar — inline SVG, header ortida

## O'zgartirish

Ma'lumotlar HTML ichida qattiq yozilgan. Backend ulash uchun
`.stat-num`, `.row-t`, `.prog-n`, `.track i[style]` larni almashtirish kifoya.

`preview.png` — taxminiy ko'rinish (AI bilan chizilgan, haqiqiy render emas).
