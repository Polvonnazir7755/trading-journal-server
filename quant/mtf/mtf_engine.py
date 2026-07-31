# -*- coding: utf-8 -*-
"""
MTF dvigateli — look-ahead bias'dan HIMOYALANGAN.

Asosiy g'oya: bitta M1 oqimi, undan barcha TF quriladi.
Har qanday HTF ma'lumot faqat YOPILGAN shamdan olinadi.
"""
import datetime as dt
from dataclasses import dataclass
from typing import List, Optional, Dict

EPOCH = dt.datetime(1970, 1, 1)

TF_MINUTES = {"M1":1, "M5":5, "M15":15, "M30":30, "H1":60, "H4":240, "D1":1440}

@dataclass
class Bar:
    time: dt.datetime
    open: float
    high: float
    low: float
    close: float
    volume: float = 0.0

def floor_time(t: dt.datetime, minutes: int) -> dt.datetime:
    total = int((t - EPOCH).total_seconds() // 60)
    return EPOCH + dt.timedelta(minutes=total - (total % minutes))


class MTFEngine:
    """
    M1 shamlarni ketma-ket 'feed' qilasiz.
    Istalgan paytda closed(tf) chaqirib, FAQAT YOPILGAN shamlarni olasiz.
    Yopilmagan sham forming(tf) da alohida turadi — u bilan qaror qabul qilmang.
    """

    def __init__(self, timeframes: List[str]):
        self.tfs = {tf: TF_MINUTES[tf] for tf in timeframes}
        self._closed: Dict[str, List[Bar]] = {tf: [] for tf in timeframes}
        self._forming: Dict[str, Optional[Bar]] = {tf: None for tf in timeframes}
        self._keys: Dict[str, Optional[dt.datetime]] = {tf: None for tf in timeframes}
        self.now: Optional[dt.datetime] = None

    def feed(self, bar: Bar) -> Dict[str, bool]:
        """Bitta M1 sham qo'shadi. Qaysi TF yangi sham yopganini qaytaradi."""
        self.now = bar.time
        just_closed = {}
        for tf, mins in self.tfs.items():
            key = floor_time(bar.time, mins)
            cur = self._forming[tf]
            if self._keys[tf] is None:
                self._keys[tf] = key
                self._forming[tf] = Bar(key, bar.open, bar.high, bar.low, bar.close, bar.volume)
                just_closed[tf] = False
            elif key != self._keys[tf]:
                # oldingi sham YOPILDI
                self._closed[tf].append(cur)
                self._keys[tf] = key
                self._forming[tf] = Bar(key, bar.open, bar.high, bar.low, bar.close, bar.volume)
                just_closed[tf] = True
            else:
                cur.high = max(cur.high, bar.high)
                cur.low = min(cur.low, bar.low)
                cur.close = bar.close
                cur.volume += bar.volume
                just_closed[tf] = False
        return just_closed

    def closed(self, tf: str, n: Optional[int] = None) -> List[Bar]:
        """YOPILGAN shamlar. Qaror shu asosda qabul qilinadi."""
        bars = self._closed[tf]
        return bars[-n:] if n else bars

    def forming(self, tf: str) -> Optional[Bar]:
        """Hozir shakllanayotgan sham. DIQQAT: qaror uchun ishlatmang!"""
        return self._forming[tf]

    def last_closed(self, tf: str) -> Optional[Bar]:
        b = self._closed[tf]
        return b[-1] if b else None


# ---------- Photon uchun asosiy struktura funksiyalari ----------

def swings(bars: List[Bar], left=2, right=2):
    """Fraktal swing high/low. right>0 => tasdiqlash uchun kutish kerak."""
    highs, lows = [], []
    for i in range(left, len(bars) - right):
        w = bars[i-left:i+right+1]
        if bars[i].high == max(b.high for b in w) and \
           all(bars[i].high > b.high for b in w if b is not bars[i]):
            highs.append((i, bars[i]))
        if bars[i].low == min(b.low for b in w) and \
           all(bars[i].low < b.low for b in w if b is not bars[i]):
            lows.append((i, bars[i]))
    return highs, lows

def structure_state(bars: List[Bar], left=2, right=2):
    """Sodda BOS/CHoCH holati. Faqat YOPILGAN shamlar bilan chaqiring."""
    hi, lo = swings(bars, left, right)
    if len(hi) < 2 or len(lo) < 2:
        return dict(bias=None, last_bos=None, sh=None, sl=None)
    last_h, prev_h = hi[-1][1], hi[-2][1]
    last_l, prev_l = lo[-1][1], lo[-2][1]
    hh = last_h.high > prev_h.high
    hl = last_l.low > prev_l.low
    lh = last_h.high < prev_h.high
    ll = last_l.low < prev_l.low
    if hh and hl:   bias = "BULL"
    elif lh and ll: bias = "BEAR"
    else:           bias = "RANGE"
    return dict(bias=bias, sh=last_h.high, sl=last_l.low,
                prev_sh=prev_h.high, prev_sl=prev_l.low)

def premium_discount(sh: float, sl: float, price: float):
    """P&D: 0.5 dan yuqori = premium, past = discount."""
    if sh is None or sl is None or sh <= sl:
        return None, None
    pos = (price - sl) / (sh - sl)
    zone = "PREMIUM" if pos > 0.5 else "DISCOUNT"
    if pos > 0.79:  zone = "EXTREME_PREMIUM"
    if pos < 0.21:  zone = "EXTREME_DISCOUNT"
    return round(pos, 3), zone


if __name__ == "__main__":
    from resample_demo import gen_m1
    eng = MTFEngine(["M1", "M5", "M15", "H1", "H4"])
    raw = gen_m1(5760)   # 4 kun
    closes = {tf: 0 for tf in eng.tfs}
    for t, o, h, l, c in raw:
        jc = eng.feed(Bar(t, o, h, l, c))
        for tf, ok in jc.items():
            if ok: closes[tf] += 1

    print("Yopilgan shamlar soni:")
    for tf in eng.tfs:
        print(f"  {tf:<4} closed={len(eng.closed(tf)):<6} forming={eng.forming(tf).time}")

    print("\nHTF holati (faqat yopilgan H4 asosida):")
    st = structure_state(eng.closed("H4"))
    print("  ", st)
    price = eng.forming("M1").close
    pos, zone = premium_discount(st["sh"], st["sl"], price)
    print(f"   narx={price:.5f}  P&D pozitsiya={pos}  zona={zone}")
