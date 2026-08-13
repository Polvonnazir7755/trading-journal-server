# -*- coding: utf-8 -*-
"""
Breakeven / trailing tahlili.
Model SIZNING HAQIQIY natijangizga kalibrlangan:
  123 savdo, WR 18.7%, TP 8R -> P(MFE >= 8R) = 0.187
"""
import random, math
random.seed(41)

# kalibrovka: P(MFE>=8) = 0.187  ->  exp(-8/mean)=0.187  ->  mean = 8/1.677
MEAN_MFE = 8.0 / -math.log(0.187)

def mfe():
    return -math.log(1 - random.random()) * MEAN_MFE

def run(be_at=0.0, trail=0.0, tp_r=8.0, n=123, sims=20000):
    tot=[]; dds=[]; W=B=L=0
    for _ in range(sims):
        rs=[]
        for _ in range(n):
            m = mfe()
            if m >= tp_r:
                r = tp_r
            elif trail > 0 and m > trail:
                r = max(0.0, m - trail)
            elif be_at > 0 and m >= be_at:
                r = 0.0
            else:
                r = -1.0
            rs.append(r)
        W += sum(1 for x in rs if x > 0)
        B += sum(1 for x in rs if x == 0)
        L += sum(1 for x in rs if x < 0)
        eq=peak=mdd=0.0
        for x in rs:
            eq+=x; peak=max(peak,eq); mdd=max(mdd,peak-eq)
        tot.append(sum(rs)); dds.append(mdd)
    tot.sort(); dds.sort()
    return dict(med=tot[len(tot)//2], p5=tot[int(len(tot)*0.05)],
                dd=dds[int(len(dds)*0.95)],
                w=W/sims, b=B/sims, l=L/sims)

print("="*76)
print("KALIBROVKA TEKSHIRUVI (sizning natijangizga moslashtirildi)")
print("="*76)
base = run()
print(f"  Model:  yutuq {base['w']:.0f}  zarar {base['l']:.0f}  jami {base['med']:+.1f}R  maxDD {base['dd']:.1f}R")
print(f"  Haqiqiy: yutuq 23  zarar 100  jami +24.2R  maxDD {565/20:.1f}R")
print("  -> mos keladi\n")

print("="*76)
print("1) BREAKEVEN KO'CHIRISH — TP 8R")
print("="*76)
print(f"{'BE nuqtasi':>14}{'yutuq':>7}{'BE(0)':>7}{'zarar':>7}{'jami R':>10}{'5% yomon':>10}{'maxDD':>8}{'WR%':>7}")
for be, lbl in [(0,"yo'q"), (0.8,"0.8R (10%)"), (1.6,"1.6R (20%)"),
                (2.4,"2.4R (30%)"), (4.0,"4.0R (50%)")]:
    r = run(be_at=be)
    wr = r['w']/123*100
    print(f"{lbl:>14}{r['w']:>7.0f}{r['b']:>7.0f}{r['l']:>7.0f}"
          f"{r['med']:>+10.1f}{r['p5']:>+10.1f}{r['dd']:>8.1f}{wr:>7.1f}")

print("""
  -> BE zararni kamaytiradi, LEKIN foydani ham kamaytiradi
  -> maxDD sezilarli yaxshilanadi
  -> "5% yomon" ustuni: eng yomon holatda qancha
""")

print("="*76)
print("2) TRAILING STOP — MFE dan N R orqada suriladi")
print("="*76)
print(f"{'usul':>16}{'yutuq':>7}{'BE(0)':>7}{'zarar':>7}{'jami R':>10}{'5% yomon':>10}{'maxDD':>8}")
r0 = run()
lbl0 = "yoq (asl)"
print(f"{lbl0:>16}" + f"{r0['w']:>7.0f}{r0['b']:>7.0f}{r0['l']:>7.0f}" + f"{r0['med']:>+10.1f}{r0['p5']:>+10.1f}{r0['dd']:>8.1f}")
for t in (1.0, 2.0, 3.0, 4.0):
    r = run(trail=t)
    print(f"{'Trail '+str(t)+'R':>16}{r['w']:>7.0f}{r['b']:>7.0f}{r['l']:>7.0f}"
          f"{r['med']:>+10.1f}{r['p5']:>+10.1f}{r['dd']:>8.1f}")

print("="*76)
print("3) BE + TRAILING birga")
print("="*76)
print(f"{'usul':>22}{'jami R':>10}{'5% yomon':>11}{'maxDD':>8}{'recovery':>10}")
combos = [(0,0,"Hech narsa"), (1.6,0,"BE 1.6R"), (0,2.0,"Trail 2R"),
          (1.6,3.0,"BE 1.6R + Trail 3R")]
for be,tr,lbl in combos:
    r = run(be_at=be, trail=tr)
    rec = r['med']/r['dd'] if r['dd']>0 else 0
    print(f"{lbl:>22}{r['med']:>+10.1f}{r['p5']:>+11.1f}{r['dd']:>8.1f}{rec:>10.2f}")
print("""
  recovery = jami R / maxDD.  >2.0 yaxshi, <1.0 xavfli.
""")
