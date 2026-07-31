# -*- coding: utf-8 -*-
"""
Eksportdan OLDIN ishga tushiring — muhit tayyorligini tekshiradi.
Muammo bo'lsa, nima qilish kerakligini aytadi.
"""
import sys, platform

def ok(m):   print(f"  [OK]    {m}")
def bad(m):  print(f"  [XATO]  {m}")
def warn(m): print(f"  [!]     {m}")

print("="*60)
print("MUHIT TEKSHIRUVI")
print("="*60)

problems = 0

# --- OS ---
print("\n1) Operatsion tizim")
if platform.system() == "Windows":
    ok(f"Windows {platform.release()}  ({platform.machine()})")
else:
    bad(f"{platform.system()} — MetaTrader5 paketi faqat Windows'da ishlaydi")
    problems += 1

# --- Python arxitekturasi ---
print("\n2) Python")
bits = 64 if sys.maxsize > 2**32 else 32
print(f"          versiya {sys.version.split()[0]}, {bits}-bit")
if bits == 64:
    ok("64-bit Python — MT5 terminal bilan mos")
else:
    bad("32-bit Python — 64-bit MT5 bilan ishlamaydi. 64-bit Python o'rnating")
    problems += 1

if platform.machine().upper() in ("ARM64", "AARCH64"):
    warn("ARM protsessor aniqlandi. MT5 emulyatsiyada ishlaydi —")
    warn("Python ham x64 (ARM emas) bo'lishi kerak")

# --- kutubxonalar ---
print("\n3) Kutubxonalar")
for pkg, pipname in [("MetaTrader5", "MetaTrader5"), ("pandas", "pandas")]:
    try:
        m = __import__(pkg)
        v = getattr(m, "__version__", "?")
        ok(f"{pkg} {v}")
    except ImportError:
        bad(f"{pkg} yo'q  ->  pip install {pipname}")
        problems += 1

# --- terminalga ulanish ---
print("\n4) MT5 terminal")
try:
    import MetaTrader5 as mt5
    if not mt5.initialize():
        bad(f"Ulanmadi: {mt5.last_error()}")
        print("          -> MT5 terminalni oching va hisobga kiring")
        print("          -> Tools > Options > Expert Advisors:")
        print("             'Allow algorithmic trading' yoqilgan bo'lsin")
        problems += 1
    else:
        ai = mt5.account_info()
        ti = mt5.terminal_info()
        ok(f"Ulandi: {ai.company}")
        print(f"          server  : {ai.server}")
        print(f"          hisob   : {ai.login}  ({'DEMO' if ai.trade_mode==0 else 'REAL'})")
        print(f"          balans  : {ai.balance} {ai.currency}")
        print(f"          terminal: {ti.name} build {ti.build}")

        # --- simvollarni topish ---
        print("\n5) Simvollar")
        allsym = mt5.symbols_get()
        print(f"          jami {len(allsym)} ta simvol")
        for want in ("EURUSD", "GBPUSD"):
            cands = [s.name for s in allsym if s.name.upper().startswith(want)]
            if not cands:
                bad(f"{want}: topilmadi")
                problems += 1
                continue
            name = cands[0]
            mt5.symbol_select(name, True)
            si = mt5.symbol_info(name)
            pip = 0.0001 if si.digits in (4, 5) else 0.01
            spread_pips = si.spread * si.point / pip
            ok(f"{want} -> '{name}'  spred={spread_pips:.2f} pip  digits={si.digits}")
            if spread_pips > 1.5:
                warn(f"   Spred yuqori! Raw Spread / Zero hisob tavsiya qilinadi")

            # --- tarix chuqurligi ---
            import datetime as dt
            for year in (2022, 2024):
                r = mt5.copy_rates_range(name, mt5.TIMEFRAME_M1,
                                         dt.datetime(year,1,1), dt.datetime(year,1,15))
                n = 0 if r is None else len(r)
                if n == 0:
                    warn(f"   {year}-yil M1 tarixi YO'Q — MT5 da yuklang:")
                    warn(f"      View > Symbols > {name} > Bars > M1 > Request")
                else:
                    ok(f"   {year}-yil M1: {n:,} sham mavjud")
        mt5.shutdown()
except ImportError:
    pass

print("\n" + "="*60)
if problems == 0:
    print("HAMMASI TAYYOR ✓   endi:  python export_mt5.py")
else:
    print(f"{problems} ta muammo bor — yuqoridagi ko'rsatmalarga qarang")
print("="*60)
