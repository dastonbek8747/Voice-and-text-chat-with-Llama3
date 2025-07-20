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

        if txt.lower() == "to'xta":
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
# import requests
#
# GROK_API_URL = "https://api.grok.ai/v1/chat"
# GROK_API_KEY = "///////"  # API tokenni o'zgaruvchiga joylang
#
#
# def get_date_ai(txt: str):
#     headers = {
#         "Authorization": f"Bearer {GROK_API_KEY}",
#         "Content-Type": "application/json"
#     }
#
#     payload = {
#         "model": "grok-1",  # yoki sizdagi model nomi
#         "messages": [
#             {"role": "user", "content": txt}
#         ]
#     }
#
#     response = requests.post(GROK_API_URL, headers=headers, json=payload)
#
#     if response.status_code == 200:
#         data = response.json()
#         return data["choices"][0]["message"]["content"]
#     else:
#         print("❌ Grok API xatosi:", response.text)
#         return "Kechirasiz, javob olishda muammo bo‘ldi."
#
#
# def ai_communication():
#     while True:
#         voice_to_text.continue_listening = True
#         txt = voice_to_text.listen_and_get_text()
#         print("Ovozdan olingan matn:", txt)
#
#         if txt.lower() == "to'xta":
#             break
#         else:
#             voice_to_text.continue_listening = False
#             english_txt = GoogleTranslator(source='uz', target='en').translate(txt)
#             print("Tarjima (UZ ➜ EN):", english_txt)
#
#             ai_result = get_date_ai(english_txt)
#             print("AI javobi (EN):", ai_result)
#
#             uzbek_response = GoogleTranslator(source='en', target='uz').translate(ai_result)
#             print("Tarjima (EN ➜ UZ):", uzbek_response)
#
#             text_to_voice.speek_text(uzbek_response)
#             voice_to_text.continue_listening = True
#
#
# ai_communication()
# # import os
# #
# # from xai_sdk import Client
# # from xai_sdk.chat import user, system
# #
# # client = Client(
# #     api_key=os.getenv("XAI_API_KEY"),
# #     timeout=3600,  # Override default timeout with longer timeout for reasoning models
# # )
# #
# # chat = client.chat.create(model="grok-4")
# # chat.append(system("You are Grok, a highly intelligent, helpful AI assistant."))
# # chat.append(user("What is the meaning of life, the universe, and everything?"))
# #
# # response = chat.sample()
# # print(response.content)