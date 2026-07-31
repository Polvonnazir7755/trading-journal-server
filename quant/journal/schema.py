# -*- coding: utf-8 -*-
"""
Photon savdo kundaligi — ustunlar sxemasi.
Photon backtest jadvali asosida, + statistik tahlil uchun qo'shimcha maydonlar.
"""
from dataclasses import dataclass, field, asdict
from typing import Optional, List

# ---- ruxsat etilgan qiymatlar (typo'ni oldini oladi) ----
SESSIONS     = ["LDN", "LDN_LULL", "NY", "ASIA", "OTHER"]
PAIRS        = ["EURUSD", "GBPUSD"]
PROBABILITY  = ["HIGH", "MED", "LOW"]
MTF_PHASES   = ["A", "A2", "B", "C", "D", "RANGE"]
ENTRY_MODELS = ["LC-1", "LC-2A", "PBL", "EARLY", "OTHER"]
DIRECTIONS   = ["LONG", "SHORT"]
HTF_BIAS     = ["BULL", "BEAR", "RANGE"]

@dataclass
class Trade:
    # --- identifikatsiya ---
    id: str
    date: str                      # YYYY-MM-DD
    entry_time: str                # HH:MM (broker vaqti)
    session: str                   # SESSIONS
    pair: str                      # PAIRS
    direction: str                 # DIRECTIONS

    # --- Photon konteksti ---
    htf_bias: str                  # HTF_BIAS
    mtf_phase: str                 # MTF_PHASES  (A/B/C/D)
    probability: str               # PROBABILITY (o'z bahoyingiz, KIRISHDAN OLDIN)
    entry_model: str               # ENTRY_MODELS (LC-1 / LC-2A ...)
    poi_mitigated: bool            # MTF POI mitigatsiya bo'lganmi?
    poi_stacked_htf: bool          # HTF zona bilan ustma-ust tushganmi?
    poi_unmitigated: bool          # POI toza (avval tegilmagan)mi?
    lq_swept: bool                 # likvidlik olindimi?
    well_priced: bool              # premium/discount bo'yicha yaxshi narxdami?

    # --- narx / o'lcham ---
    entry_price: float
    sl_price: float
    tp_price: float
    sl_pips: float                 # risk masofasi
    entry_candle_size: float       # kirish shamining o'lchami (pip)
    risk_pct: float = 0.5          # kapitalning %i

    # --- natija ---
    exit_price: Optional[float] = None
    exit_reason: str = ""          # TP / SL / MANUAL / BE / TIME
    result_r: Optional[float] = None   # yakuniy R (masalan +3.0 yoki -1.0)
    max_r: Optional[float] = None      # savdo davomida yetgan eng yuqori R (MFE)
    mae_r: Optional[float] = None      # eng chuqur minus (MAE), R da

    # --- kontekst / eslatma ---
    entry_news: str = ""           # kirish paytida yangilik bormidi
    mgmt_news: str = ""            # ushlab turishda yangilik
    screenshot: str = ""           # TradingView link
    notes: str = ""

    # --- avtomatik hisoblanadi ---
    r_multiple: Optional[float] = None
    is_win: Optional[bool] = None

    def compute(self, spread_pips: float = 0.6):
        """Xarajatni hisobga olib real R ni hisoblaydi."""
        if self.result_r is None:
            return self
        # spred solig'i: risk kattalashadi, mukofot kichrayadi
        cost_r = spread_pips / self.sl_pips if self.sl_pips else 0.0
        self.r_multiple = self.result_r - cost_r
        self.is_win = self.r_multiple > 0
        return self

    def to_dict(self):
        return asdict(self)


CSV_COLUMNS = [
    "id","date","entry_time","session","pair","direction",
    "htf_bias","mtf_phase","probability","entry_model",
    "poi_mitigated","poi_stacked_htf","poi_unmitigated","lq_swept","well_priced",
    "entry_price","sl_price","tp_price","sl_pips","entry_candle_size","risk_pct",
    "exit_price","exit_reason","result_r","max_r","mae_r",
    "entry_news","mgmt_news","screenshot","notes",
]
