# This page deleting upper 5 sec mp3 files

import os
from mutagen.mp3 import MP3

# your sounds pack folder
folder_path = "/path/to/folder/sounds"

for filename in os.listdir(folder_path):
    if filename.endswith(".mp3"):
        file_path = os.path.join(folder_path, filename)
        audio = MP3(file_path)
        length = audio.info.length
        if length > 5:
            os.remove(file_path)
            print(f"{filename} dosyası silindi.")
