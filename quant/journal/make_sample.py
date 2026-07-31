# -*- coding: utf-8 -*-
"""Namuna ma'lumot yaratadi — Photon jadvalidagi ko'rinishda.
DIQQAT: bu SUN'IY ma'lumot, faqat vositani sinash uchun."""
import csv, random, datetime as dt
random.seed(7)

PHASE_EDGE = {"A": 0.34, "A2": 0.22, "B": 0.28, "C": 0.38, "D": 0.14, "RANGE": 0.18}
MODEL_EDGE = {"LC-2A": 0.05, "LC-1": 0.0, "PBL": -0.03, "EARLY": -0.05}
PROB_EDGE  = {"HIGH": 0.06, "MED": 0.0, "LOW": -0.06}
SESS       = ["LDN", "LDN_LULL", "NY"]

rows = []
d = dt.date(2025, 1, 6)
for i in range(1, 121):
    while d.weekday() >= 5:
        d += dt.timedelta(days=1)
    ph    = random.choices(list(PHASE_EDGE), weights=[25,10,18,28,8,11])[0]
    model = random.choices(list(MODEL_EDGE), weights=[60,20,12,8])[0]
    prob  = random.choices(list(PROB_EDGE),  weights=[30,50,20])[0]
    wr = max(0.05, min(0.75, PHASE_EDGE[ph] + MODEL_EDGE[model] + PROB_EDGE[prob]))
    win = random.random() < wr
    sl_pips = round(random.uniform(8, 26), 1)
    rows.append({
        "id": f"T{i:04d}",
        "date": d.isoformat(),
        "entry_time": f"{random.choice([7,8,9,12,13,14])}:{random.choice(['05','20','35','50'])}",
        "session": random.choice(SESS),
        "pair": random.choice(["EURUSD","GBPUSD"]),
        "direction": random.choice(["LONG","SHORT"]),
        "htf_bias": random.choice(["BULL","BEAR"]),
        "mtf_phase": ph,
        "probability": prob,
        "entry_model": model,
        "poi_mitigated": True,
        "poi_stacked_htf": random.random() < 0.4,
        "poi_unmitigated": random.random() < 0.6,
        "lq_swept": random.random() < 0.7,
        "well_priced": random.random() < 0.6,
        "entry_price": "", "sl_price": "", "tp_price": "",
        "sl_pips": sl_pips,
        "entry_candle_size": round(random.uniform(2, 8), 1),
        "risk_pct": 0.5,
        "exit_price": "",
        "exit_reason": "TP" if win else "SL",
        "result_r": 3.0 if win else -1.0,
        "max_r": round(random.uniform(3.0, 12.0), 2) if win else round(random.uniform(0, 1.8), 2),
        "mae_r": round(-random.uniform(0, 0.9), 2),
        "entry_news": "", "mgmt_news": "",
        "screenshot": "", "notes": "",
    })
    d += dt.timedelta(days=random.choice([1,1,2,3]))

from schema import CSV_COLUMNS
with open("trades_sample.csv", "w", newline="", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, fieldnames=CSV_COLUMNS)
    w.writeheader()
    w.writerows(rows)
print(f"trades_sample.csv yaratildi — {len(rows)} ta savdo (SUN'IY ma'lumot)")
