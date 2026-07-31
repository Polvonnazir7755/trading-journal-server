# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W = 2480
HMAX = 5200
FD = "fonts/Roboto-%s.ttf"
_c = {}
def f(s, z):
    k = (s, z)
    if k not in _c: _c[k] = ImageFont.truetype(FD % s, z)
    return _c[k]

WHITE = (255,255,255)
GOLD  = (247,196,74)
GOLD2 = (255,222,130)
CYAN  = (60,214,214)
GREEN = (86,214,140)
MUTE  = (176,203,214)
DARK  = (8,26,44)

layer = Image.new("RGBA", (W, HMAX), (0,0,0,0))
d = ImageDraw.Draw(layer)

def rr(box, r, fill=None, outline=None, width=0):
    d.rounded_rectangle(box, radius=r, fill=fill, outline=outline, width=width)

def tw(s, fo, sp=0):
    w = sum(d.textlength(c, font=fo) for c in s)
    return w + sp*(len(s)-1) if sp and len(s)>1 else w

def text(xy, s, fo, fill=WHITE, anchor="la", sp=0):
    if not sp:
        d.text(xy, s, font=fo, fill=fill, anchor=anchor); return
    x, y = xy; total = tw(s, fo, sp)
    if anchor[0]=="m": x -= total/2
    elif anchor[0]=="r": x -= total
    for c in s:
        d.text((x,y), c, font=fo, fill=fill, anchor="l"+anchor[1])
        x += d.textlength(c, font=fo) + sp

M = 150
CW = W - 2*M
y = 130

# ---------- top badge ----------
bt = "DIQQAT!  YANGI  O’QUV  YILI  BOSHLANMOQDA"
bf = f("Bold", 44)
bw = tw(bt, bf, 2) + 130
bx = (W - bw)//2
rr([bx, y, bx+bw, y+108], 54, fill=(247,196,74,40), outline=(247,196,74,190), width=4)
d.ellipse([bx+46, y+42, bx+70, y+66], fill=GOLD)
text((bx+92, y+54), bt, bf, GOLD2, anchor="lm", sp=2)
y += 108 + 62

# ---------- title ----------
t1 = f("Black", 132)
text((W//2, y), "BIOLOGIYA  ·  KIMYO", t1, WHITE, anchor="ma", sp=-2)
y += 158
text((W//2, y), "O’QUV  MARKAZI", f("Black", 88), CYAN, anchor="ma", sp=7)
y += 128

# gold rule
rr([W//2-270, y, W//2+270, y+8], 4, fill=GOLD)
y += 60

text((W//2, y), "Yangi o’quv yiliga START beramiz!", f("Medium", 54), MUTE, anchor="ma")
y += 104

# ---------- group pills ----------
pills = [("NOLDAN  GURUHLAR", GREEN), ("SERTIFIKAT  GURUHLAR", GOLD)]
pf = f("Bold", 50)
widths = [tw(p, pf, 2)+110 for p,_ in pills]
tot = sum(widths) + 36
x = (W - tot)//2
for (p, col), w_ in zip(pills, widths):
    rr([x, y, x+w_, y+112], 56, fill=col+(38,), outline=col+(200,), width=4)
    text((x+w_/2, y+56), p, pf, col, anchor="mm", sp=2)
    x += w_ + 36
y += 112 + 70

# ---------- audience box ----------
bh = 330
rr([M, y, M+CW, y+bh], 40, fill=(255,255,255,20), outline=(90,150,180,110), width=3)
text((M+60, y+48), "KURSLAR  KIMLAR  UCHUN?", f("Black", 54), GOLD, sp=2)
lines = ["BMB (blok) imtihoniga tayyorlanayotgan abituriyentlar",
         "7 – 8 – 9 – 10-sinf o’quvchilari — sertifikat darajasigacha",
         "Bu yil yetarlicha ball to’play olmagan o’quvchilar"]
yy = y + 140
for ln in lines:
    d.ellipse([M+62, yy+12, M+94, yy+44], outline=GREEN, width=5)
    d.line([(M+70, yy+28),(M+77, yy+36),(M+88, yy+20)], fill=GREEN, width=6, joint="curve")
    text((M+126, yy), ln, f("Medium", 46), (225,240,247))
    yy += 62
y += bh + 80

# ---------- section header ----------
def flask(cx, cy, s, col):
    nw = max(3, int(s*0.085))
    top = cy - s*0.56
    neck = cy - s*0.16
    d.line([(cx-s*0.13, top),(cx-s*0.13, neck)], fill=col, width=nw)
    d.line([(cx+s*0.13, top),(cx+s*0.13, neck)], fill=col, width=nw)
    d.line([(cx-s*0.26, top),(cx+s*0.26, top)], fill=col, width=nw)
    body = [(cx-s*0.13, neck),(cx+s*0.13, neck),
            (cx+s*0.46, cy+s*0.42),(cx+s*0.36, cy+s*0.54),
            (cx-s*0.36, cy+s*0.54),(cx-s*0.46, cy+s*0.42)]
    d.polygon(body, outline=col)
    d.line(body+[body[0]], fill=col, width=nw, joint="curve")
    d.polygon([(cx-s*0.33, cy+s*0.13),(cx+s*0.33, cy+s*0.13),
               (cx+s*0.46, cy+s*0.42),(cx+s*0.36, cy+s*0.54),
               (cx-s*0.36, cy+s*0.54),(cx-s*0.46, cy+s*0.42)], fill=col)
    d.ellipse([cx-s*0.30, cy+s*0.24, cx-s*0.18, cy+s*0.36], fill=DARK)
    d.ellipse([cx+s*0.12, cy+s*0.30, cx+s*0.26, cy+s*0.44], fill=DARK)

def helix(cx, cy, s, col):
    import math
    w_ = int(s*0.10)
    for sgn in (1,-1):
        pts = []
        for i in range(41):
            t = i/40
            pts.append((cx + sgn*s*0.42*math.sin(t*3.14159*2.2), cy - s*0.62 + t*s*1.24))
        d.line(pts, fill=col, width=w_, joint="curve")
    for i in range(1,6):
        t = i/6
        yv = cy - s*0.62 + t*s*1.24
        xa = cx + s*0.42*math.sin(t*3.14159*2.2)
        xb = cx - s*0.42*math.sin(t*3.14159*2.2)
        d.line([(xa,yv),(xb,yv)], fill=col, width=int(w_*0.7))

def section(ytop, title, col, icon):
    rr([M, ytop, M+CW, ytop+120], 60, fill=col+(34,), outline=col+(150,), width=3)
    d.ellipse([M+16, ytop+16, M+104, ytop+104], fill=col)
    icon(M+60, ytop+60, 62, DARK)
    text((M+142, ytop+60), title, f("Black", 62), col, anchor="lm", sp=4)
    return ytop + 120 + 34

# ---------- icons for cards ----------
def ic_phone(cx, cy, s, col):
    r = s*0.5
    d.rounded_rectangle([cx-r*0.58, cy-r, cx+r*0.58, cy+r], radius=int(r*0.3), fill=col)
    d.rounded_rectangle([cx-r*0.32, cy+r*0.42, cx+r*0.32, cy+r*0.62], radius=2, fill=DARK)
def ic_tg(cx, cy, s, col):
    r = s*0.58
    d.polygon([(cx-r, cy-r*0.12),(cx+r, cy-r*0.85),(cx+r*0.26, cy+r*0.85),(cx-r*0.04, cy+r*0.14)], fill=col)
def ic_pin(cx, cy, s, col):
    r = s*0.44
    d.ellipse([cx-r, cy-r*1.2, cx+r, cy+r*0.8], fill=col)
    d.polygon([(cx-r*0.52, cy+r*0.4),(cx+r*0.52, cy+r*0.4),(cx, cy+r*1.55)], fill=col)
    d.ellipse([cx-r*0.35, cy-r*0.52, cx+r*0.35, cy+r*0.18], fill=DARK)
def ic_cal(cx, cy, s, col):
    r = s*0.5
    d.rounded_rectangle([cx-r, cy-r*0.85, cx+r, cy+r*0.9], radius=int(r*0.2), fill=col)
    d.rectangle([cx-r, cy-r*0.85, cx+r, cy-r*0.35], fill=col)
    d.line([(cx-r*0.5, cy-r*1.15),(cx-r*0.5, cy-r*0.65)], fill=col, width=int(s*0.11))
    d.line([(cx+r*0.5, cy-r*1.15),(cx+r*0.5, cy-r*0.65)], fill=col, width=int(s*0.11))
    for i in range(3):
        for j in range(2):
            d.rectangle([cx-r*0.62+i*r*0.6, cy-r*0.12+j*r*0.42,
                         cx-r*0.36+i*r*0.6, cy+r*0.10+j*r*0.42], fill=DARK)

def card(ytop, col, place, addr, when, name, phone, tg):
    ch = 350
    rr([M, ytop, M+CW, ytop+ch], 40, fill=(255,255,255,20), outline=(255,255,255,58), width=3)
    rr([M, ytop+26, M+16, ytop+ch-26], 8, fill=col)
    lx = M + 62
    # left column
    ic_pin(lx+22, ytop+62, 52, col)
    text((lx+68, ytop+62), place, f("Black", 52), WHITE, anchor="lm", sp=1)
    yy = ytop + 108
    for ln in addr:
        text((lx+68, yy), ln, f("Regular", 38), MUTE); yy += 50
    # date pill
    dpf = f("Bold", 44)
    dw = tw(when, dpf) + 116
    py = ytop + ch - 120
    rr([lx, py, lx+dw, py+86], 43, fill=GOLD+(42,), outline=GOLD+(190,), width=3)
    ic_cal(lx+50, py+43, 44, GOLD)
    text((lx+92, py+43), when, dpf, GOLD2, anchor="lm")
    # right column
    rx = M + 1230
    text((rx, ytop+50), "O’QITUVCHI", f("Bold", 34), col, sp=4)
    text((rx, ytop+96), name, f("Black", 56), WHITE, sp=1)
    d.ellipse([rx, ytop+188, rx+62, ytop+250], fill=col)
    ic_phone(rx+31, ytop+219, 36, DARK)
    text((rx+84, ytop+219), phone, f("Bold", 48), WHITE, anchor="lm")
    d.ellipse([rx, ytop+266, rx+62, ytop+328], fill=col)
    ic_tg(rx+31, ytop+297, 36, DARK)
    text((rx+84, ytop+297), tg, f("Medium", 44), CYAN, anchor="lm")
    return ytop + ch + 26

URDU = ["Urganch davlat universiteti", "(UrDU) yon tomoni"]

y = section(y, "KIMYO", GREEN, flask)
y = card(y, GREEN, "URGANCH SHAHRI", URDU, "4-avgust  ·  09:00",
         "RAXIMOV JAHONGIR", "+998 93 867 97 79", "@Jahongirrahimov_1")
y += 34

y = section(y, "BIOLOGIYA", CYAN, helix)
y = card(y, CYAN, "URGANCH SHAHRI", URDU, "5-avgust  ·  09:00",
         "IBRAGIMOV SHODLIK", "+998 94 111 16 13", "@Ibragimov_Shodlik")
y = card(y, CYAN, "SHOVOT TUMANI", ["Monoq markazi"], "6-avgustdan",
         "SHOMURATOV HURMAT", "+998 93 170 26 60", "@Shomuratov_Hurmat")
y = card(y, CYAN, "XONQA TUMANI", ["1-son texnikum", "(eski maishiy kolleji)"], "6-avgust  ·  14:00",
         "RAXIMOV XUSHNUD", "+998 99 944 32 94", "@Dav1atnazarovich")
y += 56

# ---------- motto ----------
mh = 300
rr([M, y, M+CW, y+mh], 40, fill=(247,196,74,30), outline=GOLD+(150,), width=4)
text((W//2, y+52), "NATIJALARIMIZGA  O’ZINGIZ  GUVOHSIZ", f("Black", 62), GOLD2, anchor="ma", sp=2)
text((W//2, y+142), "Ortiqcha gap-so’zga hojat yo’q — faqat mehnat qiling,", f("Medium", 48), (232,242,248), anchor="ma")
text((W//2, y+200), "eng yaxshisiga erishing. Yakunda esa — NATIJA!", f("Medium", 48), (232,242,248), anchor="ma")
y += mh + 56

# ---------- QR BLOK ----------
QR_TOP = y
qh = 700
rr([M, y, M+CW, y+qh], 40, fill=(255,255,255,18), outline=(90,150,180,110), width=3)
text((W//2, y+44), "TELEFONINGIZ  KAMERASINI  QARATING", f("Black", 50), GOLD, anchor="ma", sp=3)

QR_SLOTS = []          # (x, y, size, sarlavha, izoh)
qsize = 400
gapq = 300
qy = y + 140
x1 = W//2 - gapq//2 - qsize
x2 = W//2 + gapq//2
for qx, title, sub in [(x1, "TELEGRAM  KANAL", "yangiliklar va e’lonlar"),
                       (x2, "NATIJALARIMIZ", "sertifikat va ballar")]:
    rr([qx-24, qy-24, qx+qsize+24, qy+qsize+24], 30, fill=(255,255,255,255))
    QR_SLOTS.append((qx, qy, qsize))
    text((qx+qsize//2, qy+qsize+56), title, f("Black", 44), WHITE, anchor="ma", sp=2)
    text((qx+qsize//2, qy+qsize+112), sub, f("Regular", 36), MUTE, anchor="ma")

y += qh + 40

CONTENT_END = y + 40

# ================= compose =================
FH = CONTENT_END + 300          # + footer
bg = Image.new("RGB", (W, FH))
bd = ImageDraw.Draw(bg)
c1, c2 = (10,38,64), (4,14,26)
for i in range(FH):
    t = i/FH
    bd.line([(0,i),(W,i)], fill=tuple(int(c1[k]+(c2[k]-c1[k])*t) for k in range(3)))

gl = Image.new("L", (W,FH), 0); gd = ImageDraw.Draw(gl)
gd.ellipse([-900,-1100,1700,1100], fill=100)
gd.ellipse([1300,FH-1900,3300,FH+300], fill=78)
gl = gl.filter(ImageFilter.GaussianBlur(430))
bg = Image.composite(Image.new("RGB",(W,FH),(14,96,120)), bg, gl)

def wm(path, w_, pos, op, rot=0):
    im = Image.open(path)
    if rot: im = im.rotate(rot, expand=True)
    im = im.resize((w_, int(im.height*w_/im.width)), Image.LANCZOS)
    im.putalpha(im.split()[3].point(lambda p:int(p*op)))
    bg.paste(im, pos, im)

wm("dna_cut.png", 1150, (W-760, 240), 0.11)
wm("dna_cut.png", 900, (-330, FH-1750), 0.07, 180)
wm("mol_cut.png", 720, (W-620, FH-1400), 0.09)

img = bg.convert("RGBA")
img = Image.alpha_composite(img, layer.crop((0,0,W,FH)))
d = ImageDraw.Draw(img)

# ---------- QR rasmlarni joylashtirish ----------
for (qx, qy, qs), qfile in zip(QR_SLOTS, ["qr_kanal.png", "qr_natija.png"]):
    qim = Image.open(qfile).convert("RGB").resize((qs, qs), Image.LANCZOS)
    img.paste(qim, (int(qx), int(qy)))

# ---------- footer ----------
fy = FH - 300
d.rectangle([0, fy, W, FH], fill=(4,17,30))
d.rectangle([0, fy, W, fy+9], fill=GOLD)

text((W//2, fy+54), "HAQIQIY  BILIMNI  O’ZINGIZ  TANLANG!", f("Black", 58), WHITE, anchor="ma", sp=3)
tgf = f("Bold", 56)
label = "t.me/BiologiyaKimyomarkaz"
lw = tw(label, tgf) + 190
lx2 = (W - lw)//2
rr([lx2, fy+150, lx2+lw, fy+254], 52, fill=CYAN+(38,), outline=CYAN+(190,), width=4)
d.ellipse([lx2+30, fy+172, lx2+90, fy+232], fill=CYAN)
ic_tg(lx2+60, fy+202, 36, DARK)
text((lx2+118, fy+202), label, tgf, WHITE, anchor="lm")

out = img.convert("RGB")
out.save("biokimyo_afisha.png")
out.save("biokimyo_afisha.jpg", quality=93)
sc = 1400/W
out.resize((1400, int(FH*sc)), Image.LANCZOS).save("preview.jpg", quality=90)
print("size", W, FH)
