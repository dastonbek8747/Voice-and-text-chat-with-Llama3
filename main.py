# import os
# import subprocess
#
#
# def text_to_speech(text, voices="uz-UZ-MadinaNeural", output_file="output.mp3"):
#     """
#     Berilgan matnni ovozga aylantirib, MP3 fayliga saqlaydi.
#
#     Parametrlar:
#         text (str): Ovozga aylantiriladigan matn
#         voices (str): Ovoz modeli (default: uz-UZ-MadinaNeural)
#         output_file (str): Saqlanadigan fayl nomi (default: output.mp3)
#     """
#     try:
#         # Matndagi maxsus belgilarni to'g'rilash
#         text = text.replace('"', '\\"').replace("'", "\\'")
#
#         # edge-tts buyrug'ini tayyorlash
#         cmd = f'edge-tts --voices {voices} --text "{text}" --write-media {output_file}'
#
#         # Buyruqni ishga tushirish
#         subprocess.run(cmd, shell=True, check=True)
#
#         # Faylni ochish (Ubuntu)
#         os.system(f"xdg-open {output_file}")
#
#         print(f"Ovoz fayli muvaffaqiyatli yaratildi: {output_file}")
#     except Exception as e:
#         print(f"Xatolik yuz berdi: {e}")
#
#
# # Funksiyani test qilish
# if __name__ == "__main__":
#     long_text = """
#     „Matn" tushunchasining ikkita asosiy talqini mavjud: immanent (kengaytirilgan, falsafiy qarashlarga yoʻgʻrilgan) va reprezentativ (asosan, xususiy munosabat aks etgan). Immanent yondashuv matnda voqelikka xolis munosabat bildirib, uning ichki tuzilishini uchinchi shaxs tomonidan yoritishga eʼtibor qaratishni nazarda tutadi. Reprezentativ yondoshuv esa, matnni tashqi voqelik haqidagi maʼlumotni taqdim etishning maxsus shakli sifatida koʻrib chiqishni anglatadi.
#
#     Tilshunoslikda „matn" atamasi keng doirada, jumladan, ogʻzaki nutq namunalarida ham qoʻllanadi. Matnni idrok etish matn lingvistikasi va psixolingvistika doirasida oʻrganiladi. I. R. Galperin matn xususiyatlari haqida toʻxtalib oʻtar ekan, unga quyidagicha taʼrif beradi: „Matn bu yozma hujjat shaklida ob'ektivlashtirilgan, turli xil leksik, grammatik va mantiqiy bogʻlanishlar bilan birlashtirilgan bir qator bayonotlardan tashkil topgan, axloqiy xarakter, pragmatik munosabat va shunga mos ravishda adabiy qayta ishlangan maʼlum bir xususiyatga ega boʻlgan yozma xabardir"[1].
#     """
#
#     text_to_speech(long_text)
