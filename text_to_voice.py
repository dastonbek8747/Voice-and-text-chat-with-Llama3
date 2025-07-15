import os

# Oʻzbekcha matnni MP3 ga aylantirish
os.system(f'edge-tts --voice uz-UZ-MadinaNeural --text "{
"""„Matn“ tushunchasining ikkita asosiy talqini mavjud: immanent (kengaytirilgan, falsafiy qarashlarga yoʻgʻrilgan) va reprezentativ (asosan, xususiy munosabat aks etgan). Immanent yondashuv matnda voqelikka xolis munosabat bildirib, uning ichki tuzilishini uchinchi shaxs tomonidan yoritishga eʼtibor qaratishni nazarda tutadi. Reprezentativ yondoshuv esa, matnni tashqi voqelik haqidagi maʼlumotni taqdim etishning maxsus shakli sifatida koʻrib chiqishni anglatadi.

Tilshunoslikda „matn“ atamasi keng doirada, jumladan, ogʻzaki nutq namunalarida ham qoʻllanadi. Matnni idrok etish matn lingvistikasi va psixolingvistika doirasida oʻrganiladi. I. R. Galperin matn xususiyatlari haqida toʻxtalib oʻtar ekan, unga quyidagicha taʼrif beradi: „Matn bu yozma hujjat shaklida ob’ektivlashtirilgan, turli xil leksik, grammatik va mantiqiy bogʻlanishlar bilan birlashtirilgan bir qator bayonotlardan tashkil topgan, axloqiy xarakter, pragmatik munosabat va shunga mos ravishda adabiy qayta ishlangan maʼlum bir xususiyatga ega boʻlgan yozma xabardir."""
}" --write-media voices/output.mp3')

# Faylni ochish (Ubuntu)
os.system("xdg-open voices/output.mp3")
