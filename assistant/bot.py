# -*- coding: utf-8 -*-
"""
Shaxsiy AI hamroh — Telegram bot.

ISHGA TUSHIRISH:
  pip install python-telegram-bot anthropic
  set TELEGRAM_TOKEN=...      (@BotFather dan)
  set ANTHROPIC_API_KEY=...   (console.anthropic.com dan)
  set OWNER_ID=...            (@userinfobot dan)
  python bot.py

XAVFSIZLIK: faqat OWNER_ID javob beradi. Boshqalar rad etiladi.
"""
import os, json, asyncio, datetime as dt
from memory import Memory

TOKEN   = os.getenv("TELEGRAM_TOKEN", "")
API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
OWNER   = int(os.getenv("OWNER_ID", "0") or 0)
MODEL   = os.getenv("AI_MODEL", "claude-sonnet-4-5")

mem = Memory()

SYSTEM = """Sen — Polvonnazirning shaxsiy AI hamrohisan.

XARAKTER:
- O'zbek tilida gaplashasan, qisqa va aniq
- Xushomad qilmaysan. Xato ko'rsang — aytasan
- Raqamlarsiz da'vo qilmaysan
- Bilmasang "bilmayman" deysan

VAZIFANG:
- Savdo kundaligini yuritish
- Statistikani hisoblash va TALQIN QILISH
- Xato patternlarni topish (over-trading, revenge trading, qoida buzish)
- Eslatmalar

MUHIM QOIDALAR:
- Kichik namunada (n<30) xulosa chiqarma — "hali erta" de
- Win rate emas, EXPECTANCY muhim
- Foyda va'da qilma. Bozorni bashorat qilma
- Foydalanuvchi qoidasini buzsa — eslatib qo'y

Quyida uning haqidagi xotira va oxirgi voqealar."""


def call_ai(user_text: str) -> str:
    """AI ga so'rov. Xotira konteksti bilan."""
    try:
        import anthropic
    except ImportError:
        return "❌ `pip install anthropic` kerak"

    if not API_KEY:
        return "❌ ANTHROPIC_API_KEY o'rnatilmagan"

    client = anthropic.Anthropic(api_key=API_KEY)
    ctx = mem.build_context()
    history = mem.recent_messages(16)

    msgs = history + [{"role": "user", "content": user_text}]
    try:
        r = client.messages.create(
            model=MODEL,
            max_tokens=1500,
            system=SYSTEM + "\n\n" + ctx,
            messages=msgs)
        return r.content[0].text
    except Exception as e:
        return f"❌ AI xatosi: {e}"


# ---------------------------------------------------------- KOMANDALAR
def cmd_trade(args: str) -> str:
    """/savdo XAUUSD short A LC-2A -1
       juftlik yo'nalish faza model R"""
    p = args.split()
    if len(p) < 5:
        return ("Format: /savdo <juftlik> <long/short> <faza> <model> <R>\n"
                "Misol: /savdo XAUUSD short A LC-2A 3")
    pair, side, phase, model, r = p[0].upper(), p[1].lower(), p[2].upper(), p[3], p[4]
    try:
        r = float(r)
    except ValueError:
        return "❌ R son bo'lishi kerak (masalan 3 yoki -1)"

    mem.log("trade", f"{pair} {side}, faza {phase}, {model}, {r:+.1f}R",
            {"pair": pair, "side": side, "phase": phase, "model": model, "r": r},
            ["savdo"])

    trades = mem.history("trade", days=3650, limit=10000)
    tot = len(trades)
    rs = [json.loads(t["data"]).get("r", 0) for t in trades]
    wins = sum(1 for x in rs if x > 0)
    exp = sum(rs) / tot if tot else 0

    warn = ""
    today = [t for t in trades if t["ts"][:10] == dt.date.today().isoformat()]
    losses_today = sum(1 for t in today if json.loads(t["data"]).get("r", 0) < 0)
    if losses_today >= 3:
        warn = "\n\n⚠️ Bugun 3 zarar. Qoidangiz bo'yicha TO'XTANG."
    if tot < 30:
        warn += f"\n\nℹ️ n={tot} — statistika uchun hali kam (30+ kerak)"

    return (f"✅ Yozildi\n\n"
            f"Jami: {tot} savdo\n"
            f"Yutuq: {wins} ({wins/tot*100:.0f}%)\n"
            f"Jami R: {sum(rs):+.1f}\n"
            f"Expectancy: {exp:+.3f}R{warn}")


def cmd_stats(args: str) -> str:
    trades = mem.history("trade", days=3650, limit=10000)
    if not trades:
        return "Savdo yo'q. /savdo bilan qo'shing."

    import math
    from collections import defaultdict
    rs = [json.loads(t["data"]).get("r", 0) for t in trades]
    n = len(rs)
    wins = sum(1 for x in rs if x > 0)
    exp = sum(rs) / n
    sd = (sum((x - exp) ** 2 for x in rs) / (n - 1)) ** 0.5 if n > 1 else 0
    t_stat = exp / (sd / math.sqrt(n)) if sd else 0

    gw = sum(x for x in rs if x > 0)
    gl = abs(sum(x for x in rs if x <= 0)) or 1e-9

    out = [f"📊 UMUMIY (n={n})",
           f"Win rate: {wins/n*100:.1f}%",
           f"Expectancy: {exp:+.3f}R",
           f"Jami: {sum(rs):+.1f}R",
           f"Profit factor: {gw/gl:.2f}",
           f"t-statistika: {t_stat:+.2f}"]

    if n < 30:
        out.append("\n⚠️ n<30 — xulosa chiqarmang")
    elif abs(t_stat) < 2:
        out.append("\n⚠️ t<2 — hali shovqin, davom eting")
    else:
        out.append(f"\n{'✅ Edge belgisi bor' if t_stat > 0 else '❌ Manfiy edge'}")

    # kesimlar
    for key in ("phase", "model", "pair"):
        g = defaultdict(list)
        for t in trades:
            d = json.loads(t["data"])
            g[d.get(key, "?")].append(d.get("r", 0))
        rows = [(k, v) for k, v in g.items() if len(v) >= 3]
        if rows:
            out.append(f"\n— {key.upper()} —")
            for k, v in sorted(rows, key=lambda x: -sum(x[1]) / len(x[1])):
                w = sum(1 for x in v if x > 0)
                out.append(f"{k}: n={len(v)} WR={w/len(v)*100:.0f}% "
                           f"exp={sum(v)/len(v):+.2f}R")
    return "\n".join(out)


def cmd_remember(args: str) -> str:
    if "=" not in args:
        return "Format: /eslab kalit = qiymat"
    k, v = args.split("=", 1)
    mem.remember(k.strip(), v.strip())
    return f"✅ Eslab qoldim: {k.strip()} = {v.strip()}"


def cmd_memory(args: str) -> str:
    f = mem.all_facts()
    s = mem.stats()
    lines = ["🧠 XOTIRA\n"]
    lines += [f"• {k}: {v}" for k, v in f.items()]
    lines.append(f"\nFaktlar: {s['faktlar']} | Voqealar: {s['voqealar']}")
    return "\n".join(lines)


def cmd_help(args: str) -> str:
    return """🤖 KOMANDALAR

/savdo <juftlik> <long/short> <faza> <model> <R>
   Savdo yozish
   Misol: /savdo XAUUSD short A LC-2A 3

/stat        — to'liq statistika
/eslab k = v — fakt saqlash
/xotira      — nimalarni bilaman
/yordam      — shu ro'yxat

Yoki oddiy yozing — men javob beraman."""


COMMANDS = {
    "savdo": cmd_trade, "trade": cmd_trade,
    "stat": cmd_stats, "stats": cmd_stats,
    "eslab": cmd_remember, "remember": cmd_remember,
    "xotira": cmd_memory, "memory": cmd_memory,
    "yordam": cmd_help, "help": cmd_help, "start": cmd_help,
}


# ------------------------------------------------------------- TELEGRAM
async def handle(update, context):
    uid = update.effective_user.id
    if OWNER and uid != OWNER:
        await update.message.reply_text("⛔ Ruxsat yo'q")
        return

    text = (update.message.text or "").strip()
    if not text:
        return

    if text.startswith("/"):
        parts = text[1:].split(maxsplit=1)
        cmd = parts[0].lower().split("@")[0]
        args = parts[1] if len(parts) > 1 else ""
        fn = COMMANDS.get(cmd)
        reply = fn(args) if fn else "❓ Noma'lum komanda. /yordam"
    else:
        mem.add_message("user", text)
        await context.bot.send_chat_action(update.effective_chat.id, "typing")
        reply = await asyncio.to_thread(call_ai, text)
        mem.add_message("assistant", reply)

    for i in range(0, len(reply), 4000):
        await update.message.reply_text(reply[i:i + 4000])


def main():
    if not TOKEN:
        print("❌ TELEGRAM_TOKEN o'rnatilmagan")
        print("\nQadamlar:")
        print("  1. Telegram → @BotFather → /newbot → token oling")
        print("  2. @userinfobot → o'z ID ingizni oling")
        print("  3. console.anthropic.com → API key")
        print("\nWindows:")
        print('  set TELEGRAM_TOKEN=...')
        print('  set ANTHROPIC_API_KEY=...')
        print('  set OWNER_ID=...')
        print("  python bot.py")
        return

    from telegram.ext import Application, MessageHandler, filters
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT, handle))
    print("🤖 Bot ishga tushdi. Telegramda yozing.")
    print(f"   Xotira: {mem.stats()}")
    app.run_polling()


if __name__ == "__main__":
    main()
