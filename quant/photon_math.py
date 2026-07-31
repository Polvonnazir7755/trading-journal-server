# -*- coding: utf-8 -*-
"""Photon plan parametrlarini matematik tekshirish."""

def breakeven_wr(rr):
    return 1.0 / (1.0 + rr)

print("="*62)
print("1) FIXED +3R uchun zarur win rate")
print("="*62)
for rr in (1, 2, 3, 4):
    print(f"  RR 1:{rr}  ->  breakeven WR = {breakeven_wr(rr)*100:5.1f}%"
          f"   (foyda uchun kerak: >{breakeven_wr(rr)*100+5:.0f}%)")

print("\n" + "="*62)
print("2) SPRED SOLIG'I — 'minimum 2 pip SL' muammosi")
print("="*62)
print(f"{'SL (pip)':>9} {'spred+slip':>11} {'xarajat/risk':>13} {'real RR (nom.3R)':>18} {'zarur WR':>10}")
for sl in (2, 5, 10, 20, 30):
    for cost in (0.8,):
        # kirish+chiqishda spred to'lanadi; sodda model: SL ga cost qo'shiladi, TPdan ayiriladi
        real_risk = sl + cost
        real_reward = sl*3 - cost
        rr_eff = real_reward / real_risk
        print(f"{sl:>9} {cost:>11.1f} {cost/sl*100:>12.0f}% {rr_eff:>18.2f} {breakeven_wr(rr_eff)*100:>9.1f}%")

print("""
  -> 2 pip SL da spred riskning 40%ini yeydi. Nominal 3R aslida ~2.1R.
  -> 20-30 pip SL da spred deyarli sezilmaydi.
  Xulosa: 'minimum 2 pip SL' - eng zaif nuqta. M15+ strukturada
  SL tabiiy ravishda kattaroq bo'lishi kerak.
""")

print("="*62)
print("3) 'Max 3 losses/day' + 0.5% risk rejimi")
print("="*62)
worst_day = 3 * 0.5
print(f"  Eng yomon kun: -{worst_day:.1f}%")
print(f"  Ketma-ket 10 yomon kun: -{(1-(1-worst_day/100)**10)*100:.1f}%")
print("  -> Juda konservativ. Bu PLYUS: hisobni tez kuydirmaydi.")
print("  -> Minus: statistik ma'noli namuna to'plash sekin kechadi.")

print("\n" + "="*62)
print("4) Necha savdo kerak? (edge haqiqiy ekanini bilish uchun)")
print("="*62)
print("  Statistik qoida: p<0.05 ishonch uchun taxminan")
print(f"{'WR farqi':>12} {'kerakli savdo soni':>22}")
for wr, be in ((0.30, 0.25), (0.35, 0.25), (0.40, 0.25), (0.45, 0.25)):
    # sodda normal approx: n ~ (z^2 * p(1-p)) / (p-be)^2
    z = 1.96
    n = (z**2 * wr*(1-wr)) / (wr-be)**2
    print(f"  {wr*100:>4.0f}% vs {be*100:.0f}%  {n:>18.0f} ta savdo")
print("""
  -> Kuniga 1-2 savdo bo'lsa, bu 6 oy - 2 yil demakdir.
  -> 30-50 savdodan keyin 'ishlayapti' degan xulosa = ILLYUZIYA.
""")
