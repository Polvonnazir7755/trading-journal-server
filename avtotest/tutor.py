# -*- coding: utf-8 -*-
"""
AVTO TEST AI MENTOR — rasmni ko'radi, gapirib tushuntiradi.

OQIM:
  rasm  ->  Vision AI  ->  tushuntirish matni  ->  TTS  ->  ovoz
                 ^
          rasmiy javob (ground truth)

ENG MUHIM QOIDA:
  AI javobni O'ZI TANLAMAYDI. Rasmiy javob beriladi, AI faqat
  NEGA to'g'ri va NEGA boshqalari noto'g'ri ekanini tushuntiradi.
  Sabab: AI yo'l belgisini xato o'qishi mumkin -> odam imtihondan
  yiqiladi yoki yo'lda xato qiladi.
"""
import os, json, base64, hashlib
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import List, Optional

CACHE = Path(__file__).parent / "cache"
CACHE.mkdir(exist_ok=True)


@dataclass
class Question:
    id: str
    image_path: str
    options: List[str]
    correct_index: int          # rasmiy javob — MAJBURIY
    topic: str = ""
    official_note: str = ""     # rasmiy izoh bo'lsa


@dataclass
class Explanation:
    question_id: str
    scene: str                  # rasmda nima ko'rinyapti
    rule: str                   # qaysi qoida ishlaydi
    correct_why: str            # nega to'g'ri
    wrong_why: List[str]        # har bir noto'g'ri variant uchun
    memory_tip: str             # eslab qolish uchun
    speech: str                 # ovoz uchun to'liq matn
    needs_diagram: bool = False


SYSTEM = """Sen — tajribali avtomaktab o'qituvchisisan. O'zbek tilida gapirasan.

MUHIM: to'g'ri javob SENGA BERILADI. Sening vazifang — uni tanlash emas,
balki TUSHUNTIRISH.

USLUB:
- Jonli gapir, konspekt yozma. Talaba oldida turgandek
- Qisqa jumlalar. Ovozda o'qiladi
- "Qarang", "e'tibor bering", "esda tuting" kabi murojaatlar ishlat
- Har bir noto'g'ri variantni ALOHIDA tushuntir — nega noto'g'ri
- Oxirida eslab qolish uchun oddiy qoida ber

QAT'IY TAQIQ:
- Berilgan javobga qarshi chiqma
- Ishonchsiz bo'lsang, "bu savolda o'qituvchingizdan so'rang" de
- Qoidani o'ylab topma

JSON qaytaring:
{
  "scene": "rasmda nima ko'rinyapti (1-2 jumla)",
  "rule": "qaysi qoida ishlaydi",
  "correct_why": "nega to'g'ri javob shu",
  "wrong_why": ["1-variant nega noto'g'ri", "..."],
  "memory_tip": "eslab qolish uchun oddiy qoida",
  "speech": "OVOZ UCHUN to'liq matn — tabiiy gapiruv, 60-120 so'z",
  "needs_diagram": true/false
}"""


def _img_b64(path: str) -> tuple:
    p = Path(path)
    data = base64.standard_b64encode(p.read_bytes()).decode()
    ext = p.suffix.lower().lstrip(".")
    mt = {"jpg": "image/jpeg", "jpeg": "image/jpeg",
          "png": "image/png", "webp": "image/webp"}.get(ext, "image/jpeg")
    return data, mt


def explain(q: Question, api_key: str = None, model: str = "claude-sonnet-4-5") -> Explanation:
    """Rasmni ko'rib, tushuntirish yaratadi. Natija keshlanadi."""
    key = hashlib.md5(f"{q.id}{q.correct_index}".encode()).hexdigest()[:12]
    cf = CACHE / f"{key}.json"
    if cf.exists():
        return Explanation(**json.loads(cf.read_text(encoding="utf-8")))

    api_key = api_key or os.getenv("ANTHROPIC_API_KEY", "")
    if not api_key:
        raise RuntimeError("ANTHROPIC_API_KEY kerak")

    import anthropic
    client = anthropic.Anthropic(api_key=api_key)
    b64, mt = _img_b64(q.image_path)

    opts = "\n".join(f"{chr(65+i)}) {o}" for i, o in enumerate(q.options))
    user = (f"SAVOL RASMI biriktirilgan.\n\nVARIANTLAR:\n{opts}\n\n"
            f"RASMIY TO'G'RI JAVOB: {chr(65+q.correct_index)}\n"
            f"{('Rasmiy izoh: ' + q.official_note) if q.official_note else ''}\n\n"
            f"Shu javobni tushuntir.")

    r = client.messages.create(
        model=model, max_tokens=1600, system=SYSTEM,
        messages=[{"role": "user", "content": [
            {"type": "image", "source": {"type": "base64",
             "media_type": mt, "data": b64}},
            {"type": "text", "text": user}]}])

    txt = r.content[0].text
    s, e = txt.find("{"), txt.rfind("}") + 1
    d = json.loads(txt[s:e])
    ex = Explanation(question_id=q.id, **d)
    cf.write_text(json.dumps(asdict(ex), ensure_ascii=False, indent=2), encoding="utf-8")
    return ex


def speak(text: str, out_path: str, voice: str = "uz"):
    """Matnni ovozga aylantiradi. Bir necha TTS varianti."""
    # 1-variant: ElevenLabs (eng sifatli)
    key = os.getenv("ELEVENLABS_API_KEY", "")
    if key:
        import requests
        vid = os.getenv("ELEVENLABS_VOICE_ID", "")
        r = requests.post(
            f"https://api.elevenlabs.io/v1/text-to-speech/{vid}",
            headers={"xi-api-key": key, "Content-Type": "application/json"},
            json={"text": text, "model_id": "eleven_multilingual_v2"})
        if r.ok:
            Path(out_path).write_bytes(r.content)
            return out_path

    # 2-variant: edge-tts (BEPUL, o'zbek tilini qo'llaydi)
    try:
        import edge_tts, asyncio
        async def _go():
            c = edge_tts.Communicate(text, "uz-UZ-SardorNeural")
            await c.save(out_path)
        asyncio.run(_go())
        return out_path
    except ImportError:
        pass

    raise RuntimeError("TTS yo'q: pip install edge-tts")


if __name__ == "__main__":
    print(__doc__)
    print("\nNAMUNA ISHLATISH:\n")
    print("""
from tutor import Question, explain, speak

q = Question(
    id="q_142",
    image_path="savollar/142.jpg",
    options=["Faqat A avtomobil", "A va B avtomobillar",
             "Barcha avtomobillar", "Hech qaysi"],
    correct_index=1,
    topic="Chorraha"
)

ex = explain(q)          # rasmni ko'radi, tushuntiradi
print(ex.speech)
speak(ex.speech, "javob.mp3")   # ovozga aylantiradi
""")
