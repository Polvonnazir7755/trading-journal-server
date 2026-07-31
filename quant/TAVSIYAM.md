# Mening tavsiyam — aniq strategiyalar

## Avval aniqlik kiritay

Men "ICT/SMC tasdiqlanmagan" dedim. Bu **"yomon"** degani emas.

| Daraja | Ma'nosi | Misollar |
|---|---|---|
| Tasdiqlangan | akademik adabiyotda, mustaqil takrorlangan | momentum, vaqt effektlari |
| **Tasdiqlanmagan** | **mexanizm bor, isbot yo'q** | **ICT/SMC/Photon** |
| Rad etilgan | test qilingan, ishlamagan | ko'p indikator kombinatsiyalari |
| Tekshirilmaydigan | rad etib bo'lmaydi | Gann, Fibonachchi, Elliott |

ICT/SMC **2-darajada** — bu bizning asosiy nomzodimiz bo'lishga arziydi.
Aynan shuning uchun uni sinaymiz.

---

## Tavsiya 1: Trend-following (Donchian breakout)

**Nega bu:** momentum akademik adabiyotda **eng ko'p tasdiqlangan** bozor
anomaliyasi. 1993-yildan beri o'nlab mustaqil tadqiqot, 100+ yillik
ma'lumot, turli bozorlar. Turtle Traders shu bilan ishlagan.

**Nega edge hali yo'qolmagan:** bu risk premiyasi. Trend-follower uzoq
davom etadigan drawdown'ni ko'taradi — buning evaziga mukofot oladi.
Ko'pchilik bunga chidamaydi, shuning uchun edge saqlanadi.

**Qoidalar (to'liq obyektiv):**
```
Taymfreym:  D1
Kirish LONG:   narx oxirgi 20 kunning eng yuqorisidan yuqori yopilsa
Kirish SHORT:  narx oxirgi 20 kunning eng pastidan past yopilsa
SL:            2 x ATR(20)
TP:            yo'q — trailing: 10 kunlik teskari ekstremum
Risk:          0.5% har savdo
Filtr:         yo'q (sof holicha sinaymiz)
```

**Parametri:** 3 ta (20, 2.0, 10). Juda kam — overfitting xavfi past.

**Sizning vaqtingiz:** 0 soat. Men 20 yillik ma'lumotda sinayman.

---

## Tavsiya 2: Sessiya/vaqt effekti

**Nega bu:** eng oddiy, eng ishonchli tekshiriladigan gipoteza.
Institutsional oqim aniq vaqtlarda keladi — London fixing, NY ochilishi,
opsion expiry. Bu **kuzatiladigan haqiqat**, e'tiqod emas.

**Qoidalar:**
```
Taymfreym:  M15
Kirish:     London ochilishi (07:00 UTC) dagi 1-soatlik diapazon buzilishi
SL:         diapazonning teskari tomoni
TP:         1 x diapazon kengligi
Vaqt stop:  NY yopilishida chiqish
Filtr:      yuqori ta'sirli yangilikdan 30 daqiqa oldin kirmaslik
```

**Sizning vaqtingiz:** 0 soat.

---

## Bank manipulatsiyasi — HA, qoidalarini yuboring

Men uni **alohida slot** sifatida emas, lekin baribir sinayman.
Sabab: agar u to'liq obyektiv bo'lsa, avtomatik backtest **bepul**.

### Menga aynan nima kerak

Qoidalarni shu formatda yozing:

```
1. BOZOR
   - Qaysi juftlik/aktiv?
   - Qaysi taymfreym?
   - Qaysi sessiya/vaqt?

2. KONTEKST (savdo qidirish sharti)
   - Trend qanday aniqlanadi?
   - Qaysi darajalar belgilanadi? (qanday qoida bilan)
   - Likvidlik hovuzi qanday aniqlanadi?

3. KIRISH SIGNALI (eng muhim - MAKSIMAL ANIQ)
   - Aynan nima sodir bo'lishi kerak?
   - Sham yopilishi bilanmi yoki teginish bilanmi?
   - Tasdiqlash kerakmi? Qanday?

4. STOP LOSS
   - Aynan qayerga? (necha pip / qaysi darajaning ortiga)
   - Bufer bormi?

5. TAKE PROFIT
   - Qayerga? Qismli chiqish bormi?
   - Trailing bormi?

6. FILTRLAR
   - Qachon savdo QILINMAYDI?
   - Yangilik, vaqt, volatilite cheklovlari?

7. RISK
   - Har savdoda necha %?
   - Kunlik limit bormi?
```

### Nima bo'lsa yaxshi

✅ Video darslardan yozib olgan konspektingiz
✅ PDF / matn / skrinshotlar
✅ TradingView indikator kodi (Pine) — bo'lsa eng zo'r
✅ MT4/MT5 EA yoki indikator kodi
✅ Excel kalkulyator (Gann'dagidek ochib beraman)

### Nima bo'lsa muammo

⚠️ *"Bu yerda kirish kerakligini his qilasiz"* — kodlab bo'lmaydi
⚠️ *"Tajriba bilan bilinadi"* — kodlab bo'lmaydi
⚠️ Faqat video — men ko'ra olmayman

Agar qoidalar subyektiv bo'lsa, uni Photon'ga **kesim** sifatida
qo'shamiz (LQ swept, SL o'lchami) — qo'shimcha savdosiz javob olamiz.

---

## Yakuniy tuzilma

### Asosiy nomzodlar (Bonferroni t > 2.39)

| # | Strategiya | Turi | Sizning vaqtingiz |
|---|---|---|---|
| 1 | **Photon** | diskretsion | 30 soat |
| 2 | **Trend-following** | avtomatik | 0 soat |
| 3 | **Bank manipulatsiyasi** yoki **Sessiya** | ? | qoidalarga bog'liq |

3-slot **sizning strategiyangiz uchun ochiq**. Agar qoidalari obyektiv
bo'lsa — u kiradi. Bo'lmasa — sessiya effekti kiradi.

### Benchmarklar (bepul, slot yemaydi)

- Gann Sq9 — "murakkab formula oddiydan yaxshimi?"
- Buy & hold
- Tasodifiy kirish — "umuman edge bormi?"

---

## Nega men o'zim tavsiya qilaman, lekin sizni majburlamayman

Men tavsiya qilgan strategiyalarning **akademik asosi bor** — bu ularni
kafolatlamaydi, faqat "nega edge bor?" savoliga javobi borligini bildiradi.

Lekin **sizning strategiyangiz ham sinovga arziydi**. Balki u ishlaydi.
Balki men bilmagan narsani siz bilasiz.

Yagona shart: **qoidalar aniq bo'lsin.** Aniq bo'lmasa — tekshirib
bo'lmaydi, tekshirib bo'lmasa — bu strategiya emas, umid.
