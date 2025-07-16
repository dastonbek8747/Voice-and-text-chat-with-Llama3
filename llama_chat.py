import requests
import text_to_voice
import voice_to_text


# bu funksiya llama3 modelimga sorov yuborayapdi va undan kelgan responsni qaytarib yuboradi!
# siz bu yerda istalgan ai bilan integratsiya qilishingiz mumkin boladi

def get_date_ai(txt: str):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": f"{txt}",
            "stream": False
        }
    )
    ai_text_return = response.json()["response"]
    print("AI javobi :", ai_text_return)
    return ai_text_return


# demak funksiyalarni chaqirib loyihani tayyor qisimin yashayniz
sikl = True


def ai_communication():
    global sikl
    ...
    while sikl:
        txt = voice_to_text.listen_and_get_text()
        if txt.lower() == "to'xta":
            sikl = False
        elif txt.lower() == "yaxshi":
            print("  sen bu sozni aytding :", txt)
        else:
            data = get_date_ai(txt)
            text_to_voice.speek_text(data)


ai_communication()
