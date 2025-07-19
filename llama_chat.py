import requests
from deep_translator import GoogleTranslator
import voice_to_text
import text_to_voice


def get_date_ai(txt: str):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": txt,
            "stream": False
        }
    )
    return response.json()["response"]


def ai_communication():
    while True:
        voice_to_text.continue_listening = True
        txt = voice_to_text.listen_and_get_text()
        print("Ovozdan olingan matn:", txt)

        if txt.lower() == "dastur toxtatilsin":
            break
        else:
            voice_to_text.continue_listening = False
            english_txt = GoogleTranslator(source='uz', target='en').translate(txt)
            print("Tarjima (UZ ➜ EN):", english_txt)
            ai_result = get_date_ai(english_txt)
            print("AI javobi (EN):", ai_result)
            uzbek_response = GoogleTranslator(source='en', target='uz').translate(ai_result)
            print("Tarjima (EN ➜ UZ):", uzbek_response)
            text_to_voice.speek_text(uzbek_response)
            voice_to_text.continue_listening = True


ai_communication()
