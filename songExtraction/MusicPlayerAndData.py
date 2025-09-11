#Combination of MusicData2 and MusicPlayer
#Songs information is loaded from the first song is played
#If Next song is clicked the information is loaded and the next song plays

import os
import random
import pygame
import re
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3, ID3NoHeaderError 

def Player():
    pygame.mixer.init() 

    folder_path = "C:\Visual Studio Code\Play or Nay\Songs"

    mp3_files = [file for file in os.listdir(folder_path) if file.endswith('.mp3')] 

    random_mp3 = random.choice(mp3_files)

    file_path = os.path.join(folder_path, random_mp3)
    pygame.mixer.music.load(file_path)

    MusicData(file_path)

    menu = 0 
    count = 0
    while menu != 5: 
        
        print("- - - - - - - - - - - - ")
        print("1 - Play Music/restart current song")
        print("2 - Pause Music")
        print("3 - Resume Music")
        print("4 - Next Song")
        print("5 - Exit")
        #print()
        
        print("- - - - - - - - - - - - ")
        print()
        menu = int(input("What would you like to do? "))
        print()
        print("- - - - - - - - - - - - ")


        if menu ==  1: 
            pygame.mixer.music.play()
            


        if menu == 2: 
            pygame.mixer.music.pause()

        if menu == 3: 
            pygame.mixer.music.unpause()

        if menu == 4: 

            random_mp3 = random.choice(mp3_files)
            file_path = os.path.join(folder_path, random_mp3)
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()
            MusicData(file_path)
def MusicData(mp3_file):
    cover_folder = r"C:\Visual Studio Code\Play or Nay\Cover"
    audio = EasyID3(mp3_file)

    

    title = audio.get("title",["Not Title Found"])[0]
    artist = audio.get("artist",["Not Artist Found"])[0]
    album = audio.get("album",["Not Album Found"])[0]

    print("Title:",title)
    print("Artist:",artist)
    print("Album:",album)

    cover_filename = album+"_cover.jpg"
    cover_path = os.path.join(cover_folder, cover_filename)

    tags = ID3(mp3_file)
    for tag in tags.values():
        if tag.FrameID == "APIC": 
            with open(cover_path,"wb") as img: # wb is write in binary and is how to save image
                img.write(tag.data)
            print("Saved Cover")
            break
    else: 
        print("No album art found")

def Main():
    Player()


Main()
