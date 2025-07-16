import speech_recognition

rec = speech_recognition.Recognizer()
mikrofon = speech_recognition.Microphone()
print("Mikrofon tayyor boldi ....."
      "gapir.....")
sikl = True

with mikrofon as mic:
    rec.adjust_for_ambient_noise(mic)
    while sikl:
        print("⏳ Eshitilmoqda...")
        audio = rec.listen(mic)

        try:
            text = rec.recognize_google(audio, language="uz-UZ")
            print("matin:", text)
            if text.lower() == "to'xta":
                sikl = False

        except speech_recognition.UnknownValueError:
            print("😕 Tushunib bo‘lmadi...")
        except speech_recognition.RequestError as e:
            print(f"❌ API muammosi: {e}")
