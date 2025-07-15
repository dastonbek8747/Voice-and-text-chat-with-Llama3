import os

# Oʻzbekcha matnni MP3 ga aylantirish
os.system(f'edge-tts --voice uz-UZ-MadinaNeural --text "{"salom. men aqlli uy loyihasi uchun Sultonov Doston tomonidan yaratildim. Men seni uyingni boshqarishda senga yordam beraman."}" --write-media voices/output.mp3')

# Faylni ochish (Ubuntu)
os.system("xdg-open voices/output.mp3")
