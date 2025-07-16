import os

# Bir martalik status flag (global o'zgaruvchi)
processing_shown = False


def speek_text(data):
    global processing_shown

    if not data.strip():
        # Faqat bir marta aytiladi
        if not processing_shown:
            print("🟡 Maʼlumotlar qayta ishlanmoqda...")
            os.system(
                'edge-tts --voice uz-UZ-MadinaNeural --text "Maʼlumotlar qayta ishlanmoqda..." --write-media voices/output.mp3'
            )
            os.system("xdg-open voices/output.mp3")
            processing_shown = True
        return ""

    # Agar text bo‘sh bo‘lmasa:
    print("✅ Matn ovozga aylantirilmoqda:", data)
    os.system(
        f'edge-tts --voice uz-UZ-MadinaNeural --text "{data}" --write-media voices/output.mp3'
    )
    os.system("xdg-open voices/output.mp3")

    processing_shown = False  # qayta reset qilinadi
    return ""
