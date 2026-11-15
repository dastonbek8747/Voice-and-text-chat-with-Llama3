import os
import subprocess

processing_shown = False
audio_number = 0
AUDIO_FILE_PATH = f"voices/{audio_number}_output.mp3"
EDGE_TTS = "edge-tts"
CVLC = "cvlc"


def build_edge_tts_command(data: str, output_path: str) -> list:
    """edge-tts buyrug'ini argv ro'yxati sifatida quradi (shell ishlatilmaydi)."""
    return [
        EDGE_TTS,
        "--voice",
        "uz-UZ-MadinaNeural",
        "--text",
        data,
        "--write-media",
        output_path,
    ]


def build_play_command(path: str) -> list:
    return [CVLC, "--play-and-exit", path]


def _run(cmd: list) -> bool:
    try:
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except (FileNotFoundError, subprocess.CalledProcessError) as exc:
        print(f"⚠️ Buyruq bajarilmadi: {exc}")
        return False


def speek_text(data: str):
    global audio_number
    global processing_shown
    if not data.strip():
        if not processing_shown:
            print("Maʼlumotlar qayta ishlanmoqda...")
            _run(build_edge_tts_command("Maʼlumotlar qayta ishlanmoqda...", AUDIO_FILE_PATH))
            play_audio()
            processing_shown = True
        return
    print("AI javobi ovozga aylantirilmoqda...")
    _run(build_edge_tts_command(data, AUDIO_FILE_PATH))
    play_audio()
    audio_number += 1
    processing_shown = False


def play_audio():
    if os.path.exists(AUDIO_FILE_PATH):
        _run(build_play_command(AUDIO_FILE_PATH))
    else:
        print("Ovoz fayli topilmadi.")

