import os
import time
processing_shown = False
audio_number = 0
AUDIO_FILE_PATH = f"voices/{audio_number}_output.mp3"


def speek_text(data: str):
    global audio_number
    global processing_shown
    if not data.strip():
        if not processing_shown:
            print("Maʼlumotlar qayta ishlanmoqda...")
            os.system(
                f'edge-tts --voice uz-UZ-MadinaNeural --text "Maʼlumotlar qayta ishlanmoqda..." --write-media {AUDIO_FILE_PATH}'
            )
            play_audio()
            processing_shown = True
        return
    print("AI javobi ovozga aylantirilmoqda...")
    os.system(
        f'edge-tts --voice uz-UZ-MadinaNeural --text "{data}" --write-media {AUDIO_FILE_PATH}'
    )
    play_audio()
    audio_number += 1
    processing_shown = False


def play_audio():
    if os.path.exists(AUDIO_FILE_PATH):
        os.system(f"cvlc --play-and-exit {AUDIO_FILE_PATH} >/dev/null 2>&1")
    else:
        print("Ovoz fayli topilmadi.")
