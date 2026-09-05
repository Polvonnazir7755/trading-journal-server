"""
1.618 LEGENDA — Demo savdo jurnali (Excel) generatori

Yaratadi: SAVDO_JURNALI.xlsx
  Varaq 1 "Savdolar"   — savdolarni yozib borish (formulalar avtomatik)
  Varaq 2 "Statistika" — WR, PF, expectancy, DD avtomatik hisoblanadi
  Varaq 3 "Taqqoslash" — backtest vs demo, qaror mezonlari

Ishga tushirish:  python3 make_journal.py
"""
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.formatting.rule import CellIsRule
from openpyxl.worksheet.datavalidation import DataValidation

# ---------- uslublar ----------
HDR_BG   = PatternFill("solid", fgColor="1F3864")
HDR_FT   = Font(color="FFFFFF", bold=True, size=10)
SUB_BG   = PatternFill("solid", fgColor="2E5C9A")
IN_BG    = PatternFill("solid", fgColor="FFF9E6")   # qo'lda kiritiladigan
CALC_BG  = PatternFill("solid", fgColor="EAF1F8")   # avtomatik
GOOD_BG  = PatternFill("solid", fgColor="C6EFCE")
BAD_BG   = PatternFill("solid", fgColor="FFC7CE")
WARN_BG  = PatternFill("solid", fgColor="FFEB9C")
THIN     = Side(style="thin", color="B0B0B0")
BOX      = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
TITLE_FT = Font(bold=True, size=13, color="1F3864")

N_ROWS = 120          # nechta savdo qatori tayyorlanadi
FIRST  = 3            # birinchi ma'lumot qatori

wb = Workbook()

# =====================================================================
#  VARAQ 1 — SAVDOLAR
# =====================================================================
ws = wb.active
ws.title = "Savdolar"

ws["A1"] = "1.618 LEGENDA — DEMO SAVDO JURNALI"
ws["A1"].font = TITLE_FT
ws.merge_cells("A1:N1")

cols = [
    ("№",              6,  "auto"),
    ("Sana",           12, "in"),
    ("Vaqt",           8,  "in"),
    ("Aktiv",          10, "in"),
    ("TF",             7,  "in"),
    ("Yo'nalish",      11, "in"),
    ("Kirish",         11, "in"),
    ("SL",             11, "in"),
    ("TP",             11, "in"),
    ("Chiqish",        11, "in"),
    ("Natija (R)",     11, "calc"),
    ("Risk $",         10, "in"),
    ("Foyda $",        11, "calc"),
    ("Izoh",           34, "in"),
]
for i, (name, w, kind) in enumerate(cols, start=1):
    c = ws.cell(row=2, column=i, value=name)
    c.fill = HDR_BG
    c.font = HDR_FT
    c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    c.border = BOX
    ws.column_dimensions[get_column_letter(i)].width = w
ws.row_dimensions[2].height = 28
ws.freeze_panes = "A3"

# ochiluvchi ro'yxatlar
dv_dir = DataValidation(type="list", formula1='"LONG,SHORT"', allow_blank=True)
dv_tf  = DataValidation(type="list", formula1='"M30,H1,H4,D"', allow_blank=True)
dv_sym = DataValidation(type="list", formula1='"EURUSD,XAUUSD,GBPUSD,US500"', allow_blank=True)
for dv in (dv_dir, dv_tf, dv_sym):
    ws.add_data_validation(dv)
dv_dir.add(f"F{FIRST}:F{FIRST+N_ROWS-1}")
dv_tf.add(f"E{FIRST}:E{FIRST+N_ROWS-1}")
dv_sym.add(f"D{FIRST}:D{FIRST+N_ROWS-1}")

for r in range(FIRST, FIRST + N_ROWS):
    # № — faqat sana kiritilganda ko'rinadi
    ws.cell(row=r, column=1, value=f'=IF(B{r}="","",COUNT($B$3:B{r}))')
    # Natija R = (chiqish-kirish)/(kirish-SL), SHORT uchun teskari
    ws.cell(row=r, column=11, value=(
        f'=IF(OR(G{r}="",H{r}="",J{r}=""),"",'
        f'IF(F{r}="LONG",(J{r}-G{r})/(G{r}-H{r}),(G{r}-J{r})/(H{r}-G{r})))'
    ))
    # Foyda $ = R * risk$
    ws.cell(row=r, column=13, value=f'=IF(OR(K{r}="",L{r}=""),"",K{r}*L{r})')

    for c in range(1, 15):
        cell = ws.cell(row=r, column=c)
        cell.border = BOX
        kind = cols[c-1][2]
        if kind == "in":
            cell.fill = IN_BG
        elif kind == "calc":
            cell.fill = CALC_BG
        if c in (7, 8, 9, 10):
            cell.number_format = "0.00000"
        if c in (11,):
            cell.number_format = "0.00"
        if c in (12, 13):
            cell.number_format = "0.00"
        if c == 2:
            cell.number_format = "DD.MM.YYYY"

# --- yordamchi ustunlar (avtomatik DD va seriya uchun) ---
helper = [("Balans $", 12), ("Cho'qqi $", 12), ("DD $", 11), ("Zarar seriya", 13)]
for j, (nm, w) in enumerate(helper):
    col = 15 + j
    c = ws.cell(row=2, column=col, value=nm)
    c.fill = PatternFill("solid", fgColor="7F7F7F")
    c.font = Font(color="FFFFFF", bold=True, size=9)
    c.alignment = Alignment(horizontal="center", wrap_text=True)
    c.border = BOX
    ws.column_dimensions[get_column_letter(col)].width = w

for r in range(FIRST, FIRST + N_ROWS):
    prev = r - 1
    # O: kumulyativ balans (faqat savdo bo'lsa)
    ws.cell(row=r, column=15, value=(
        f'=IF(M{r}="","",IF(ROW()={FIRST},M{r},N({chr(79)}{prev})+M{r}))'))
    # P: shu paytgacha eng yuqori balans
    ws.cell(row=r, column=16, value=(
        f'=IF(O{r}="","",IF(ROW()={FIRST},MAX(0,O{r}),MAX(N(P{prev}),O{r})))'))
    # Q: joriy drawdown
    ws.cell(row=r, column=17, value=f'=IF(O{r}="","",P{r}-O{r})')
    # R: ketma-ket zarar hisoblagichi
    ws.cell(row=r, column=18, value=(
        f'=IF(K{r}="","",IF(K{r}<0,IF(ROW()={FIRST},1,N(R{prev})+1),0))'))
    for col in range(15, 19):
        cc = ws.cell(row=r, column=col)
        cc.border = BOX
        cc.fill = PatternFill("solid", fgColor="F2F2F2")
        cc.number_format = "0.00" if col < 18 else "0"

# R ustuniga rang: musbat yashil, manfiy qizil
ws.conditional_formatting.add(
    f"K{FIRST}:K{FIRST+N_ROWS-1}",
    CellIsRule(operator="greaterThan", formula=["0"], fill=GOOD_BG))
ws.conditional_formatting.add(
    f"K{FIRST}:K{FIRST+N_ROWS-1}",
    CellIsRule(operator="lessThan", formula=["0"], fill=BAD_BG))

# namuna qator (ko'rsatma sifatida)
sample = ["", "2026-09-08", "14:30", "EURUSD", "M30", "LONG",
          1.16500, 1.16200, 1.16985, 1.16985, "", 20, "", "toza TP, to'siq yo'q"]
for i, v in enumerate(sample, start=1):
    if v != "":
        ws.cell(row=FIRST, column=i, value=v)

# =====================================================================
#  VARAQ 2 — STATISTIKA
# =====================================================================
st = wb.create_sheet("Statistika")
st["A1"] = "AVTOMATIK STATISTIKA"
st["A1"].font = TITLE_FT
st.merge_cells("A1:D1")
st.column_dimensions["A"].width = 30
st.column_dimensions["B"].width = 16
st.column_dimensions["C"].width = 16
st.column_dimensions["D"].width = 46

R = f"Savdolar!$K${FIRST}:$K${FIRST+N_ROWS-1}"
P = f"Savdolar!$M${FIRST}:$M${FIRST+N_ROWS-1}"

rows = [
    ("ASOSIY", None, None, None),
    ("Jami savdo",        f'=COUNT({R})', None, "Yozilgan savdolar soni"),
    ("Yutuq",             f'=COUNTIF({R},">0")', None, ""),
    ("Zarar",             f'=COUNTIF({R},"<0")', None, ""),
    ("Breakeven",         f'=COUNTIF({R},"=0")', None, ""),
    ("Win rate",          '=IF(B3=0,"",B4/B3)', "0.0%", "Backtest: 72.7%"),
    ("", None, None, None),
    ("FOYDA", None, None, None),
    ("Gross profit ($)",  f'=SUMIF({R},">0",{P})', "0.00", ""),
    ("Gross loss ($)",    f'=ABS(SUMIF({R},"<0",{P}))', "0.00", ""),
    ("Net profit ($)",    '=B10-B11', "0.00", ""),
    ("Profit factor",     '=IF(B11=0,"",B10/B11)', "0.000", "Backtest: 4.51  |  Mezon: >1.5"),
    ("", None, None, None),
    ("R BO'YICHA", None, None, None),
    ("Jami R",            f'=SUM({R})', "0.00", ""),
    ("Expectancy (R)",    '=IF(B3=0,"",B16/B3)', "0.000", "Backtest: +0.683R  |  Mezon: >0.2"),
    ("O'rtacha yutuq (R)", f'=IF(B4=0,"",SUMIF({R},">0")/B4)', "0.00", ""),
    ("O'rtacha zarar (R)", f'=IF(B5=0,"",ABS(SUMIF({R},"<0"))/B5)', "0.00", ""),
    ("avg_win/avg_loss",  '=IF(B19=0,"",B18/B19)', "0.00", "Backtest: 1.31"),
    ("Break-even WR",     '=IF(B20="","",1/(1+B20))', "0.0%", "Shundan yuqori bo'lishi kerak"),
    ("", None, None, None),
    ("RISK", None, None, None),
    ("Eng uzun zarar seriya", f'=IF(B3=0,"",MAX(Savdolar!$R${FIRST}:$R${FIRST+N_ROWS-1}))', "0", "8 ta bo'lsa TO'XTATING"),
    ("Max drawdown ($)",  f'=IF(B3=0,"",MAX(Savdolar!$Q${FIRST}:$Q${FIRST+N_ROWS-1}))', "0.00", "Avtomatik hisoblanadi"),
    ("Max DD (% balansdan)", '=IF(OR(B25="",B25=0),"",B25/(B25+B12))', "0.0%", "Mezon: <20%"),
    ("Recovery factor",   '=IF(OR(B25="",B25=0),"",B12/B25)', "0.00", "Net / MaxDD  |  Mezon: >2"),
]

r = 2
for name, formula, fmt, note in rows:
    if name and formula is None and note is None:
        c = st.cell(row=r, column=1, value=name)
        c.fill = SUB_BG
        c.font = Font(color="FFFFFF", bold=True)
        st.merge_cells(start_row=r, start_column=1, end_row=r, end_column=4)
    elif name:
        st.cell(row=r, column=1, value=name).font = Font(bold=True)
        cb = st.cell(row=r, column=2, value=formula)
        cb.fill = CALC_BG
        cb.border = BOX
        if fmt:
            cb.number_format = fmt
        st.cell(row=r, column=4, value=note).font = Font(size=9, italic=True, color="666666")
    r += 1

# mezon ranglari
st.conditional_formatting.add("B13", CellIsRule(operator="greaterThan", formula=["1.5"], fill=GOOD_BG))
st.conditional_formatting.add("B13", CellIsRule(operator="lessThan",    formula=["1.0"], fill=BAD_BG))
st.conditional_formatting.add("B17", CellIsRule(operator="greaterThan", formula=["0.2"], fill=GOOD_BG))
st.conditional_formatting.add("B17", CellIsRule(operator="lessThan",    formula=["0"],   fill=BAD_BG))
st.conditional_formatting.add("B7",  CellIsRule(operator="lessThan",    formula=["0.5"], fill=WARN_BG))

# =====================================================================
#  VARAQ 3 — TAQQOSLASH VA QAROR
# =====================================================================
cmp_ = wb.create_sheet("Taqqoslash")
cmp_["A1"] = "BACKTEST  vs  DEMO — QAROR MEZONLARI"
cmp_["A1"].font = TITLE_FT
cmp_.merge_cells("A1:E1")
for col, w in zip("ABCDE", (26, 16, 16, 16, 44)):
    cmp_.column_dimensions[col].width = w

hdr = ["Ko'rsatkich", "Backtest", "Demo", "Holat", "Izoh"]
for i, h in enumerate(hdr, start=1):
    c = cmp_.cell(row=3, column=i, value=h)
    c.fill = HDR_BG
    c.font = HDR_FT
    c.border = BOX
    c.alignment = Alignment(horizontal="center")

data = [
    ("Savdolar soni",  33,     "=Statistika!B3",  '=IF(C4="","",IF(C4>=30,"OK","kutish"))',  "30 tadan kam bo'lsa xulosa erta"),
    ("Win rate",       0.7273, "=Statistika!B7",  '=IF(C5="","",IF(C5>=0.55,"OK","past"))',  "CI: 57.5% - 87.9%"),
    ("Profit factor",  4.506,  "=Statistika!B13", '=IF(C6="","",IF(C6>=1.5,"OK","past"))',   "Mezon: >1.5"),
    ("Expectancy (R)", 0.683,  "=Statistika!B17", '=IF(C7="","",IF(C7>=0.2,"OK","past"))',   "Mezon: >0.2R"),
    ("avg_win/avg_loss", 1.31, "=Statistika!B20", '=IF(C8="","",IF(C8>=1.0,"OK","past"))',   ""),
    ("Max DD %",       0.0461, "=Statistika!B26", '=IF(C9="","",IF(C9<=0.2,"OK","YUQORI"))', "Mezon: <20%"),
    ("Recovery factor", 12.0,  "=Statistika!B27", '=IF(C10="","",IF(C10>=2,"OK","past"))',   "Mezon: >2"),
]
r = 4
for name, bt, dm, status, note in data:
    cmp_.cell(row=r, column=1, value=name).font = Font(bold=True)
    b = cmp_.cell(row=r, column=2, value=bt)
    c = cmp_.cell(row=r, column=3, value=dm)
    d = cmp_.cell(row=r, column=4, value=status)
    cmp_.cell(row=r, column=5, value=note).font = Font(size=9, italic=True, color="666666")
    for cc in (b, c, d):
        cc.border = BOX
    c.fill = CALC_BG
    if name in ("Win rate", "Max DD %"):
        b.number_format = "0.0%"
        c.number_format = "0.0%"
    else:
        b.number_format = "0.000"
        c.number_format = "0.000"
    cmp_.conditional_formatting.add(f"D{r}",
        CellIsRule(operator="equal", formula=['"OK"'], fill=GOOD_BG))
    cmp_.conditional_formatting.add(f"D{r}",
        CellIsRule(operator="notEqual", formula=['"OK"'], fill=BAD_BG))
    r += 1

# qaror bloki
r += 1
cmp_.cell(row=r, column=1, value="QAROR QOIDALARI").fill = SUB_BG
cmp_.cell(row=r, column=1).font = Font(color="FFFFFF", bold=True)
cmp_.merge_cells(start_row=r, start_column=1, end_row=r, end_column=5)
r += 1
rules = [
    ("30 savdodan keyin PF > 1.5", "REAL PULGA O'TISH mumkin ($300-500, risk 2%)"),
    ("30 savdodan keyin PF 1.0-1.5", "DAVOM ETISH, yana 30 savdo kutish"),
    ("30 savdodan keyin PF < 1.0", "TO'XTATISH — backtest aldagan"),
    ("", ""),
    ("DARHOL TO'XTATISH SHARTLARI", ""),
    ("Real DD > 25%", "Backtest chegarasidan oshdi"),
    ("Ketma-ket 8 zarar", "WR 72% da ehtimoli 0.003% — model buzilgan"),
    ("3 oy signal yo'q", "Bozor rejimi o'zgargan"),
]
for a, b in rules:
    if a and not b:
        c = cmp_.cell(row=r, column=1, value=a)
        c.font = Font(bold=True, color="C00000")
        cmp_.merge_cells(start_row=r, start_column=1, end_row=r, end_column=5)
    elif a:
        cmp_.cell(row=r, column=1, value=a).font = Font(bold=True)
        cmp_.cell(row=r, column=2, value=b)
        cmp_.merge_cells(start_row=r, start_column=2, end_row=r, end_column=5)
    r += 1

# =====================================================================
#  VARAQ 4 — QO'LLANMA
# =====================================================================
hw = wb.create_sheet("Qo'llanma")
hw["A1"] = "QANDAY ISHLATISH"
hw["A1"].font = TITLE_FT
hw.column_dimensions["A"].width = 100
lines = [
    "",
    "1) HAR SAVDODAN KEYIN 'Savdolar' varag'iga yozing:",
    "     Sana, Vaqt, Aktiv, TF, Yo'nalish (LONG/SHORT)",
    "     Kirish narxi, SL, TP, Chiqish narxi",
    "     Risk $ (masalan 2% dan $500 = $10)",
    "     Izoh — nima bo'lgani (yangilik, spred kengaygan, to'siq bor edi...)",
    "",
    "2) 'Natija (R)' va 'Foyda $' AVTOMATIK hisoblanadi — teginmang.",
    "     Sariq katakchalar = siz kiritasiz",
    "     Ko'k katakchalar   = formula, o'zi hisoblaydi",
    "",
    "3) 'Statistika' varag'i o'zi yangilanadi. Har hafta qarab turing.",
    "",
    "4) 30 savdodan keyin 'Taqqoslash' varag'iga qarang.",
    "     Hamma qator OK bo'lsa — real pulga o'tish mumkin.",
    "",
    "MUHIM: har savdoni yozing — YUTUQNI HAM, ZARARNI HAM.",
    "Faqat yutuqni yozish — o'zini aldash. Statistika buziladi.",
    "",
    "IZOH USTUNI ENG QIMMATLI. 30 savdodan keyin uni o'qib chiqing —",
    "takrorlanadigan naqsh topasiz (masalan 'yangilik paytida hamma savdo zarar').",
    "",
    "YAKUNIY SOZLAMA (TradingView):",
    "     Aktiv: EURUSD, TF: M30",
    "     Pivot: 5,  Kirish: 4-OTE 0.5-0.618",
    "     TP1: 1.618, yopish 100%",
    "     Realistik xarajat: ON, pip avtomatik: ON",
    "     Radar: OFF,  Risk: 2%",
]
for i, t in enumerate(lines, start=2):
    c = hw.cell(row=i, column=1, value=t)
    if t.startswith(("1)", "2)", "3)", "4)", "MUHIM", "IZOH", "YAKUNIY")):
        c.font = Font(bold=True, size=11)
    else:
        c.font = Font(size=10)

wb.save("SAVDO_JURNALI.xlsx")
print("Yaratildi: SAVDO_JURNALI.xlsx")
print("  Varaqlar: Savdolar / Statistika / Taqqoslash / Qo'llanma")
print(f"  {N_ROWS} ta savdo qatori tayyor, formulalar joylangan")
