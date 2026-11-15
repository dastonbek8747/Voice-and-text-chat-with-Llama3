# 🎙 Ovoz va Matn Orqali Llama3 bilan Suhbat

Ovozni matnga, matnni ovozga aylantirib, **Llama3** modeli bilan suhbatlashish imkonini beruvchi loyiha.

---

## ✨ Imkoniyatlar

- 🎤 **Ovozdan matnga:** `speech_recognition` + Google Speech
- 🔊 **Matndan ovozga:** `edge-tts` (o'zbek ovozi — MadinaNeural)
- 🌐 **Tarjima:** `deep_translator` (UZ ⇄ EN)
- 🤖 **AI suhbat:** Llama3 / Groq / xAI orqali javob
- ▶️ **Ovozni ijro etish:** `cvlc`

---

## 🛠 Texnologiyalar

| Texnologiya | Maqsad |
|---|---|
| **Python 3.10+** | Asosiy til |
| **speech_recognition** | Ovozni matnga |
| **edge-tts** | Matnni ovozga |
| **deep_translator** | Tarjima |
| **python-dotenv** | Muhit o'zgaruvchilari |

> Tizimda `edge-tts` va `vlc` (`cvlc`) o'rnatilgan bo'lishi kerak.

---

## ⚙️ O'rnatish

```bash
git clone https://github.com/dastonbek8747/Voice-and-text-chat-with-Llama3.git
cd Voice-and-text-chat-with-Llama3
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Tizim paketlari (Ubuntu/Debian)
sudo apt install vlc
pip install edge-tts
```

Kalitni sozlang:

```bash
cp .env.example .env
```

---

## ▶️ Ishga tushirish

```bash
python llama_chat.py
```

Mikrofon orqali gapiring; bot javobini ovozda eshitasiz.

---

## 📁 Loyiha tuzilishi

```
Voice-and-text-chat-with-Llama3/
├── llama_chat.py      # Asosiy suhbat sikli
├── voice_to_text.py   # Ovozni matnga
├── text_to_voice.py   # Matnni ovozga
├── requirements.txt
├── tests/
└── .env.example
```

---

## 📄 Litsenziya

Litsenziya ko'rsatilmagan.
