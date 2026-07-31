# -*- coding: utf-8 -*-
"""
Chiroyli, LEKIN ISHONCHLI QR kod.
Burchak markerlari (finder) standart kvadrat — o'zgartirilsa skaner buziladi.
Faqat ma'lumot nuqtalari dumaloqlashtiriladi.
"""
import qrcode
from qrcode.constants import ERROR_CORRECT_H
from PIL import Image, ImageDraw

def make_qr(data, path, px=1200, fg=(8, 26, 44), bg=(255, 255, 255),
            rounded=True, logo_ratio=0.0, verify=True):
    q = qrcode.QRCode(error_correction=ERROR_CORRECT_H, box_size=1, border=0)
    q.add_data(data)
    q.make(fit=True)
    m = q.get_matrix()
    n = len(m)

    quiet = 4                                  # tinch zona — majburiy
    total = n + quiet * 2
    scale = max(3, px // total)
    size = total * scale

    img = Image.new("RGB", (size, size), bg)
    d = ImageDraw.Draw(img)

    def on(r, c):
        return 0 <= r < n and 0 <= c < n and m[r][c]

    def is_finder(r, c):
        return (r < 7 and c < 7) or (r < 7 and c >= n - 7) or (r >= n - 7 and c < 7)

    # --- ma'lumot nuqtalari ---
    for r in range(n):
        for c in range(n):
            if not m[r][c] or is_finder(r, c):
                continue
            x0, y0 = (c + quiet) * scale, (r + quiet) * scale
            x1, y1 = x0 + scale, y0 + scale
            if not rounded:
                d.rectangle([x0, y0, x1 - 1, y1 - 1], fill=fg)
                continue
            nb = (on(r - 1, c), on(r + 1, c), on(r, c - 1), on(r, c + 1))
            if not any(nb):
                d.ellipse([x0, y0, x1 - 1, y1 - 1], fill=fg)      # yolg'iz -> doira
            else:
                rad = int(scale * 0.42)
                d.rounded_rectangle([x0, y0, x1 - 1, y1 - 1], radius=rad, fill=fg)
                # qo'shnilar bilan tutashtirish
                h = scale // 2
                if nb[0]: d.rectangle([x0, y0, x1 - 1, y0 + h], fill=fg)
                if nb[1]: d.rectangle([x0, y0 + h, x1 - 1, y1 - 1], fill=fg)
                if nb[2]: d.rectangle([x0, y0, x0 + h, y1 - 1], fill=fg)
                if nb[3]: d.rectangle([x0 + h, y0, x1 - 1, y1 - 1], fill=fg)

    # --- burchak markerlari: STANDART kvadrat (o'zgartirmaymiz!) ---
    for (fr, fc) in [(0, 0), (0, n - 7), (n - 7, 0)]:
        for r in range(fr, fr + 7):
            for c in range(fc, fc + 7):
                if not m[r][c]:
                    continue
                x0, y0 = (c + quiet) * scale, (r + quiet) * scale
                d.rectangle([x0, y0, x0 + scale - 1, y0 + scale - 1], fill=fg)

    # --- markazdagi logo joyi (ERROR_CORRECT_H => 30% gacha bardosh) ---
    if logo_ratio > 0:
        ls = int(size * logo_ratio)
        lx = (size - ls) // 2
        d.rounded_rectangle([lx, lx, lx + ls, lx + ls], radius=int(ls * 0.2), fill=bg)

    img.save(path)

    ok = None
    if verify:
        try:
            import cv2
            ok = bool(cv2.QRCodeDetector().detectAndDecode(cv2.imread(path))[0])
        except ImportError:
            pass
    print(f"{path:<18} modules={n:<3} size={img.size}  skaner={'OK' if ok else ('FAIL' if ok is False else '?')}")
    return img


if __name__ == "__main__":
    make_qr("https://t.me/BiologiyaKimyomarkaz", "qr_kanal.png", logo_ratio=0.16)
    make_qr("https://t.me/BiologiyaKimyomarkaz", "qr_natija.png", logo_ratio=0.16)
