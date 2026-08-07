# Shaxsiy AI hamroh — 1-bosqich

E.D.I.T.H. emas, lekin **haqiqiy** va bugun ishlaydi.

---

## Nima qiladi

- **Sizni eslaydi** — ism, broker, strategiya, qoidalar, maqsadlar
- **Savdolarni yozadi** — Telegram orqali, 10 soniyada
- **Statistika hisoblaydi** — expectancy, t-stat, faza/model kesimlari
- **Ogohlantiradi** — "bugun 3 zarar, qoidangiz bo'yicha to'xtang"
- **Suhbatlashadi** — kontekstni bilgan holda

---

## O'rnatish (15 daqiqa)

### 1. Kutubxonalar
```
pip install python-telegram-bot anthropic
```

### 2. Telegram bot yarating
- Telegramda **@BotFather** ni toping
- `/newbot` → nom bering → **tokenni** oling

### 3. O'z ID ingizni oling
- **@userinfobot** ga yozing → raqamni oling

### 4. AI kalit
- console.anthropic.com → API Keys → yangi kalit
- (yoki OpenAI ishlatish uchun kodda `call_ai` ni o'zgartiring)

### 5. Ishga tushiring

**Windows (PowerShell):**
```powershell
$env:TELEGRAM_TOKEN="123456:ABC..."
$env:ANTHROPIC_API_KEY="sk-ant-..."
$env:OWNER_ID="123456789"
python bot.py
```

**Doimiy ishlashi uchun** — `.bat` fayl yarating:
```bat
@echo off
set TELEGRAM_TOKEN=123456:ABC...
set ANTHROPIC_API_KEY=sk-ant-...
set OWNER_ID=123456789
python bot.py
pause
```

---

## Komandalar

| Komanda | Nima qiladi |
|---|---|
| `/savdo XAUUSD short A LC-2A 3` | Savdo yozish |
| `/stat` | To'liq statistika + kesimlar |
| `/eslab broker = Exness` | Fakt saqlash |
| `/xotira` | Nimalarni bilaman |
| `/yordam` | Ro'yxat |

Komandasiz yozsangiz — AI javob beradi, xotirani bilgan holda.

---

## Misol

```
Siz: /savdo XAUUSD short A LC-2A -1

Bot: ✅ Yozildi
     Jami: 23 savdo
     Yutuq: 8 (35%)
     Jami R: +4.0
     Expectancy: +0.174R
     ℹ️ n=23 — statistika uchun hali kam (30+ kerak)

Siz: nega A fazada yomon ketyapman?

Bot: Hozircha "yomon" deyish erta — A fazada 9 savdo bor,
     bu xulosa uchun kam. Lekin ko'rinayotgan narsa:
     A: n=9, WR=33%, exp=+0.11R
     B: n=14, WR=36%, exp=+0.21R
     Farq bor, lekin tasodif bo'lishi mumkin.
     Kamida 30 tadan yig'ing.
```

---

## Xavfsizlik

- Faqat `OWNER_ID` javob oladi
- API kalitlar kodda emas, muhit o'zgaruvchisida
- Ma'lumot **sizning kompyuteringizda** (`memory.db`)
- Hech qanday broker paroli saqlanmaydi

⚠️ `memory.db` ni git'ga qo'ymang — `.gitignore` da bor.

---

## Keyingi bosqichlar

| Bosqich | Nima qo'shiladi |
|---|---|
| **2** | Asboblar: kod ishga tushirish, MT5 ulanish, grafik |
| **3** | Ovoz: gapirasiz — u tushunadi va javob beradi |
| **4** | Avtonom: ertalabki hisobot, savdo yopilganda avtoyozuv |

Har bosqich alohida ishlaydi. Birinchisi bugun foyda beradi.

---

## Halol chegaralar

| Filmda | Haqiqatda |
|---|---|
| Doim to'g'ri | Xato qiladi — tekshiring |
| O'zi qaror qiladi | Siz tasdiqlaysiz |
| Ongli | Yo'q — matn bashorat qiladi |
| Bozorni biladi | **Bilmaydi.** Hech kim bilmaydi |

Bu **hamkasb**, sehrgar emas. Lekin haqiqiy hamkasb.
