import speech_recognition as sr
import time

continue_listening = True

def listen_and_get_text(lang="uz-UZ"):
    global continue_listening
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        while True:
            if not continue_listening:
                time.sleep(0.5)
                continue
            print("Gapiring  >>>>>>>>")
            try:
                audio = recognizer.listen(source, timeout=5)
                text = recognizer.recognize_google(audio, language=lang)
                return text.strip()
            except sr.UnknownValueError:
                print("Tushunib bo‘lmadi...")
            except sr.WaitTimeoutError:
                print("Hech narsa eshitilmadi.")
            except sr.RequestError as e:
                print(f"❌ Google API xatosi: {e}")
