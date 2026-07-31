# -*- coding: utf-8 -*-
"""
Exness MT5 dan M1 tarixni CSV ga eksport qiladi.

TALAB:
  - Windows + MT5 terminal ochiq va hisobga kirgan
  - pip install MetaTrader5 pandas

ISHLATISH:
  python export_mt5.py                       # standart: EURUSD+GBPUSD, 2022-2026
  python export_mt5.py EURUSD 2023 2026      # bitta juftlik, muayyan yillar
"""
import sys, os, datetime as dt

def main():
    try:
        import MetaTrader5 as mt5
        import pandas as pd
    except ImportError:
        print("XATO: kutubxona yo'q.  Ishga tushiring:\n  pip install MetaTrader5 pandas")
        return 1

    symbols = ["EURUSD", "GBPUSD"]
    y_from, y_to = 2022, 2026
    if len(sys.argv) > 1: symbols = [sys.argv[1].upper()]
    if len(sys.argv) > 2: y_from = int(sys.argv[2])
    if len(sys.argv) > 3: y_to   = int(sys.argv[3])

    if not mt5.initialize():
        print("XATO: MT5 ga ulanib bo'lmadi:", mt5.last_error())
        print("  -> MT5 terminalni oching va hisobga kiring")
        return 1

    info = mt5.account_info()
    print(f"Ulandi: {info.server}  |  hisob {info.login}  |  {info.company}")

    out_dir = os.path.dirname(os.path.abspath(__file__))

    for sym in symbols:
        if not mt5.symbol_select(sym, True):
            # Exness ba'zan qo'shimcha bilan nomlaydi: EURUSDm, EURUSDz
            found = None
            for s in mt5.symbols_get():
                if s.name.upper().startswith(sym):
                    found = s.name
                    break
            if not found:
                print(f"  {sym}: topilmadi, o'tkazib yuborildi")
                continue
            print(f"  {sym} -> {found} deb topildi")
            sym_real = found
            mt5.symbol_select(sym_real, True)
        else:
            sym_real = sym

        # --- spred va kontrakt ma'lumoti (backtest uchun MUHIM) ---
        si = mt5.symbol_info(sym_real)
        tick = mt5.symbol_info_tick(sym_real)
        spread_pts = si.spread
        point = si.point
        digits = si.digits
        pip = 0.0001 if digits in (4, 5) else 0.01
        spread_pips = spread_pts * point / pip
        print(f"  {sym_real}: spred={spread_pips:.2f} pip  digits={digits}  "
              f"contract={si.trade_contract_size}  swap_long={si.swap_long}")

        # --- barlarni bo'laklab tortish (MT5 limiti bor) ---
        frames = []
        for year in range(y_from, y_to + 1):
            a = dt.datetime(year, 1, 1)
            b = dt.datetime(year + 1, 1, 1)
            rates = mt5.copy_rates_range(sym_real, mt5.TIMEFRAME_M1, a, b)
            if rates is None or len(rates) == 0:
                print(f"    {year}: ma'lumot yo'q")
                continue
            df = pd.DataFrame(rates)
            frames.append(df)
            print(f"    {year}: {len(df):>8,} sham")

        if not frames:
            continue

        df = pd.concat(frames, ignore_index=True).drop_duplicates("time")
        df["time"] = pd.to_datetime(df["time"], unit="s")
        df = df.sort_values("time")
        df = df[["time", "open", "high", "low", "close", "tick_volume", "spread"]]
        df.columns = ["time", "open", "high", "low", "close", "volume", "spread_pts"]

        path = os.path.join(out_dir, f"{sym}_M1.csv")
        df.to_csv(path, index=False)
        mb = os.path.getsize(path) / 1e6
        print(f"  -> {path}  ({len(df):,} sham, {mb:.1f} MB)")
        print(f"     davr: {df['time'].iloc[0]} .. {df['time'].iloc[-1]}")

        # meta fayl — backtest xarajatlari uchun
        meta = os.path.join(out_dir, f"{sym}_meta.txt")
        with open(meta, "w") as fh:
            fh.write(f"symbol={sym_real}\ndigits={digits}\npoint={point}\n"
                     f"pip={pip}\nspread_pips_now={spread_pips:.2f}\n"
                     f"contract_size={si.trade_contract_size}\n"
                     f"swap_long={si.swap_long}\nswap_short={si.swap_short}\n"
                     f"server={info.server}\n")
        print(f"     meta: {meta}")

    mt5.shutdown()
    print("\nTayyor. CSV fayllarni menga yuboring (yoki repoga qo'ying).")
    return 0

if __name__ == "__main__":
    sys.exit(main())
