# -*- coding: utf-8 -*-
"""
"6R ga bordi, keyin SL oldi" — bu qancha tez-tez uchraydi?
Model sizning haqiqiy natijangizga kalibrlangan (123 savdo, WR 18.7%, TP 8R).
"""
import random, math
random.seed(53)

MEAN = 8.0 / -math.log(0.187)   # P(MFE>=8R)=0.187

def mfe():
    return -math.log(1 - random.random()) * MEAN

print("="*74)
print("1) MFE TAQSIMOTI — narx qanchagacha borib qaytadi?")
print("="*74)
N = 200000
data = [mfe() for _ in range(N)]
print(f"{'MFE oralig i':>16}{'savdo %':>10}{'izoh':>34}")
bands = [(0,0.5,"deyarli darhol SL"),(0.5,1,"kichik harakat"),
         (1,2,"BE zonasi"),(2,4,"yaxshi harakat"),
         (4,6,"JUDA yaqin edi"),(6,8,"OG'RIQLI — 6-8R"),(8,99,"TP oldi")]
for lo,hi,note in bands:
    c = sum(1 for x in data if lo <= x < hi)
    print(f"{str(lo)+'-'+str(hi)+'R':>16}{c/N*100:>9.1f}%{note:>34}")

lost46 = sum(1 for x in data if 4 <= x < 8)
print(f"""
  -> 4R dan oshib, TP ga yetmagan: {lost46/N*100:.1f}% savdo
  -> Bu 123 savdodan ~{lost46/N*123:.0f} ta
  -> Har biri -1R o'rniga +4..7R bo'lishi mumkin edi!
""")

print("="*74)
print("2) PROFESSIONAL YECHIMLAR — solishtirish")
print("="*74)

def run(mode, p1=0.0, p2=0.0, tp=8.0, n=123, sims=20000):
    tot=[]; dds=[]; W=BE=L=0
    for _ in range(sims):
        rs=[]
        for _ in range(n):
            m = mfe()
            r = 0.0
            if mode == "none":
                r = tp if m >= tp else -1.0
            elif mode == "be":
                r = tp if m >= tp else (0.0 if m >= p1 else -1.0)
            elif mode == "trail":
                if m >= tp: r = tp
                elif m >= p1: r = max(0.0, m - p2)
                else: r = -1.0
            elif mode == "partial":
                # p1 da yarmini yopadi, qolgani TP yoki SL
                first = 0.5 * p1 if m >= p1 else 0.5 * -1.0
                second = 0.5 * tp if m >= tp else (0.5 * -1.0 if m < p1 else 0.5 * -1.0)
                r = first + second
            elif mode == "partial_be":
                # p1 da yarmini yopadi + qolganiga BE
                if m >= tp:
                    r = 0.5*p1 + 0.5*tp
                elif m >= p1:
                    r = 0.5*p1 + 0.0      # qolgani BE da chiqdi
                else:
                    r = -1.0
            elif mode == "tp_lower":
                r = p1 if m >= p1 else -1.0
            rs.append(r)
        W += sum(1 for x in rs if x > 0.01)
        BE += sum(1 for x in rs if -0.01 <= x <= 0.01)
        L += sum(1 for x in rs if x < -0.01)
        eq=peak=mdd=0.0
        for x in rs:
            eq+=x; peak=max(peak,eq); mdd=max(mdd,peak-eq)
        tot.append(sum(rs)); dds.append(mdd)
    tot.sort(); dds.sort()
    med = tot[len(tot)//2]; dd = dds[int(len(dds)*0.95)]
    return dict(med=med, p5=tot[int(len(tot)*0.05)], dd=dd,
                w=W/sims, be=BE/sims, l=L/sims,
                rec=med/dd if dd>0 else 0)

rows = [
 ("1. Hech narsa (asl)",      "none", 0, 0),
 ("2. BE @ 1.5R",             "be", 1.5, 0),
 ("3. BE @ 2.5R",             "be", 2.5, 0),
 ("4. Trail 2R (start 3R)",   "trail", 3.0, 2.0),
 ("5. Trail 3R (start 4R)",   "trail", 4.0, 3.0),
 ("6. Partial 50% @2R + BE",  "partial_be", 2.0, 0),
 ("7. Partial 50% @3R + BE",  "partial_be", 3.0, 0),
 ("8. TP ni 4R ga tushirish", "tp_lower", 4.0, 0),
 ("9. TP ni 3R ga tushirish", "tp_lower", 3.0, 0),
]
print(f"{'usul':<26}{'yutuq':>6}{'BE':>5}{'zarar':>6}{'jami R':>9}{'maxDD':>8}{'recov':>7}")
for lbl, m, a, b in rows:
    r = run(m, a, b)
    print(f"{lbl:<26}{r['w']:>6.0f}{r['be']:>5.0f}{r['l']:>6.0f}"
          f"{r['med']:>+9.1f}{r['dd']:>8.1f}{r['rec']:>7.2f}")
print("""
  recov = jami R / maxDD.  >2 yaxshi, >4 a'lo
""")
