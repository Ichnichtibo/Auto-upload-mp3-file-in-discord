import os
from mutagen.mp3 import MP3

folder_path = "C:/Users/saykı/Desktop/Code/Pyhton Klasör/Python_Camping/selenium/Discord/sounnds"

for filename in os.listdir(folder_path):
    if filename.endswith(".mp3"):
        file_path = os.path.join(folder_path, filename)
        audio = MP3(file_path)
        length = audio.info.length
        if length > 5:
            os.remove(file_path)
            print(f"{filename} dosyası silindi.")