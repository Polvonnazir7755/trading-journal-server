# 3 ta strategiya — yakuniy ro'yxat

| # | Nomi | Turi | Sizning vaqtingiz | Holati |
|---|---|---|---|---|
| 1 | **Photon Trading** | diskretsion | ~30 soat | qoidalar tayyor |
| 2 | **BETA 1 + LAOL** | avtomatik (Pine) | 0 soat | kod bor, tahlil qilindi |
| 3 | **QM + FIBO + OB + IMB** | yarim-avtomatik | ~10 soat | ❓ aniqlashtirish kerak |

**Benchmarklar** (slot yemaydi): Gann Sq9, buy&hold, tasodifiy kirish

Bonferroni chegarasi: **t > 2.39** (3 ta gipoteza)

---

## Nega bu uchtasi yaxshi to'plam

| | Photon | BETA 1 | QM+FIBO |
|---|---|---|---|
| Mantiq | struktura + POI | ko'p-TF likvidlik | zona + fib |
| Kirish | diskretsion | avtomatik | qoidali |
| TF | M15–H4 | M1–H2 (25 ta!) | M1–H4 |
| TP | qat'iy 3R | SL × 8 | fib 1.618 |
| Parametr | ~10 | ~44 | ~15 |

Uchalasi ham **likvidlik/struktura** oilasidan — bu kamchilik.
Shuning uchun **benchmark** (trend-following) qo'shamiz: agar uchalasi
ham oddiy trend-following'dan yomon chiqsa, bu muhim ma'lumot.

---

## Ish tartibi

### Hozir (siz)
1. `check_setup.py` natijasini yuboring
2. XAUUSD + EURUSD M1 eksport
3. QM strategiyasi savollariga javob (`quant/qm_fibo/SPEC.md`)

### Keyin (men, ~2 hafta)
1. BETA 1 → `strategy()` versiyasi (repaintsiz)
2. QM scanner + backtest
3. Photon ko'r-rejim vositasi
4. Benchmark kodlari

### So'ng (birga, ~5 hafta)
- Siz: Photon 300 setup + QM 300 setup
- Men: BETA 1 va benchmarklarni avtomatik sinayman
