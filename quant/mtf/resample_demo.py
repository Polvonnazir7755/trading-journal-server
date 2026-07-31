# -*- coding: utf-8 -*-
"""
M1 dan barcha taymfreymlarni QURISH mumkin.
Brokerdan H4/D1 tortish shart emas — hatto zararli.
"""
import datetime as dt, random
random.seed(3)

EPOCH = dt.datetime(1970, 1, 1)

def gen_m1(n=7200, start=1.08000):
    """Sun'iy M1 sham oqimi."""
    t = dt.datetime(2025, 3, 3, 0, 0)
    p = start
    out = []
    for _ in range(n):
        o = p
        c = o + random.gauss(0, 0.00012)
        h = max(o, c) + abs(random.gauss(0, 0.00005))
        l = min(o, c) - abs(random.gauss(0, 0.00005))
        out.append((t, o, h, l, c))
        p = c
        t += dt.timedelta(minutes=1)
    return out

def floor_time(t, minutes):
    """Vaqtni TF chegarasiga tushirish (epoch asosida — aniq)."""
    total = int((t - EPOCH).total_seconds() // 60)
    return EPOCH + dt.timedelta(minutes=total - (total % minutes))

def resample(m1, minutes):
    """M1 -> istalgan TF. Sham FAQAT yopilgach to'liq bo'ladi."""
    buckets, order = {}, []
    for t, o, h, l, c in m1:
        key = floor_time(t, minutes)
        if key not in buckets:
            buckets[key] = [o, h, l, c]
            order.append(key)
        else:
            b = buckets[key]
            b[1] = max(b[1], h)
            b[2] = min(b[2], l)
            b[3] = c
    return [(k, *buckets[k]) for k in order]

if __name__ == "__main__":
    m1 = gen_m1()
    print("M1 shamlar:", len(m1), " davr:", m1[0][0], "->", m1[-1][0])
    print()
    print(f"{'TF':<6}{'shamlar':>9}{'kutilgan':>10}{'birinchi':>22}{'oxirgi':>22}")
    for name, mins in [("M1",1),("M5",5),("M15",15),("M30",30),("H1",60),("H4",240),("D1",1440)]:
        r = resample(m1, mins)
        print(f"{name:<6}{len(r):>9}{len(m1)//mins:>10}{str(r[0][0]):>22}{str(r[-1][0]):>22}")

    print("""
=> Brokerda H4 yo'q bo'lsa ham muammo emas: M1 dan quriladi.
=> Aksincha, M1 dan qurish ANIQROQ — broker serveridagi H4/D1
   shamlar ba'zan to'liq emas yoki vaqt zonasi boshqacha bo'ladi.
""")
