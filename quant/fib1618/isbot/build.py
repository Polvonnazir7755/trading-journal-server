"""
ISBOT.html generatori — barcha statistik dalillarni bitta interaktiv
HTML sahifaga chizadi. Tashqi kutubxona YO'Q (sof SVG + vanilla JS),
shuning uchun internetsiz ham ochiladi.

Ishga tushirish:  python3 build.py
Natija:           ISBOT.html
"""
import json, os

D = json.load(open(os.path.join(os.path.dirname(__file__), 'data.json')))
INLINE = "const D=" + json.dumps(D, separators=(',', ':')) + ";"

HTML = r"""<!DOCTYPE html>
<html lang="uz">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>1.618 LEGENDA — Statistik isbotlar</title>
<style>
:root{
  --bg:#0b1020; --bg2:#121a33; --card:#151d38; --line:#243055;
  --tx:#e8edff; --dim:#8fa0c8; --acc:#5b9cff; --ok:#2fd07a;
  --bad:#ff5a6e; --warn:#ffc14d; --pur:#b07cff;
}
*{box-sizing:border-box}
body{margin:0;background:linear-gradient(180deg,#0b1020,#0d1329);
     color:var(--tx);font:15px/1.65 -apple-system,Segoe UI,Roboto,sans-serif}
.wrap{max-width:1180px;margin:0 auto;padding:28px 18px 80px}
header{text-align:center;padding:38px 0 26px;border-bottom:1px solid var(--line);margin-bottom:26px}
h1{margin:0 0 10px;font-size:30px;letter-spacing:-.4px}
h1 span{color:var(--acc)}
.sub{color:var(--dim);font-size:15px}
.badge{display:inline-block;margin-top:16px;padding:7px 18px;border-radius:20px;
   background:rgba(47,208,122,.13);border:1px solid rgba(47,208,122,.4);color:var(--ok);
   font-weight:600;font-size:14px}
nav{display:flex;gap:7px;flex-wrap:wrap;margin:22px 0 30px;justify-content:center}
nav a{color:var(--dim);text-decoration:none;font-size:12.5px;padding:6px 12px;
   border:1px solid var(--line);border-radius:16px;transition:.15s}
nav a:hover{color:var(--tx);border-color:var(--acc);background:rgba(91,156,255,.08)}
.card{background:var(--card);border:1px solid var(--line);border-radius:14px;
   padding:24px;margin:20px 0}
.card h2{margin:0 0 5px;font-size:20px;display:flex;align-items:center;gap:10px}
.num{display:inline-flex;align-items:center;justify-content:center;width:27px;height:27px;
   border-radius:8px;background:var(--acc);color:#04102b;font-size:14px;font-weight:700;flex:none}
.q{color:var(--acc);font-size:13.5px;margin:0 0 14px;font-weight:500}
.card p{margin:11px 0;color:#cdd7f5;font-size:14.5px}
.formula{background:#0a1226;border:1px solid var(--line);border-left:3px solid var(--pur);
   border-radius:8px;padding:13px 16px;font-family:ui-monospace,Consolas,monospace;
   font-size:13.5px;color:#c9d6ff;margin:14px 0;overflow-x:auto}
.take{border-left:3px solid var(--ok);background:rgba(47,208,122,.07);
   border-radius:8px;padding:13px 16px;margin:16px 0 4px;font-size:14.5px}
.take.warn{border-left-color:var(--warn);background:rgba(255,193,77,.07)}
.take.bad{border-left-color:var(--bad);background:rgba(255,90,110,.07)}
.take b{color:var(--tx)}
svg{display:block;width:100%;height:auto;margin:8px 0 4px}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:16px}
@media(max-width:820px){.grid2{grid-template-columns:1fr}}
table{width:100%;border-collapse:collapse;margin:14px 0;font-size:13.5px}
th{background:#0e1730;color:var(--dim);font-weight:600;text-align:right;
   padding:9px 11px;border-bottom:1px solid var(--line)}
th:first-child,td:first-child{text-align:left}
td{padding:9px 11px;border-bottom:1px solid #1b2444;text-align:right}
tr:last-child td{border-bottom:none}
.g{color:var(--ok);font-weight:600}.r{color:var(--bad);font-weight:600}
.y{color:var(--warn);font-weight:600}.dim{color:var(--dim)}
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:12px;margin:18px 0}
.kpi{background:#0e1730;border:1px solid var(--line);border-radius:10px;padding:14px;text-align:center}
.kpi .v{font-size:23px;font-weight:700;margin-bottom:3px}
.kpi .l{font-size:11.5px;color:var(--dim);text-transform:uppercase;letter-spacing:.4px}
.legend{display:flex;gap:16px;flex-wrap:wrap;font-size:12.5px;color:var(--dim);margin:6px 0 2px}
.legend i{display:inline-block;width:11px;height:11px;border-radius:3px;margin-right:5px;vertical-align:-1px}
.ctrl{display:flex;gap:9px;align-items:center;flex-wrap:wrap;margin:12px 0;font-size:13px;color:var(--dim)}
input[type=range]{flex:1;min-width:170px;accent-color:var(--acc)}
.chip{padding:4px 11px;border-radius:12px;background:#0e1730;border:1px solid var(--line);
   font-family:ui-monospace,monospace;font-size:12.5px;color:var(--tx)}
footer{text-align:center;color:var(--dim);font-size:12.5px;padding:36px 0 0;
   border-top:1px solid var(--line);margin-top:34px}
</style>
</head>
<body>
<div class="wrap">

<header>
  <h1>1.618 <span>LEGENDA</span> — statistik isbotlar</h1>
  <div class="sub">EURUSD M30 · 33 savdo · 8 oy · xarajat hisobga olingan · 26 test o'tkazilgan</div>
  <div class="badge">P(edge haqiqiy) = 85% · kutilgan daromad ~27.5%/yil</div>
</header>

<nav>
  <a href="#s1">1 · Equity</a><a href="#s2">2 · Drawdown</a>
  <a href="#s3">3 · t-statistika</a><a href="#s4">4 · Bonferroni</a>
  <a href="#s5">5 · Ekstremal qiymat</a><a href="#s6">6 · Bayes</a>
  <a href="#s7">7 · Pivot</a><a href="#s8">8 · Monte-Carlo</a>
  <a href="#s9">9 · Ishonch oralig'i</a><a href="#s10">10 · Walk-forward</a>
  <a href="#s11">11 · TP masofasi</a><a href="#s12">12 · Xarajat</a>
  <a href="#s13">13 · Risk</a><a href="#s14">14 · Tiklanish</a>
  <a href="#s15">15 · Xulosa</a>
</nav>

<!-- 1 -->
<div class="card" id="s1">
  <h2><span class="num">1</span>Equity — foyda qanday to'plangan</h2>
  <div class="q">Savol: foyda bir necha omadli savdodanmi yoki barqarormi?</div>
  <p>Vertikal o'q — jami <b>R</b> (risk birligi). 1R = bir savdodagi risk.
     Har nuqta bitta savdo. Chiziq yuqoriga barqaror ko'tarilsa — edge bor.
     Bitta sakrash bo'lsa — omad.</p>
  <div id="c1"></div>
  <div class="legend"><span><i style="background:#5b9cff"></i>Kumulyativ R</span>
     <span><i style="background:#2fd07a"></i>Yutuq</span>
     <span><i style="background:#ff5a6e"></i>Zarar</span></div>
  <div class="take"><b>Xulosa:</b> o'sish tekis taqsimlangan, bitta savdoga bog'liq emas.
     24 yutuq / 9 zarar, eng katta yutuq jami foydaning 8% idan kam.</div>
</div>

<!-- 2 -->
<div class="card" id="s2">
  <h2><span class="num">2</span>Drawdown — og'riq chuqurligi</h2>
  <div class="q">Savol: eng yomon paytda hisob qancha tushgan?</div>
  <div class="formula">DD(t) = max(equity[0..t]) − equity[t]
Max DD = eng chuqur nuqta</div>
  <p>Bu "qancha yo'qotdim" emas — <b>"eng baxtli paytimdan qancha pastga tushdim"</b>.</p>
  <div id="c2"></div>
  <div class="kpis">
    <div class="kpi"><div class="v g">4.57%</div><div class="l">Max DD</div></div>
    <div class="kpi"><div class="v g">13.2</div><div class="l">Recovery</div></div>
    <div class="kpi"><div class="v">$47.22</div><div class="l">DD dollarda</div></div>
    <div class="kpi"><div class="v g">72.7%</div><div class="l">Win rate</div></div>
  </div>
  <div class="take"><b>Recovery factor = Net ÷ MaxDD = 13.2.</b>
     Har $1 og'riq uchun $13.2 foyda. Mezon 2.0 edi.</div>
</div>

<!-- 3 -->
<div class="card" id="s3">
  <h2><span class="num">3</span>t-statistika — natija tasodifmi?</h2>
  <div class="q">Savol: bu foyda tasodifan chiqishi mumkinmi?</div>
  <div class="formula">t = (expectancy / σ) × √n
σ = √(p(1−p)) × (W+L)   —   savdo natijalarining tarqoqligi</div>
  <p>Egri chiziq — <b>nol gipoteza</b>: agar strategiyada edge <u>bo'lmasa</u>,
     t qanday taqsimlanadi. Qizil chiziq — bizning natija.</p>
  <div id="c3"></div>
  <div class="take"><b>t = 3.81, p = 0.00014.</b>
     Ya'ni edge bo'lmasa, bunday natija <b>7000 tadan 1 marta</b> tasodifan chiqadi.</div>
</div>

<!-- 4 -->
<div class="card" id="s4">
  <h2><span class="num">4</span>Bonferroni — ko'p test jazosi</h2>
  <div class="q">Savol: 26 ta test qildik. Chegara qanchaga ko'tariladi?</div>
  <div class="formula">α_tuzatilgan = α / k = 0.05 / 26 = 0.0019
kerakli t = Φ⁻¹(1 − α/2k) = 3.10</div>
  <p>Qancha ko'p test qilsangiz, "chiroyli tasodif" topish ehtimoli shuncha yuqori.
     Bonferroni buni jazolaydi — chegarani ko'taradi.</p>
  <div id="c4"></div>
  <div class="take"><b>26 test uchun kerak t &gt; 3.10. Bizda 3.81.</b> O'tdi — lekin zaxira katta emas.
     Yana test qilsak chegara yanada ko'tariladi.</div>
</div>

<!-- 5 -->
<div class="card" id="s5">
  <h2><span class="num">5</span>Ekstremal qiymat — eng muhim tekshiruv</h2>
  <div class="q">Savol: edge <u>umuman bo'lmasa</u>, 26 testdan eng yaxshisi qanday t beradi?</div>
  <div class="formula">E[max t] ≈ √(2 ln k) − [ln ln k + ln 4π] / (2√(2 ln k))
k = 26  →  E[max t] = 1.83</div>
  <p>Bu Gumbel taqsimoti — ekstremal qiymatlar nazariyasidan.
     Sof shovqinda ham 26 tadan eng yaxshisi t≈1.83 beradi.
     <b>Bizning ortiqchamiz = 3.81 − 1.83 = 1.98.</b></p>
  <div id="c5"></div>
  <div class="take"><b>Deflated Sharpe p = 0.024.</b>
     Tanlash effekti chiqarib tashlangandan keyin ham natija ahamiyatli.</div>
</div>

<!-- 6 -->
<div class="card" id="s6">
  <h2><span class="num">6</span>Bayes — "edge bor" ehtimoli</h2>
  <div class="q">Savol: hamma dalilni ko'rgach, edge haqiqiy bo'lish ehtimoli qancha?</div>
  <div class="formula">P(edge|dalil) = P(dalil|edge)·P(edge) / P(dalil)
LR = LR₁ × LR₂ × LR₃ × LR₄</div>
  <table>
    <tr><th>Dalil</th><th>LR</th><th>Tomon</th></tr>
    <tr><td>t = 3.81 (26 test tuzatilgan)</td><td class="g">152.5×</td><td class="g">foyda</td></tr>
    <tr><td>Pivot 3/6 da PF 1.41–1.60</td><td class="r">0.43×</td><td class="r">zarar</td></tr>
    <tr><td>XAUUSD t=2.50, short −$105</td><td class="y">0.82×</td><td class="y">zarar</td></tr>
    <tr><td>Walk-forward barqaror (p=0.475)</td><td class="g">2.00×</td><td class="g">foyda</td></tr>
    <tr><td><b>Umumiy</b></td><td class="g"><b>106.9×</b></td><td></td></tr>
  </table>
  <p>Slayderni suring — boshlang'ich ishonchni (prior) o'zgartirib ko'ring:</p>
  <div class="ctrl">
    <span>Prior:</span><input type="range" id="pr" min="1" max="50" value="5">
    <span class="chip" id="prv">5%</span><span>→</span>
    <span class="chip" id="pov" style="color:#2fd07a">—</span>
  </div>
  <div id="c6"></div>
  <div class="take"><b>Skeptik prior 5% → posterior 85%.</b>
     Adabiyot: retail strategiyalarning ~5% i xarajatdan keyin foydali.</div>
</div>

<!-- 7 -->
<div class="card" id="s7">
  <h2><span class="num">7</span>Pivot — eng zaif nuqta</h2>
  <div class="q">Savol: parametr barqarormi?</div>
  <p>Ishonchli strategiyada qo'shni parametrlar ham yaxshi ishlashi kerak —
     <b>silliq tepalik</b>. Bizda esa <b>tor cho'qqi</b>.</p>
  <div id="c7"></div>
  <table>
    <tr><th>Pivot</th><th>Savdo</th><th>WR</th><th>PF</th><th>Max DD</th></tr>
    <tr><td>3</td><td>59</td><td>57.6%</td><td class="r">1.604</td><td class="r">22.5%</td></tr>
    <tr><td>4</td><td>45</td><td>77.8%</td><td class="g">3.975</td><td class="g">11.7%</td></tr>
    <tr><td><b>5</b> ← tanlangan</td><td>33</td><td>72.7%</td><td class="g">4.186</td><td class="g">11.3%</td></tr>
    <tr><td>6</td><td>31</td><td>51.6%</td><td class="r">1.413</td><td class="r">26.9%</td></tr>
  </table>
  <div class="take bad"><b>Bu overfitting belgisi.</b> PF 3 barobar tebranadi.
     Shuning uchun Bayes tahlilida bu dalil ehtimolni 0.43× ga pasaytirdi
     va kutilmalar PF 4.5 dan 1.8–2.8 ga tushirildi.</div>
</div>

<!-- 8 -->
<div class="card" id="s8">
  <h2><span class="num">8</span>Monte-Carlo — pivot farqi shovqinmi?</h2>
  <div class="q">Savol: haqiqiy PF 2.85 bo'lsa, kichik namunada u qanchalik tebranadi?</div>
  <p>30,000 marta simulyatsiya. Har safar n ta savdo, WR 60%, RR 1.9.
     <b>Edge o'zgarmas</b> — faqat tasodif ishlaydi.</p>
  <div id="c8"></div>
  <div class="legend"><span><i style="background:#ff5a6e"></i>n=33</span>
     <span><i style="background:#ffc14d"></i>n=60</span>
     <span><i style="background:#2fd07a"></i>n=120</span></div>
  <div class="take warn"><b>n=33 da PF 1.56–5.46 oralig'ida tasodifan tebranadi.</b>
     Bizning pivot diapazonimiz (1.41–4.19) aynan shu ichiga tushadi —
     demak pivot farqi ehtimol <b>sof shovqin</b>.</div>
</div>

<!-- 9 -->
<div class="card" id="s9">
  <h2><span class="num">9</span>Ishonch oralig'i — nima uchun 33 savdo kam</h2>
  <div class="q">Savol: haqiqiy win rate qayerda?</div>
  <div class="formula">CI = p ± 1.96 × √(p(1−p)/n)     kenglik ∝ 1/√n</div>
  <div id="c9"></div>
  <div class="take warn"><b>n=33 → WR 57.5%–87.9% (kenglik 30 punkt).</b>
     Haqiqiy WR 58% ham bo'lishi mumkin. Buni toraytirish uchun
     n=120 kerak — bu esa faqat vaqt bilan keladi.</div>
</div>

<!-- 10 -->
<div class="card" id="s10">
  <h2><span class="num">10</span>Walk-forward — vaqt barqarorligi</h2>
  <div class="q">Savol: strategiya davr ichida barqarormi?</div>
  <div class="formula">z = (p₁−p₂) / √(p̄(1−p̄)(1/n₁+1/n₂))
z = 0.714  →  p = 0.475</div>
  <div id="c10"></div>
  <div class="take"><b>p = 0.475 &gt; 0.05 → ikki yarim orasida statistik farq YO'Q.</b>
     Ikkalasida ham PF &gt; 3.4. Bu curve-fitting emasligining kuchli dalili —
     odatda fitting bo'lganda birinchi yarim ajoyib, ikkinchisi yomon bo'ladi.</div>
</div>

<!-- 11 -->
<div class="card" id="s11">
  <h2><span class="num">11</span>TP masofasi — win rate tuzog'i</h2>
  <div class="q">Savol: win rate'ni oshirsa bo'ladimi?</div>
  <p>Ha — TP ni yaqinlashtiring. Lekin qarang nima bo'ladi.</p>
  <div id="c11"></div>
  <div class="legend"><span><i style="background:#ffc14d"></i>Win rate %</span>
     <span><i style="background:#2fd07a"></i>Expectancy (R)</span>
     <span><i style="background:#5b9cff"></i>1.618 (hozirgi)</span></div>
  <div class="take warn"><b>WR 90% olish mumkin — lekin foyda 3 barobar kamayadi.</b>
     Edge o'zgarmaydi (+23.9 punkt), faqat qayta taqsimlanadi.
     Yagona haqiqiy yaxshilash — <b>filtr</b>, TP emas.</div>
</div>

<!-- 12 -->
<div class="card" id="s12">
  <h2><span class="num">12</span>Xarajat — SL masofasiga bog'liqlik</h2>
  <div class="q">Savol: spred va komissiya qancha yeydi?</div>
  <div class="formula">xarajat_R = jami_pip / SL_pip     (bizda 2.1 pip)</div>
  <div id="c12"></div>
  <div class="take"><b>SL kichik bo'lsa xarajat ulushi katta.</b>
     Aynan shuning uchun M3/M5 da strategiya ishlamaydi:
     u yerda W bo'yi 2–5 pip, xarajat 40%+ ni yeydi.</div>
</div>

<!-- 13 -->
<div class="card" id="s13">
  <h2><span class="num">13</span>Risk % — Kelly va portlash</h2>
  <div class="q">Savol: qancha risk olish kerak?</div>
  <div id="c13"></div>
  <div class="legend"><span><i style="background:#2fd07a"></i>Median natija</span>
     <span><i style="background:#ffc14d"></i>DD 95%</span>
     <span><i style="background:#ff5a6e"></i>Portlash %</span></div>
  <div class="take"><b>2% tanlandi.</b> Sizning testingiz: 5%→2% da foyda 27% tushdi,
     DD esa 59% tushdi. Har 1% DD uchun foyda 1.8× oshdi.</div>
</div>

<!-- 14 -->
<div class="card" id="s14">
  <h2><span class="num">14</span>Tiklanish assimetriyasi</h2>
  <div class="q">Savol: nega DD ni past ushlash muhim?</div>
  <div class="formula">tiklanish = 1/(1−DD) − 1</div>
  <div id="c14"></div>
  <div class="take bad"><b>50% yo'qotsangiz, nolga qaytish uchun 100% kerak.</b>
     Matematika shafqatsiz — shuning uchun DD ni past ushlash
     foydani oshirishdan muhimroq.</div>
</div>

<!-- 15 -->
<div class="card" id="s15">
  <h2><span class="num">15</span>Yakuniy xulosa</h2>
  <div class="grid2">
    <div>
      <p><b>Uch strategiya taqqoslovi</b></p>
      <div id="c15"></div>
    </div>
    <div>
      <p><b>Stsenariy taqsimoti</b></p>
      <div id="c16"></div>
    </div>
  </div>
  <div class="kpis">
    <div class="kpi"><div class="v g">85%</div><div class="l">P(edge bor)</div></div>
    <div class="kpi"><div class="v g">27.5%</div><div class="l">Kutilgan yillik</div></div>
    <div class="kpi"><div class="v y">1.8–2.8</div><div class="l">Realistik PF</div></div>
    <div class="kpi"><div class="v y">20–25%</div><div class="l">Realistik DD</div></div>
  </div>
  <table>
    <tr><th>Test</th><th>Natija</th><th>Holat</th></tr>
    <tr><td>Vaqt barqarorligi (walk-forward)</td><td>p = 0.475</td><td class="g">o'tdi</td></tr>
    <tr><td>Ikki bozor (EURUSD + XAUUSD)</td><td>ikkalasi foydali</td><td class="g">o'tdi</td></tr>
    <tr><td>Realistik xarajat (2.1 pip)</td><td>PF 4.19 saqlandi</td><td class="g">o'tdi</td></tr>
    <tr><td>Bonferroni (26 test)</td><td>t 3.81 &gt; 3.10</td><td class="g">o'tdi</td></tr>
    <tr><td>Deflated Sharpe</td><td>p = 0.024</td><td class="g">o'tdi</td></tr>
    <tr><td>Repaint / look-ahead</td><td>topilmadi</td><td class="g">o'tdi</td></tr>
    <tr><td><b>Pivot barqarorligi</b></td><td>PF 1.41–4.19</td><td class="r">o'tmadi</td></tr>
    <tr><td>Namuna hajmi</td><td>33 savdo</td><td class="y">kam</td></tr>
  </table>
  <div class="take"><b>Yakun:</b> strategiyada haqiqiy edge bo'lish ehtimoli 85%.
     Kutilgan daromad ~27.5%/yil. Zaif nuqta — parametr barqarorligi va kichik namuna.
     <b>Keyingi qadam faqat demo</b> — yangi backtest emas.</div>
  <div class="take bad"><b>Obuna haqida:</b> $500 depozitda 4 oylik kutilgan foyda ~$35,
     Essential obunasi $52. Kutilgan sof natija <b>−$10</b>.
     Obuna $600+ depozitda oqlanadi.</div>
</div>

<footer>
  1.618 LEGENDA · barcha raqamlar backtest va Monte-Carlo simulyatsiyasidan<br>
  Backtest ≠ kelajak. Demo natijasi pastroq bo'lishi kutiladi.
</footer>
</div>

<script>
__DATA__

const NS='http://www.w3.org/2000/svg';
const C={acc:'#5b9cff',ok:'#2fd07a',bad:'#ff5a6e',warn:'#ffc14d',pur:'#b07cff',
         dim:'#8fa0c8',line:'#243055',tx:'#e8edff'};
function el(t,a={}){const e=document.createElementNS(NS,t);
  for(const k in a)e.setAttribute(k,a[k]);return e;}
function svg(id,w,h){const s=el('svg',{viewBox:`0 0 ${w} ${h}`});
  document.getElementById(id).appendChild(s);return s;}
function txt(s,x,y,t,o={}){const e=el('text',{x,y,fill:o.fill||C.dim,
  'font-size':o.fs||11,'text-anchor':o.a||'start','font-weight':o.fw||400,
  'font-family':o.mono?'ui-monospace,monospace':'inherit'});
  e.textContent=t;s.appendChild(e);return e;}
function ln(s,x1,y1,x2,y2,o={}){const e=el('line',{x1,y1,x2,y2,
  stroke:o.c||C.line,'stroke-width':o.w||1,'stroke-dasharray':o.d||'none',
  opacity:o.op??1});s.appendChild(e);return e;}
function path(s,d,o={}){const e=el('path',{d,fill:o.fill||'none',
  stroke:o.c||C.acc,'stroke-width':o.w||2,opacity:o.op??1,
  'stroke-linejoin':'round','stroke-linecap':'round'});s.appendChild(e);return e;}
function rect(s,x,y,w,h,o={}){const e=el('rect',{x,y,width:Math.max(0,w),
  height:Math.max(0,h),fill:o.fill||C.acc,opacity:o.op??1,rx:o.rx??2});s.appendChild(e);return e;}
function circ(s,cx,cy,r,o={}){const e=el('circle',{cx,cy,r,
  fill:o.fill||C.acc,opacity:o.op??1});s.appendChild(e);return e;}
function grid(s,x0,y0,w,h,ny,fmt,min,max){
  for(let i=0;i<=ny;i++){const y=y0+h-h*i/ny;
    ln(s,x0,y,x0+w,y,{c:C.line,op:.45});
    txt(s,x0-7,y+3.5,fmt(min+(max-min)*i/ny),{a:'end',fs:10});}
}

/* ---------- 1. EQUITY ---------- */
(function(){
  const W=1000,H=330,P={l:52,r:18,t:18,b:32};
  const s=svg('c1',W,H),d=D.equity;
  const w=W-P.l-P.r,h=H-P.t-P.b;
  const mn=Math.min(...d),mx=Math.max(...d);
  const X=i=>P.l+w*i/(d.length-1), Y=v=>P.t+h-h*(v-mn)/(mx-mn);
  grid(s,P.l,P.t,w,h,5,v=>v.toFixed(1)+'R',mn,mx);
  let ar=`M${X(0)},${Y(mn)}`;d.forEach((v,i)=>ar+=`L${X(i)},${Y(v)}`);
  ar+=`L${X(d.length-1)},${Y(mn)}Z`;
  path(s,ar,{fill:'rgba(91,156,255,.13)',c:'none'});
  let p='';d.forEach((v,i)=>p+=(i?'L':'M')+X(i)+','+Y(v));
  path(s,p,{c:C.acc,w:2.4});
  for(let i=1;i<d.length;i++){
    const up=d[i]>d[i-1];
    circ(s,X(i),Y(d[i]),3,{fill:up?C.ok:C.bad});
  }
  txt(s,P.l,H-9,'savdo №1',{fs:10});
  txt(s,P.l+w,H-9,'savdo №33',{a:'end',fs:10});
  txt(s,P.l+w-4,P.t+14,'jami +'+d[d.length-1].toFixed(1)+'R',
      {a:'end',fs:13,fill:C.ok,fw:700});
})();

/* ---------- 2. DRAWDOWN ---------- */
(function(){
  const W=1000,H=260,P={l:52,r:18,t:18,b:30};
  const s=svg('c2',W,H),d=D.dd_curve;
  const w=W-P.l-P.r,h=H-P.t-P.b,mx=Math.max(...d,0.6);
  const X=i=>P.l+w*i/(d.length-1),Y=v=>P.t+h*v/mx;
  for(let i=0;i<=4;i++){const y=P.t+h*i/4;ln(s,P.l,y,P.l+w,y,{c:C.line,op:.45});txt(s,P.l-7,y+3.5,'-'+(mx*i/4).toFixed(1)+'R',{a:'end',fs:10});}
  let ar=`M${P.l},${P.t}`;d.forEach((v,i)=>ar+=`L${X(i)},${Y(v)}`);
  ar+=`L${X(d.length-1)},${P.t}Z`;
  path(s,ar,{fill:'rgba(255,90,110,.2)',c:'none'});
  let p='';d.forEach((v,i)=>p+=(i?'L':'M')+X(i)+','+Y(v));
  path(s,p,{c:C.bad,w:2.2});
  const mi=d.indexOf(Math.max(...d));
  circ(s,X(mi),Y(d[mi]),5,{fill:C.bad});
  txt(s,X(mi)+9,Y(d[mi])+4,'Max DD '+d[mi].toFixed(2)+'R  (4.57%)',
      {fs:12,fill:C.bad,fw:700});
  txt(s,P.l,H-8,'savdolar ketma-ketligi',{fs:10});
})();

/* ---------- 3. t-STATISTIKA ---------- */
(function(){
  const W=1000,H=300,P={l:52,r:18,t:18,b:34};
  const s=svg('c3',W,H),w=W-P.l-P.r,h=H-P.t-P.b;
  const X=t=>P.l+w*(t+4)/8, Y=y=>P.t+h-h*y/0.42;
  const N=t=>Math.exp(-t*t/2)/Math.sqrt(2*Math.PI);
  grid(s,P.l,P.t,w,h,4,v=>v.toFixed(2),0,0.42);
  let ar=`M${X(-4)},${Y(0)}`;
  for(let t=-4;t<=4;t+=.05)ar+=`L${X(t)},${Y(N(t))}`;
  ar+=`L${X(4)},${Y(0)}Z`;
  path(s,ar,{fill:'rgba(143,160,200,.13)',c:'none'});
  let p='';for(let t=-4;t<=4;t+=.05)p+=(t===-4?'M':'L')+X(t)+','+Y(N(t));
  path(s,p,{c:C.dim,w:2});
  // rad etish zonasi
  let rz=`M${X(1.96)},${Y(0)}`;
  for(let t=1.96;t<=4;t+=.03)rz+=`L${X(t)},${Y(N(t))}`;
  rz+=`L${X(4)},${Y(0)}Z`;
  path(s,rz,{fill:'rgba(255,90,110,.25)',c:'none'});
  ln(s,X(1.96),P.t,X(1.96),P.t+h,{c:C.warn,d:'4,3',w:1.5});
  txt(s,X(1.96)+5,P.t+13,'t=1.96  (p=0.05)',{fs:10.5,fill:C.warn});
  ln(s,X(3.10),P.t,X(3.10),P.t+h,{c:C.pur,d:'4,3',w:1.5});
  txt(s,X(3.10)+5,P.t+30,'t=3.10  (Bonferroni)',{fs:10.5,fill:C.pur});
  ln(s,X(3.81),P.t-2,X(3.81),P.t+h,{c:C.ok,w:2.6});
  txt(s,X(3.81)-5,P.t+13,'BIZDA t=3.81',{a:'end',fs:13,fill:C.ok,fw:700});
  for(let t=-4;t<=4;t++)txt(s,X(t),H-11,t,{a:'middle',fs:10});
  txt(s,P.l+w/2,H-1,'t-statistika  (nol gipoteza taqsimoti)',{a:'middle',fs:10.5});
})();

/* ---------- 4. BONFERRONI ---------- */
(function(){
  const W=1000,H=280,P={l:52,r:18,t:18,b:34};
  const s=svg('c4',W,H),d=D.bonf,w=W-P.l-P.r,h=H-P.t-P.b;
  const X=k=>P.l+w*(k-1)/(d.length-1), Y=v=>P.t+h-h*(v-1.5)/2.5;
  grid(s,P.l,P.t,w,h,5,v=>v.toFixed(1),1.5,4.0);
  let p='';d.forEach((v,i)=>p+=(i?'L':'M')+X(i+1)+','+Y(v));
  path(s,p,{c:C.warn,w:2.4});
  ln(s,P.l,Y(3.81),P.l+w,Y(3.81),{c:C.ok,d:'6,4',w:2});
  txt(s,P.l+w-4,Y(3.81)-7,'bizning t = 3.81',{a:'end',fs:12,fill:C.ok,fw:700});
  circ(s,X(26),Y(d[25]),6,{fill:C.bad});
  txt(s,X(26)+10,Y(d[25])+4,'26 test → kerak 3.10',{fs:12,fill:C.bad,fw:600});
  // zaxira
  rect(s,X(26)-3,Y(3.81),6,Y(d[25])-Y(3.81),{fill:C.ok,op:.25});
  [1,10,20,30,40,50].forEach(k=>txt(s,X(k),H-11,k,{a:'middle',fs:10}));
  txt(s,P.l+w/2,H-1,'testlar soni (k)',{a:'middle',fs:10.5});
})();

/* ---------- 5. EKSTREMAL QIYMAT ---------- */
(function(){
  const W=1000,H=280,P={l:52,r:18,t:18,b:34};
  const s=svg('c5',W,H),d=D.evt,w=W-P.l-P.r,h=H-P.t-P.b;
  const X=k=>P.l+w*(k-1)/(d.length-1),Y=v=>P.t+h-h*v/4.2;
  grid(s,P.l,P.t,w,h,6,v=>v.toFixed(1),0,4.2);
  let ar=`M${X(1)},${Y(0)}`;d.forEach((v,i)=>ar+=`L${X(i+1)},${Y(v)}`);
  ar+=`L${X(d.length)},${Y(0)}Z`;
  path(s,ar,{fill:'rgba(176,124,255,.15)',c:'none'});
  let p='';d.forEach((v,i)=>p+=(i?'L':'M')+X(i+1)+','+Y(v));
  path(s,p,{c:C.pur,w:2.4});
  txt(s,X(40),Y(d[39])-10,'shovqindan kutilgan max t',{a:'middle',fs:11,fill:C.pur});
  ln(s,P.l,Y(3.81),P.l+w,Y(3.81),{c:C.ok,d:'6,4',w:2});
  txt(s,P.l+w-4,Y(3.81)-7,'bizning t = 3.81',{a:'end',fs:12,fill:C.ok,fw:700});
  circ(s,X(26),Y(d[25]),6,{fill:C.warn});
  // ortiqcha
  rect(s,X(26)-4,Y(3.81),8,Y(d[25])-Y(3.81),{fill:C.ok,op:.3});
  txt(s,X(26)+12,(Y(3.81)+Y(d[25]))/2,'ortiqcha +1.98',{fs:12,fill:C.ok,fw:700});
  txt(s,X(26),Y(d[25])+18,'k=26 → 1.83',{a:'middle',fs:11,fill:C.warn});
  [1,10,20,30,40,50].forEach(k=>txt(s,X(k),H-11,k,{a:'middle',fs:10}));
  txt(s,P.l+w/2,H-1,'testlar soni (k) — Gumbel ekstremal taqsimoti',{a:'middle',fs:10.5});
})();

/* ---------- 6. BAYES ---------- */
(function(){
  const W=1000,H=300,P={l:52,r:18,t:18,b:34};
  const s=svg('c6',W,H),d=D.bayes.curve,w=W-P.l-P.r,h=H-P.t-P.b;
  const X=p=>P.l+w*p/0.5,Y=v=>P.t+h-h*v;
  grid(s,P.l,P.t,w,h,5,v=>(v*100).toFixed(0)+'%',0,1);
  let p='';d.forEach((o,i)=>p+=(i?'L':'M')+X(o.prior)+','+Y(o.post));
  path(s,p,{c:C.ok,w:2.6});
  ln(s,P.l,Y(0),P.l+w,Y(1),{c:C.dim,d:'4,4',op:.5});
  txt(s,P.l+w-4,Y(.93),'dalilsiz (prior=posterior)',{a:'end',fs:10});
  const mk=circ(s,X(.05),Y(.849),7,{fill:C.acc});
  mk.setAttribute('id','bmk');
  const lb=txt(s,X(.05)+13,Y(.849)-8,'5% → 85%',{fs:13,fill:C.acc,fw:700});
  lb.setAttribute('id','blb');
  [0,.1,.2,.3,.4,.5].forEach(v=>txt(s,X(v),H-11,(v*100)+'%',{a:'middle',fs:10}));
  txt(s,P.l+w/2,H-1,'boshlang\u2019ich ishonch (prior)',{a:'middle',fs:10.5});
  const LR=D.bayes.LR;
  document.getElementById('pr').addEventListener('input',e=>{
    const pv=+e.target.value/100, po=pv*LR/(pv*LR+(1-pv));
    document.getElementById('prv').textContent=(pv*100).toFixed(0)+'%';
    document.getElementById('pov').textContent=(po*100).toFixed(1)+'%';
    mk.setAttribute('cx',X(pv));mk.setAttribute('cy',Y(po));
    lb.setAttribute('x',X(pv)+13);lb.setAttribute('y',Y(po)-8);
    lb.textContent=(pv*100).toFixed(0)+'% → '+(po*100).toFixed(0)+'%';
  });
  document.getElementById('pov').textContent='85.0%';
})();

/* ---------- 7. PIVOT ---------- */
(function(){
  const W=1000,H=300,P={l:52,r:52,t:22,b:38};
  const s=svg('c7',W,H),d=D.pivot,w=W-P.l-P.r,h=H-P.t-P.b;
  const X=i=>P.l+w*(i+.5)/4,Y=v=>P.t+h-h*v/5;
  grid(s,P.l,P.t,w,h,5,v=>v.toFixed(1),0,5);
  // ideal (silliq) taqqoslash
  let ip='';[2.9,3.1,3.2,3.0].forEach((v,i)=>ip+=(i?'L':'M')+X(i)+','+Y(v));
  path(s,ip,{c:C.dim,w:2,d:'6,4',op:.55});
  txt(s,X(3)+8,Y(3.0),'barqaror bo\u2019lsa shunday',{fs:10.5,fill:C.dim});
  // haqiqiy
  let p='';d.pf.forEach((v,i)=>p+=(i?'L':'M')+X(i)+','+Y(v));
  path(s,p,{c:C.warn,w:3});
  d.pf.forEach((v,i)=>{
    const good=v>3;
    circ(s,X(i),Y(v),7,{fill:good?C.ok:C.bad});
    txt(s,X(i),Y(v)-15,v.toFixed(2),{a:'middle',fs:12,fill:good?C.ok:C.bad,fw:700});
    txt(s,X(i),H-19,'pivot '+d.x[i],{a:'middle',fs:11.5,
        fill:d.x[i]===5?C.acc:C.dim,fw:d.x[i]===5?700:400});
    txt(s,X(i),H-6,d.n[i]+' savdo',{a:'middle',fs:9.5});
  });
  ln(s,P.l,Y(1.5),P.l+w,Y(1.5),{c:C.bad,d:'4,3',op:.7});
  txt(s,P.l+3,Y(1.5)-5,'PF 1.5 — minimal mezon',{fs:10,fill:C.bad});
  txt(s,P.l-42,P.t-6,'Profit factor',{fs:10.5});
})();

/* ---------- 8. MONTE-CARLO ---------- */
(function(){
  const W=1000,H=310,P={l:52,r:18,t:18,b:36};
  const s=svg('c8',W,H),w=W-P.l-P.r,h=H-P.t-P.b;
  const cols={33:C.bad,60:C.warn,120:C.ok};
  let gmax=0;
  Object.values(D.mc_pf).forEach(o=>gmax=Math.max(gmax,...o.hist));
  const X=pf=>P.l+w*pf/8, Y=v=>P.t+h-h*v/gmax;
  grid(s,P.l,P.t,w,h,4,v=>'',0,gmax);
  Object.entries(D.mc_pf).forEach(([n,o])=>{
    let p='';o.hist.forEach((v,i)=>{const pf=i*0.2+0.1;
      p+=(i?'L':'M')+X(pf)+','+Y(v);});
    path(s,p,{c:cols[n],w:2.2,op:.9});
  });
  // bizning pivot diapazoni
  rect(s,X(1.41),P.t,X(4.19)-X(1.41),h,{fill:C.acc,op:.10,rx:4});
  ln(s,X(1.41),P.t,X(1.41),P.t+h,{c:C.acc,d:'4,3',op:.8});
  ln(s,X(4.19),P.t,X(4.19),P.t+h,{c:C.acc,d:'4,3',op:.8});
  txt(s,(X(1.41)+X(4.19))/2,P.t+16,'pivot 3–6 diapazoni (1.41 – 4.19)',
      {a:'middle',fs:12,fill:C.acc,fw:600});
  txt(s,(X(1.41)+X(4.19))/2,P.t+32,'tasodifiy tebranish ichida',
      {a:'middle',fs:10.5,fill:C.acc,op:.8});
  [0,1,2,3,4,5,6,7,8].forEach(v=>txt(s,X(v),H-13,v,{a:'middle',fs:10}));
  txt(s,P.l+w/2,H-2,'Profit factor  (30,000 simulyatsiya, edge O\u2019ZGARMAS)',
      {a:'middle',fs:10.5});
})();

/* ---------- 9. ISHONCH ORALIG'I ---------- */
(function(){
  const W=1000,H=290,P={l:52,r:18,t:18,b:34};
  const s=svg('c9',W,H),d=D.ci,w=W-P.l-P.r,h=H-P.t-P.b;
  const X=n=>P.l+w*(n-15)/285,Y=v=>P.t+h-h*(v-40)/60;
  grid(s,P.l,P.t,w,h,6,v=>v.toFixed(0)+'%',40,100);
  let up='',lo='';
  d.forEach((o,i)=>{up+=(i?'L':'M')+X(o.n)+','+Y(o.hi);
                    lo+=(i?'L':'M')+X(o.n)+','+Y(o.lo);});
  const band=up+'L'+X(d[d.length-1].n)+','+Y(d[d.length-1].lo)+
    d.slice().reverse().map(o=>'L'+X(o.n)+','+Y(o.lo)).join('')+'Z';
  path(s,band,{fill:'rgba(91,156,255,.16)',c:'none'});
  path(s,up,{c:C.acc,w:1.8});path(s,lo,{c:C.acc,w:1.8});
  ln(s,P.l,Y(72.7),P.l+w,Y(72.7),{c:C.ok,d:'5,4',w:1.8});
  txt(s,P.l+w-4,Y(72.7)-7,'kuzatilgan WR 72.7%',{a:'end',fs:11.5,fill:C.ok});
  [[33,'hozir'],[120,'kerak']].forEach(([n,l])=>{
    const o=d.find(x=>Math.abs(x.n-n)<3);
    ln(s,X(n),Y(o.lo),X(n),Y(o.hi),{c:C.warn,w:3});
    circ(s,X(n),Y(o.hi),4,{fill:C.warn});circ(s,X(n),Y(o.lo),4,{fill:C.warn});
    txt(s,X(n),Y(o.hi)-9,l+' n='+n,{a:'middle',fs:11,fill:C.warn,fw:600});
    txt(s,X(n),Y(o.lo)+16,(o.hi-o.lo).toFixed(0)+'p',
        {a:'middle',fs:10.5,fill:C.warn});
  });
  [15,50,100,150,200,250,300].forEach(n=>txt(s,X(n),H-11,n,{a:'middle',fs:10}));
  txt(s,P.l+w/2,H-1,'savdolar soni (n)',{a:'middle',fs:10.5});
})();

/* ---------- 10. WALK-FORWARD ---------- */
(function(){
  const W=1000,H=250,P={l:52,r:18,t:22,b:44};
  const s=svg('c10',W,H),d=D.wf,w=W-P.l-P.r,h=H-P.t-P.b;
  const gw=w/2, bw=58;
  grid(s,P.l,P.t,w,h,4,v=>v.toFixed(0)+'%',0,100);
  const Y=v=>P.t+h-h*v/100;
  d.labels.forEach((lb,i)=>{
    const cx=P.l+gw*(i+.5);
    // WR
    rect(s,cx-bw-6,Y(d.wr[i]),bw,h-(Y(d.wr[i])-P.t),{fill:C.acc,rx:4});
    txt(s,cx-bw/2-6,Y(d.wr[i])-7,d.wr[i].toFixed(1)+'%',
        {a:'middle',fs:12.5,fill:C.acc,fw:700});
    txt(s,cx-bw/2-6,H-28,'Win rate',{a:'middle',fs:10});
    // PF (0-8 shkala -> 100 ga)
    const pfv=d.pf[i]/8*100;
    rect(s,cx+6,Y(pfv),bw,h-(Y(pfv)-P.t),{fill:C.ok,rx:4});
    txt(s,cx+6+bw/2,Y(pfv)-7,d.pf[i].toFixed(2),
        {a:'middle',fs:12.5,fill:C.ok,fw:700});
    txt(s,cx+6+bw/2,H-28,'Profit factor',{a:'middle',fs:10});
    txt(s,cx,H-11,lb+'  ·  '+d.n[i]+' savdo',{a:'middle',fs:11.5,fill:C.tx});
  });
  ln(s,P.l+gw,P.t,P.l+gw,P.t+h,{c:C.line,d:'4,4'});
  txt(s,P.l+w-4,P.t+12,'z = 0.714  ·  p = 0.475  →  farq YO\u2019Q',
      {a:'end',fs:12,fill:C.ok,fw:600});
})();

/* ---------- 11. TP MASOFASI ---------- */
(function(){
  const W=1000,H=300,P={l:52,r:52,t:18,b:34};
  const s=svg('c11',W,H),d=D.tp,w=W-P.l-P.r,h=H-P.t-P.b;
  const X=rr=>P.l+w*(rr-0.5)/4.5;
  const Yw=v=>P.t+h-h*v/100, Ye=v=>P.t+h-h*v/1.6;
  grid(s,P.l,P.t,w,h,4,v=>v.toFixed(0)+'%',0,100);
  let pw='',pe='';
  d.forEach((o,i)=>{pw+=(i?'L':'M')+X(o.rr)+','+Yw(o.wr);
                    pe+=(i?'L':'M')+X(o.rr)+','+Ye(o.exp);});
  path(s,pw,{c:C.warn,w:2.6});
  path(s,pe,{c:C.ok,w:2.6});
  const cur=d.find(o=>Math.abs(o.rr-1.6)<.06);
  ln(s,X(1.6),P.t,X(1.6),P.t+h,{c:C.acc,d:'5,4',w:2});
  circ(s,X(1.6),Yw(cur.wr),6,{fill:C.warn});
  circ(s,X(1.6),Ye(cur.exp),6,{fill:C.ok});
  txt(s,X(1.6)+9,P.t+14,'1.618 — hozirgi',{fs:12,fill:C.acc,fw:600});
  txt(s,X(0.5)+6,Yw(d[0].wr)-9,'WR '+d[0].wr.toFixed(0)+'%',{fs:11,fill:C.warn});
  txt(s,X(0.5)+6,Ye(d[0].exp)+16,'exp '+d[0].exp.toFixed(2)+'R',{fs:11,fill:C.ok});
  const last=d[d.length-1];
  txt(s,X(last.rr)-6,Yw(last.wr)-9,last.wr.toFixed(0)+'%',{a:'end',fs:11,fill:C.warn});
  txt(s,X(last.rr)-6,Ye(last.exp)-9,last.exp.toFixed(2)+'R',{a:'end',fs:11,fill:C.ok});
  [0.5,1,1.5,2,2.5,3,3.5,4,4.5,5].forEach(v=>txt(s,X(v),H-11,v,{a:'middle',fs:10}));
  txt(s,P.l+w/2,H-1,'TP masofasi (R)',{a:'middle',fs:10.5});
})();

/* ---------- 12. XARAJAT ---------- */
(function(){
  const W=1000,H=260,P={l:52,r:18,t:18,b:36};
  const s=svg('c12',W,H),d=D.cost,w=W-P.l-P.r,h=H-P.t-P.b;
  const X=i=>P.l+w*(i+.5)/d.length, bw=w/d.length*0.6;
  const Y=v=>P.t+h-h*v/0.25;
  grid(s,P.l,P.t,w,h,5,v=>(v*100).toFixed(0)+'%',0,0.25);
  d.forEach((o,i)=>{
    const bad=o.cost_r>0.10;
    rect(s,X(i)-bw/2,Y(o.cost_r),bw,P.t+h-Y(o.cost_r),
      {fill:bad?C.bad:(o.cost_r>0.06?C.warn:C.ok),rx:3});
    txt(s,X(i),Y(o.cost_r)-6,(o.cost_r*100).toFixed(1)+'%',
      {a:'middle',fs:10.5,fill:bad?C.bad:C.dim});
    txt(s,X(i),H-19,o.sl,{a:'middle',fs:10.5});
  });
  txt(s,P.l+w/2,H-4,'SL masofasi (pip)  —  xarajat 2.1 pip',{a:'middle',fs:10.5});
  txt(s,P.l-44,P.t-5,'xarajat / R',{fs:10.5});
})();

/* ---------- 13. RISK ---------- */
(function(){
  const W=1000,H=300,P={l:52,r:52,t:18,b:36};
  const s=svg('c13',W,H),d=D.risk,w=W-P.l-P.r,h=H-P.t-P.b;
  const X=i=>P.l+w*(i+.5)/d.length;
  const Yd=v=>P.t+h-h*v/100;
  grid(s,P.l,P.t,w,h,5,v=>v.toFixed(0)+'%',0,100);
  // DD 95%
  let pd='';d.forEach((o,i)=>pd+=(i?'L':'M')+X(i)+','+Yd(o.dd95));
  path(s,pd,{c:C.warn,w:2.6});
  // ruin
  let pr='';d.forEach((o,i)=>pr+=(i?'L':'M')+X(i)+','+Yd(o.ruin));
  path(s,pr,{c:C.bad,w:2.6});
  // median (log shkala -> 0-100 normallash)
  const lmax=Math.log10(Math.max(...d.map(o=>o.med||1)));
  let pm='';d.forEach((o,i)=>{const v=Math.log10(Math.max(o.med,1))/lmax*100;
    pm+=(i?'L':'M')+X(i)+','+Yd(v);});
  path(s,pm,{c:C.ok,w:2.2,d:'5,4'});
  d.forEach((o,i)=>{
    circ(s,X(i),Yd(o.dd95),4,{fill:C.warn});
    txt(s,X(i),H-19,o.risk+'%',{a:'middle',fs:10.5,
      fill:o.risk===2?C.acc:C.dim,fw:o.risk===2?700:400});
  });
  const i2=d.findIndex(o=>o.risk===2);
  ln(s,X(i2),P.t,X(i2),P.t+h,{c:C.acc,d:'5,4',w:2});
  txt(s,X(i2)+8,P.t+14,'2% — tanlangan',{fs:12,fill:C.acc,fw:600});
  txt(s,P.l+w/2,H-4,'risk har savdoda (%)',{a:'middle',fs:10.5});
})();

/* ---------- 14. TIKLANISH ---------- */
(function(){
  const W=1000,H=280,P={l:52,r:18,t:18,b:36};
  const s=svg('c14',W,H),d=D.recov,w=W-P.l-P.r,h=H-P.t-P.b;
  const X=dd=>P.l+w*(dd-5)/80, Y=v=>P.t+h-h*Math.min(v,400)/400;
  grid(s,P.l,P.t,w,h,4,v=>v.toFixed(0)+'%',0,400);
  let ar=`M${X(5)},${Y(0)}`;d.forEach(o=>ar+=`L${X(o.dd)},${Y(o.need)}`);
  ar+=`L${X(85)},${Y(0)}Z`;
  path(s,ar,{fill:'rgba(255,90,110,.15)',c:'none'});
  let p='';d.forEach((o,i)=>p+=(i?'L':'M')+X(o.dd)+','+Y(o.need));
  path(s,p,{c:C.bad,w:2.8});
  // teng chiziq
  let eq='';d.forEach((o,i)=>eq+=(i?'L':'M')+X(o.dd)+','+Y(o.dd));
  path(s,eq,{c:C.dim,w:1.5,d:'5,4',op:.6});
  txt(s,X(70),Y(70)+16,'agar simmetrik bo\u2019lsa',{fs:10.5,fill:C.dim});
  [[10,'11%'],[25,'33%'],[50,'100%'],[80,'400%']].forEach(([dd,l])=>{
    const o=d.find(x=>x.dd===dd);
    circ(s,X(dd),Y(o.need),5.5,{fill:dd>=50?C.bad:C.warn});
    txt(s,X(dd)+9,Y(o.need)-6,dd+'% → '+l,
      {fs:12,fill:dd>=50?C.bad:C.warn,fw:700});
  });
  // bizning zona
  rect(s,X(5),P.t,X(25)-X(5),h,{fill:C.ok,op:.08,rx:4});
  txt(s,(X(5)+X(25))/2,P.t+h-8,'bizning DD zonasi',{a:'middle',fs:10.5,fill:C.ok});
  [10,20,30,40,50,60,70,80].forEach(v=>txt(s,X(v),H-11,v+'%',{a:'middle',fs:10}));
  txt(s,P.l+w/2,H-1,'drawdown (%)',{a:'middle',fs:10.5});
})();

/* ---------- 15. STRATEGIYALAR ---------- */
(function(){
  const W=480,H=250,P={l:44,r:14,t:18,b:44};
  const s=svg('c15',W,H),d=D.strats,w=W-P.l-P.r,h=H-P.t-P.b;
  const X=i=>P.l+w*(i+.5)/3, bw=w/3*0.5;
  const Y=v=>P.t+h-h*v/4.5;
  grid(s,P.l,P.t,w,h,3,v=>v.toFixed(1),0,4.5);
  ln(s,P.l,Y(3.10),P.l+w,Y(3.10),{c:C.pur,d:'4,3',w:1.5});
  txt(s,P.l+2,Y(3.10)-5,'Bonferroni 3.10',{fs:9.5,fill:C.pur});
  d.forEach((o,i)=>{
    const col=o.verdict==='kuchli'?C.ok:(o.verdict==='zaif'?C.warn:C.bad);
    rect(s,X(i)-bw/2,Y(o.t),bw,P.t+h-Y(o.t),{fill:col,rx:4});
    txt(s,X(i),Y(o.t)-6,o.t.toFixed(2),{a:'middle',fs:12,fill:col,fw:700});
    o.name.split(' ').forEach((wd,j)=>
      txt(s,X(i),H-30+j*12,wd,{a:'middle',fs:9.5}));
  });
  txt(s,P.l-36,P.t-5,'t-stat',{fs:10});
})();

/* ---------- 16. STSENARIY ---------- */
(function(){
  const W=480,H=250,P={l:44,r:14,t:18,b:44};
  const s=svg('c16',W,H),d=D.scen,w=W-P.l-P.r,h=H-P.t-P.b;
  const X=i=>P.l+w*(i+.5)/4, bw=w/4*0.55;
  const Y=v=>P.t+h-h*v/70;
  grid(s,P.l,P.t,w,h,3,v=>v.toFixed(0)+'%',0,70);
  const cols=[C.bad,C.warn,C.acc,C.ok];
  d.forEach((o,i)=>{
    rect(s,X(i)-bw/2,Y(o.ann),bw,P.t+h-Y(o.ann),{fill:cols[i],rx:4});
    txt(s,X(i),Y(o.ann)-6,o.ann.toFixed(0)+'%',{a:'middle',fs:11.5,fill:cols[i],fw:700});
    txt(s,X(i),H-30,o.p+'%',{a:'middle',fs:11,fill:C.tx,fw:600});
    o.name.split(' ').forEach((wd,j)=>
      txt(s,X(i),H-18+j*11,wd,{a:'middle',fs:9}));
  });
  ln(s,P.l,Y(27.5),P.l+w,Y(27.5),{c:C.ok,d:'5,4',w:2});
  txt(s,P.l+w-2,Y(27.5)-6,'kutilgan 27.5%',{a:'end',fs:10.5,fill:C.ok,fw:600});
  txt(s,P.l-36,P.t-5,'yillik',{fs:10});
})();
</script>
</body>
</html>
"""

out = HTML.replace('__DATA__', INLINE)
path = os.path.join(os.path.dirname(__file__), 'ISBOT.html')
open(path, 'w', encoding='utf-8').write(out)
print(f"ISBOT.html yaratildi — {len(out):,} bayt")
print("16 ta chizma, tashqi kutubxona yo'q, internetsiz ochiladi")
