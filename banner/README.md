# Grand Academy — banner variantlari

Asl rasmdagi ma'lumotlar saqlangan, dizayn yangi.

## Uch yo'nalish

| Fayl | Uslub | Kimga |
|---|---|---|
| `v1_lyuks.png` | To'q yashil marmar + oltin, klassik lyuks | Nufuz, jiddiylik |
| `v2_zamonaviy.png` | Och fon + 3D clay obyektlar, do'stona | Yosh auditoriya, ota-onalar |
| `v3_grafik.png` | Swiss/brutalist tipografika, kuchli kontrast | E'tibor tortish, zamonaviy brend |
| `v3_tahrirlanadigan.html` | v3 ning aniq HTML nusxasi | **Bosmaga tayyorlash** |

## Nega HTML kerak

AI rasm matnni ba'zan buzadi. HTML versiyada:
- Har harf aniq
- Telefon raqamlarni bir joydan o'zgartirasiz
- **Haqiqiy QR rasm qo'yiladi**
- 1080x1350 (Instagram 4:5) aniq o'lchov

## HTML dan rasm olish

1. Faylni brauzerda oching (Chrome tavsiya)
2. `F12` → `Ctrl+Shift+P` → `screenshot` deb yozing
3. **"Capture node screenshot"** → `.poster` elementini tanlang
4. 1080x1350 PNG tushadi

Yoki: `Ctrl+P` → Saqlash PDF → Margins: None.

## QR joylash

```html
<div class="qr"><img src="qr1.png"></div>
```
Kommentariyani olib tashlab, `qr1.png` / `qr2.png` fayllarini shu papkaga qo'ying.

## O'zgartirish joylari

| Nima | Qayerda |
|---|---|
| Telefon raqam | `.ct-num` |
| Fan nomi | `.nm span` |
| Ajratilgan fan (oltin qator) | `class="item hot"` ni boshqa qatorga ko'chiring |
| Rang | `:root` dagi `--green` `--gold` `--cream` |

Shrift: **Archivo** (Google Fonts). Internet bo'lmasa Arial Narrow ga tushadi.
