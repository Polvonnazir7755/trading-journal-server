# Avto Test AI Mentor

**Rasmni ko'radi → gapirib tushuntiradi → kerak bo'lsa video chizadi.**

---

## Nima qiladi

```
Savol rasmi  →  Vision AI  →  tushuntirish  →  TTS  →  ovoz
                     ↑
              rasmiy javob
```

Har bir variant uchun **alohida** tushuntirish:
- Rasmda nima ko'rinyapti
- Qaysi qoida ishlaydi
- Nega to'g'ri javob shu
- **Nega qolgan variantlar noto'g'ri**
- Eslab qolish uchun oddiy qoida

---

## ⚠️ ENG MUHIM QOIDA

**AI javobni O'ZI TANLAMAYDI.**

Rasmiy javob **beriladi**, AI faqat tushuntiradi.

Nega bu shart:
- AI yo'l belgisini xato o'qishi mumkin
- Chorrahada mashina yo'nalishini adashtirishi mumkin
- Natijada odam imtihondan yiqiladi yoki **yo'lda xato qiladi**

Bu — hayot xavfsizligi masalasi. Shuning uchun `correct_index`
majburiy maydon.

---

## Fayllar

| Fayl | Vazifasi |
|---|---|
| `tutor.py` | Vision AI + tushuntirish + TTS |
| `diagram.py` | Chorraha sxemasi + video kadrlar |
| `namuna_ovoz.mp3` | Ovoz namunasi |
| `demo_frames/` | Diagramma kadrlari |

---

## Ishlatish

```python
from tutor import Question, explain, speak

q = Question(
    id="142",
    image_path="savollar/142.jpg",
    options=["Faqat A", "Tramvay B", "Avtomobil C", "Bir vaqtda"],
    correct_index=1,              # RASMIY javob — majburiy
    topic="Teng huquqli chorraha"
)

ex = explain(q)                   # rasmni ko'radi
print(ex.speech)                  # tushuntirish matni
speak(ex.speech, "javob.mp3")     # ovozga aylantiradi
```

Video kerak bo'lsa:
```python
from diagram import make_frames, build_video
frames = make_frames(scene, Path("frames"))
build_video(frames, "javob.mp3", "javob.mp4")
```

---

## O'rnatish

```bash
pip install anthropic pillow edge-tts requests
```

**API kalitlar:**
```
ANTHROPIC_API_KEY=sk-ant-...        # rasmni ko'rish uchun
ELEVENLABS_API_KEY=...              # ixtiyoriy, sifatliroq ovoz
```

`edge-tts` **bepul** va o'zbek ovozini qo'llaydi (`uz-UZ-SardorNeural`).

---

## Ovoz haqida

| Variant | Narx | Sifat | O'zbek |
|---|---|---|---|
| **edge-tts** | bepul | yaxshi | ✅ `uz-UZ-SardorNeural` |
| ElevenLabs | ~$5/oy | a'lo | ✅ multilingual |
| Google TTS | ~$4/1M belgi | yaxshi | ✅ |

Boshlash uchun **edge-tts** yetarli.

---

## Narx hisobi (1000 savol)

| Xarajat | Summa |
|---|---|
| Vision AI (1000 rasm) | ~$15–25 |
| TTS (1000 × 100 so'z) | $0 (edge-tts) |
| **Keshlash** | 1 marta → abadiy |

**Muhim:** tushuntirish bir marta yaratiladi va `cache/` ga saqlanadi.
Keyingi safar bepul. 1000 savol = bir martalik ~$20.

---

## Video haqida — halol gap

To'liq AI-video (Sora/Veo) hozircha:
- qimmat (~$0.5–2 har video)
- **ishonchsiz** — chorrahani xato chizishi mumkin

Shuning uchun `diagram.py` **kod bilan chizadi**:
- geometriya aniq, xatosiz
- bepul
- qadamma-qadam navbat ko'rsatadi

Bu "kino" emas, lekin **o'qitish uchun aniqroq**.

---

## Cheklovlar

| Nima | Holat |
|---|---|
| Rasmni ko'rish | ✅ ishlaydi |
| Tushuntirish | ✅ ishlaydi |
| O'zbek ovozi | ✅ edge-tts |
| Sxema/diagramma | ✅ kod bilan |
| Real video (3D) | ⚠️ qimmat, ishonchsiz |
| **Javobni topish** | ❌ **ataylab yo'q** |

---

## Keyingi qadam

1. **10 ta savol rasmi** + rasmiy javoblari yuboring
2. Men to'liq pipeline'ni sinab ko'raman
3. Natija yoqsa — butun bazaga qo'llaymiz
4. Keyin ilovaga ulash (Telegram bot yoki mobil)
