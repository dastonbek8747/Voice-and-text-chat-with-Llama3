import speech_recognition as sr


def listen_and_get_text(lang="uz-UZ"):
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    print("🎙 Mikrofon tayyor. Gapir...")

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)

        while True:
            print("⏳ Gap eshitilmoqda...")
            audio = recognizer.listen(source)

            try:
                text = recognizer.recognize_google(audio, language=lang)
                print("📥 Matn:", text)
                # Matn tushunarli bo‘lsa uni qaytaramiz
                return text.strip()

            except sr.UnknownValueError:
                print("😕 Tushunib bo‘lmadi...")
            except sr.RequestError as e:
                print(f"❌ Google API xatosi: {e}")
