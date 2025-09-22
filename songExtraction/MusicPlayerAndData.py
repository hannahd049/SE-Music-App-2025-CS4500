#Combination of MusicData2 and MusicPlayer
#Songs information is loaded from the first song is played
#If Next song is clicked the information is loaded and the next song plays
#updated with more menus and playlists 
#added Zimani's timer

#pip install mutagen
#pip3 install pygame

import os
import random
import pygame 
import re
import threading 

from mutagen.easyid3 import EasyID3 
from mutagen.id3 import ID3, ID3NoHeaderError 

def listPlayer(playList):
    pygame.mixer.music.load(playList[0]) 

    playListPlayer = 0 
    nextSong = 0

    while playListPlayer != 5:

        print("- - - - - - - - - - - - ")
        print("1 - Play Music/restart current song")
        print("2 - Pause Music")
        print("3 - Resume Music")
        print("4 - Next Song")
        print("5 - Exit") 
        print("- - - - - - - - - - - - ") 


        print("- - - - - - - - - - - - ")
        playListPlayer = int(input("What would you like to do? "))
        print("- - - - - - - - - - - - ")  

        if playListPlayer ==  1: 
            pygame.mixer.music.play()

        elif playListPlayer == 2: 
            pygame.mixer.music.pause()

        elif playListPlayer == 3: 
            pygame.mixer.music.unpause()

        elif playListPlayer == 4: 

            nextSong += 1

            file_path = playList[nextSong] 
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()
            MusicData(file_path) 
        elif playList == 5:
            break
        else:
            print("Invalid input, please try again.")

def menu1(menu, yayList, nayList, folder_path):
    mp3_files = [file for file in os.listdir(folder_path) if file.endswith('.mp3')] 

    random_mp3 = random.choice(mp3_files)

    file_path = os.path.join(folder_path, random_mp3)
    pygame.mixer.music.load(file_path)

    MusicData(file_path) 

    while menu != 7: 
        
        
        print("- - - - - - - - - - - - ")
        print("1 - Play Music/restart current song")
        print("2 - Pause Music")
        print("3 - Resume Music")
        print("4 - Vote Yay")
        print("5 - Vote Nay")
        print("6 - Go to playlists")
        print("7 - Exit")
        #print()
        
        print("- - - - - - - - - - - - ")
        print()
        menu = int(input("What would you like to do? "))
        print()
        print("- - - - - - - - - - - - ")


        if menu ==  1: 
            pygame.mixer.music.play()
            if timer:
                timer.cancel()
            timer = threading.Timer(30, pygame.mixer.music.stop)
            timer.start()

        elif menu == 2: 
            pygame.mixer.music.pause()
            if timer:
                timer.cancel()

        elif menu == 3: 
            pygame.mixer.music.unpause()

        elif menu == 4: 
            yayList.append(file_path) 

            random_mp3 = random.choice(mp3_files)
            file_path = os.path.join(folder_path, random_mp3)
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()
            MusicData(file_path) 

            if timer:
                timer.cancel()
            timer= threading.Timer(30, pygame.mixer.music.stop)
            timer.start()

        elif menu == 5: 
            nayList.append(file_path)

            random_mp3 = random.choice(mp3_files)
            file_path = os.path.join(folder_path, random_mp3)
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()
            MusicData(file_path)

            if timer:
                timer.cancel()
            timer= threading.Timer(30, pygame.mixer.music.stop)
            timer.start()

        elif menu == 6: 
            menu = 7
            menu2(1, yayList, nayList, folder_path) 
        
        elif menu == 7:
            print("Exiting the music player.")
            break

        else:
            print("Invalid input, please try again.")

def menu2(menu, yayList, nayList, folder_path):  
    mp3_files = [file for file in os.listdir(folder_path) if file.endswith('.mp3')] 

    random_mp3 = random.choice(mp3_files)

    file_path = os.path.join(folder_path, random_mp3)
    pygame.mixer.music.load(file_path)

    MusicData(file_path) 
    while menu != 5: 
        print("- - - - - - - - - - - - ")
        print("1 - Return to Player")
        print("2 - See Yay and Nay List")
        print("3 - Play Yay List")
        print("4 - Play Nay List")
        print("5 - Exit") 
        print("- - - - - - - - - - - - ")

        print("- - - - - - - - - - - - ")
        print()
        menu = int(input("What would you like to do? ")) 
        print()
        print("- - - - - - - - - - - - ")

        if menu == 1: #not working as intended come back to this later
            menu1(0, yayList, nayList, folder_path)

        elif menu == 2: 
            print("Yays: ", yayList)
            print("Nays: ", nayList)

        elif menu == 3: 
            listPlayer(yayList)

        elif menu == 4: 
            listPlayer(nayList)
        elif menu == 5:
            print("Exiting the music player.")
            break
        else:
            print("Invalid input, please try again.")
        
def Player(folder_path, yayList=[], nayList=[] ):
    pygame.mixer.init() 

    folder_path = "C:/Users/green/Music/Music/Sample Music"  #"C:/Users/Emma/Music"
    menu = 0 
    
    menu1(menu, yayList, nayList, folder_path)

    
            

def MusicData(mp3_file):
    cover_folder = r"C:/Users/green/Music/Music/Covers" #"C:/Users/Emma/Music/Covers"
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
