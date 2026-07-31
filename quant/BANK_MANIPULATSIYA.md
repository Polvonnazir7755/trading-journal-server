# "Bank manipulatsiyasi" + kichik SL + 1:10 RR

## Bilaman — bu ICT/SMC oilasining bir tarmog'i

Nomlar har xil: *liquidity sweep*, *stop hunt*, *turtle soup*, *judas swing*,
*smart money manipulation*. Mohiyat bir xil: likvidlik olinadi, keyin
narx teskari ketadi.

**Aytmoqchi — Photon'da ham bu bor.** LC-1 (LID sweep) va LC-2A (fake break)
aynan shu g'oya. Ya'ni bu sizga yangi narsa emas.

---

## HAQIQAT qismi (tasdiqlangan)

✅ **Stop hunting mavjud.** Equal highs/lows likvidlik hovuzlari — bu
haqiqiy hodisa. Institutlar katta hajmni joylash uchun likvidlik qidiradi.

✅ **Sessiya ochilishlarida oqim keskin oshadi**

✅ **Yangilik paytida spread kengayadi, slippage oshadi**

---

## MARKETING qismi (isbotlanmagan)

❌ *"Banklar sizning stopingizni ko'radi"*
Ko'rmaydi. Broker ko'radi, bank emas. A-book brokerga bu foydasiz.

❌ *"Manipulyatsiyani oldindan bilish mumkin"*
Agar oldindan bilinsa, u manipulyatsiya bo'lmay qolardi.

❌ *"1:10 kafolatlangan"*
Hech narsa kafolatlanmagan.

**Eng muhimi:** "stop hunting bor" degani "men uni bashorat qila olaman"
degani EMAS. Bu ikki butunlay boshqa da'vo.

---

## 1:10 RR matematikasi — hal qiluvchi nuqta

### Adolatli o'yinda RR hech narsa bermaydi

| RR | TP ga yetish ehtimoli | Kerakli WR | Natija |
|---|---|---|---|
| 1:1 | 50.0% | 50.0% | teng |
| 1:3 | 25.0% | 25.0% | teng |
| 1:10 | **9.1%** | **9.1%** | **teng** |
| 1:20 | 4.8% | 4.8% | teng |

**RR ni oshirish o'z-o'zidan edge yaratmaydi.** Uzoqroq TP = kamroq yetish.

Edge faqat bitta holatda paydo bo'ladi: **TP ga yetish ehtimoli nazariydan
yuqori bo'lsa.** Ya'ni 1:10 da 9.1% emas, 13%+ bo'lishi kerak.

Bu **mumkin**, lekin isbot talab qiladi.

---

## Kichik SL = katta spred solig'i

XAUUSD, spred+komissiya+slippage ≈ 0.40 USD:

| SL | Nominal RR | **Real RR** | Breakeven WR |
|---|---|---|---|
| **1.0** | 1:10 | **1:6.9** | 12.7% |
| 2.0 | 1:10 | 1:8.2 | 10.9% |
| 5.0 | 1:10 | 1:9.2 | 9.8% |
| 20.0 | 1:10 | 1:9.8 | 9.3% |

**1 USD SL da spred riskning 40%ini yeydi.** Siz 1:10 deb o'ylaysiz —
aslida 1:6.9.

Bundan tashqari kichik SL:
- slippage'ga o'ta sezgir (1 tick = riskning 10%i)
- yangilik paytida deyarli kafolatlangan zarar
- broker manipulyatsiyasiga ochiq (B-book)

---

## Psixologik to'siq — eng katta muammo

Ketma-ket zararlar (200 savdoda):

| WR | Median eng uzun | 95% holatda |
|---|---|---|
| 50% | 7 | 10 |
| 30% | 12 | 19 |
| 20% | 18 | 29 |
| **12%** | **27** | **46** |

**12% WR da ketma-ket 27 ta zarar NORMAL.**

Buni ko'tarish uchun temir asab kerak. Ko'pchilik 8-10 tadan keyin
strategiyani tashlaydi yoki qoidani buzadi.

Va bu eng yomon vaqtda sodir bo'ladi — aynan seriya tugashidan oldin.

---

## Tekshirish JUDA qiyin

Edge borligini `t > 2` bilan aniqlash ehtimoli:

| Strategiya | WR | exp | n=100 | n=300 | n=1000 |
|---|---|---|---|---|---|
| 1:1 klassik | 55% | +0.10 | 19% | 39% | 88% |
| 1:3 swing | 32% | +0.28 | 28% | **76%** | 100% |
| 1:10 | 13% | +0.43 | 14% | **52%** | 97% |

1:10 da natija juda tarqoq (bitta yutuq = 10 zarar). **300 savdoda ham
ishonchli xulosa chiqmaydi.** 1000+ kerak = 3-5 yil.

Ya'ni bu strategiyaning to'g'riligini **tez tekshirib bo'lmaydi**.

---

## MAE/MFE — yashirin tuzoq

1:10 da eng ko'p uchraydigan holat:
1. Narx 1:4 ga boradi
2. Qaytadi, SL ni oladi
3. Natija −1R, lekin siz *"deyarli yutgan edim"* deb his qilasiz

Keyin nima bo'ladi:
- *"TP juda uzoq"* → TP qisqartiriladi → WR oshadi, exp tushadi
- *"SL juda yaqin"* → SL kengaytiriladi → RR tushadi

Ikkalasi ham optimallashtirishga o'xshaydi, aslida **overfitting**.

Shuning uchun MAE/MFE yozish shart — kundaligimizda bu maydonlar bor.

---

## 7 ta tekshiruv savoli

Buni o'rgatayotgan odamga bering:

1. **Ochiq statistika bormi?** (Myfxbook/FXBlue — broker bilan bog'langan)
2. Necha savdoda? (n < 300 → xulosa yo'q)
3. **MAE/MFE ko'rsatilganmi?**
4. **Slippage hisobga olinganmi?** (kichik SL da hal qiluvchi)
5. Qaysi brokerda? (spred 0.3 va 1.3 — butunlay boshqa natija)
6. Yangilik paytida savdo qiladimi?
7. **Ketma-ket 20 zararni ko'rsatgan skrinshot bormi?**

7-savol eng qattiq. Agar strategiya haqiqiy bo'lsa, unda **albatta**
uzun zarar seriyalari bo'lgan. Ularni ko'rsatmasa — tanlab ko'rsatyapti.

---

## Mening tavsiyam

**Alohida strategiya sifatida qo'shmayman.** Sabablari:

| Sabab | Izoh |
|---|---|
| Photon'da allaqachon bor | LC-1, LC-2A aynan shu |
| Tekshirish 3-5 yil | 1000+ savdo kerak |
| Slot yeydi | −15 punkt aniqlash kuchi |
| Kichik SL = broker solig'i | real RR nominal RR dan ancha past |

**Lekin foydali qismini olamiz** — Photon backtestida kesim sifatida:

- Likvidlik olingandan keyingi kirish (LQ swept: ha/yo'q)
- SL o'lchami (< 10 pip vs ≥ 10 pip) — bu K5 kesimimiz
- MAE/MFE — har savdoda yoziladi

Shunda **qo'shimcha savdosiz** javob olamiz:
*"Kichik SL + katta RR haqiqatan yaxshiroqmi?"*

Agar backtest ko'rsatsa — 12 oydan keyin alohida strategiya qilamiz.
