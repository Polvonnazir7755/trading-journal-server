# -*- coding: utf-8 -*-
"""
Vaziyat diagrammasi — "video orqali tushuntirish" ning realistik versiyasi.

To'liq AI-video hozircha qimmat va ishonchsiz. O'rniga:
  1) chorraha sxemasi chiziladi (aniq, xatosiz)
  2) qadamma-qadam kadrlar yaratiladi
  3) ovoz bilan birlashtiriladi -> MP4

Bu ancha ARZON va ANIQROQ, chunki geometriya kod bilan chiziladi.
"""
from pathlib import Path

def make_frames(scene: dict, out_dir: Path):
    """
    scene = {
      "roads": "cross",              # cross | t_left | t_right | roundabout
      "cars": [
          {"from": "south", "to": "north", "type": "car",  "label": "A", "order": 2},
          {"from": "west",  "to": "east",  "type": "tram", "label": "B", "order": 1},
      ],
      "signs": [{"pos": "south", "kind": "yield"}],
    }
    Har bir 'order' uchun alohida kadr -> harakat ketma-ketligi.
    """
    from PIL import Image, ImageDraw
    out_dir.mkdir(parents=True, exist_ok=True)
    W = H = 900
    CX = CY = W // 2
    RW = 200          # yo'l kengligi

    POS = {"north": (CX, 90), "south": (CX, H - 90),
           "west": (90, CY), "east": (W - 90, CY)}

    def base():
        im = Image.new("RGB", (W, H), (34, 40, 49))
        d = ImageDraw.Draw(im)
        # asfalt
        d.rectangle([CX - RW//2, 0, CX + RW//2, H], fill=(70, 74, 82))
        d.rectangle([0, CY - RW//2, W, CY + RW//2], fill=(70, 74, 82))
        # markaz chiziqlari
        for y in range(0, H, 40):
            if abs(y - CY) > RW//2:
                d.line([(CX, y), (CX, y + 20)], fill=(230, 230, 210), width=3)
        for x in range(0, W, 40):
            if abs(x - CX) > RW//2:
                d.line([(x, CY), (x + 20, CY)], fill=(230, 230, 210), width=3)
        return im, d

    def car(d, pos, label, kind, active):
        x, y = POS[pos]
        col = (255, 196, 60) if kind == "tram" else (90, 170, 255)
        if active:
            d.ellipse([x-46, y-46, x+46, y+46], outline=(80, 230, 140), width=5)
        d.rounded_rectangle([x-30, y-42, x+30, y+42], radius=10, fill=col)
        d.text((x-5, y-8), label, fill=(20, 20, 20))

    frames = []
    orders = sorted({c.get("order", 1) for c in scene.get("cars", [])})
    for step in range(len(orders) + 1):
        im, d = base()
        for c in scene.get("cars", []):
            active = step > 0 and c.get("order", 1) == orders[step - 1]
            car(d, c["from"], c.get("label", ""), c.get("type", "car"), active)
        cap = "Boshlang'ich holat" if step == 0 else f"{step}-navbat"
        d.rectangle([0, H-56, W, H], fill=(20, 24, 30))
        d.text((20, H-38), cap, fill=(235, 235, 235))
        p = out_dir / f"frame_{step:02d}.png"
        im.save(p)
        frames.append(p)
    return frames


def build_video(frames, audio_path, out_mp4, sec_per_frame=3.0):
    """Kadrlar + ovoz -> MP4. ffmpeg kerak."""
    import subprocess, tempfile
    lst = Path(tempfile.mktemp(suffix=".txt"))
    lines = []
    for f in frames:
        lines.append(f"file '{f.resolve()}'")
        lines.append(f"duration {sec_per_frame}")
    lines.append(f"file '{frames[-1].resolve()}'")
    lst.write_text("\n".join(lines))
    cmd = ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(lst)]
    if audio_path and Path(audio_path).exists():
        cmd += ["-i", str(audio_path), "-shortest"]
    cmd += ["-vf", "scale=900:900", "-pix_fmt", "yuv420p", str(out_mp4)]
    subprocess.run(cmd, check=True, capture_output=True)
    return out_mp4


if __name__ == "__main__":
    scene = {
        "roads": "cross",
        "cars": [
            {"from": "west",  "type": "tram", "label": "B", "order": 1},
            {"from": "south", "type": "car",  "label": "A", "order": 2},
            {"from": "east",  "type": "car",  "label": "C", "order": 3},
        ],
    }
    fr = make_frames(scene, Path("demo_frames"))
    print(f"{len(fr)} kadr yaratildi:")
    for f in fr:
        print(" ", f)
