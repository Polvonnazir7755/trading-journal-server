# -*- coding: utf-8 -*-
"""
MTF dagi ENG KATTA XATO: look-ahead bias.
Yopilmagan HTF shamni ishlatish = kelajakni ko'rish = soxta foyda.
"""
import datetime as dt
from resample_demo import gen_m1, floor_time

m1 = gen_m1(2880)          # 2 kun
HTF = 240                  # H4

def htf_state_WRONG(now_idx, m1):
    """XATO: joriy (hali yopilmagan) H4 shamni ishlatadi."""
    t = m1[now_idx][0]
    key = floor_time(t, HTF)
    # shu H4 oynasidagi BARCHA M1 (kelajakdagilari ham!) ni oladi
    bars = [b for b in m1 if floor_time(b[0], HTF) == key]
    o, c = bars[0][1], bars[-1][4]
    return "BULL" if c > o else "BEAR"

def htf_state_RIGHT(now_idx, m1):
    """TO'G'RI: faqat YOPILGAN oxirgi H4 shamni ishlatadi."""
    t = m1[now_idx][0]
    cur_key = floor_time(t, HTF)
    bars = [b for b in m1[:now_idx+1] if floor_time(b[0], HTF) < cur_key]
    if not bars:
        return None
    last_key = floor_time(bars[-1][0], HTF)
    lastbars = [b for b in bars if floor_time(b[0], HTF) == last_key]
    o, c = lastbars[0][1], lastbars[-1][4]
    return "BULL" if c > o else "BEAR"

def backtest(state_fn, label):
    """Sodda test: HTF bias yo'nalishida 10 pip TP / 10 pip SL."""
    wins = losses = 0
    i = 300
    while i < len(m1) - 60:
        st = state_fn(i, m1)
        if st is None:
            i += 1; continue
        entry = m1[i][4]
        tp = entry + 0.0010 if st == "BULL" else entry - 0.0010
        sl = entry - 0.0010 if st == "BULL" else entry + 0.0010
        done = False
        for j in range(i+1, min(i+60, len(m1))):
            h, l = m1[j][2], m1[j][3]
            if st == "BULL":
                if l <= sl: losses += 1; done = True; break
                if h >= tp: wins += 1; done = True; break
            else:
                if h >= sl: losses += 1; done = True; break
                if l <= tp: wins += 1; done = True; break
        i += 60 if done else 30
    n = wins + losses
    wr = wins/n*100 if n else 0
    print(f"{label:<42} n={n:<5} WR={wr:5.1f}%  exp={wr/100*1-(1-wr/100):+.3f}R")
    return wr

print("Bir xil ma'lumot, bir xil strategiya — farq faqat HTF holatini o'qishda:\n")
w1 = backtest(htf_state_WRONG, "XATO  (yopilmagan H4 ni o'qiydi)")
w2 = backtest(htf_state_RIGHT, "TO'G'RI (faqat yopilgan H4)")
print(f"""
Farq: {w1-w2:+.1f} foiz punkt.

Bu SOF ILLYUZIYA — kod kelajakni ko'rgani uchun. Real savdoda
yopilmagan sham qanday yopilishini bilmaysiz.

Robot yozganda bu xato JUDA oson qilinadi va backtestda ajoyib
natija beradi. Jonli savdoda esa hammasi qulaydi.
""")
