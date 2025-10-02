#Chase Allen
#Date: 9/8/25
#Software Engineering

import os
import re
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3, ID3NoHeaderError

cover_folder = r"C:\Visual Studio Code\Play or Nay\Cover"
mp3_folder = r"C:\Visual Studio Code\Play or Nay\Songs"

for filename in os.listdir(mp3_folder):
    if filename.lower().endswith(".mp3"):
        mp3_save = os.path.join(mp3_folder,filename)

    audio = EasyID3(mp3_save)

    title = audio.get("title",["Not Title Found"])[0]
    artist = audio.get("artist",["Not Artist Found"])[0]
    album = audio.get("album",["Not Album Found"])[0]
    print("Title:",title)
    print("Artist:",artist)
    print("Album:",album)

    cover_filename = album+"_cover.jpg"
    cover_path = os.path.join(cover_folder, cover_filename)

    tags = ID3(mp3_save)
    for tag in tags.values():
        if tag.FrameID == "APIC": 
            with open(cover_path,"wb") as img: # wb is write in binary and is how to save image
                img.write(tag.data)
            print("Saved Cover")
            break
    else: 
        print("No album art found")