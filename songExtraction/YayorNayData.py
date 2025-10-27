#Combination of MusicData2 and MusicPlayer
#Songs information is loaded from the first song is played
#If Next song is clicked the information is loaded and the next song plays
#updated with more menus and playlists 
#added Zimani's timer

#pip install mutagen
#pip3 install pygame

import os
import random 
import pygame #utalized in the music player
import re
import threading #utalized in the timer 

#utalized in pulling the ID3
from mutagen.easyid3 import EasyID3 
from mutagen.id3 import ID3, ID3NoHeaderError 

def Player():
    pygame.mixer.init() 

    folder_path = "C:\Visual Studio Code\Play or Nay\Songs"  #"C:/Users/Emma/Music"

    mp3_files = [file for file in os.listdir(folder_path) if file.endswith('.mp3')] 

    random_mp3 = random.choice(mp3_files)

    file_path = os.path.join(folder_path, random_mp3)
    pygame.mixer.music.load(file_path)

    MusicData(file_path) 

    #the two playlists created for voting yes or no to the songs
    yayList = [] 
    nayList = [] 

    menu = 0 #main menue of the player interface
    menu2 = 0 #the menue used to intereact with the playlists that were created
    count = 0 # I don't think this is doing anything?
    timer = None #timer used to ensure that 30 sec segments are what play not the full song

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


        if menu ==  1: #Play Music/restart current song
            pygame.mixer.music.play()
            if timer:
                timer.cancel()
            timer = threading.Timer(30, pygame.mixer.music.stop)
            timer.start()
            

        if menu == 2: #pause music
            pygame.mixer.music.pause()
            if timer:
                timer.cancel()

        if menu == 3: #unpause 
            pygame.mixer.music.unpause()

        if menu == 4: #Add to the yay playlist and go to the next song
            #add to playlist
            yayList.append(file_path) 

            #select next song and pull the data
            random_mp3 = random.choice(mp3_files)
            file_path = os.path.join(folder_path, random_mp3)
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()
            MusicData(file_path) 

            #30 second timer
            if timer:
                timer.cancel()
            timer= threading.Timer(30, pygame.mixer.music.stop)
            timer.start()

        if menu == 5: #Add to the nay playlist and go to the next song
            #add to playlist
            nayList.append(file_path)

            #select next song and pull the data
            random_mp3 = random.choice(mp3_files)
            file_path = os.path.join(folder_path, random_mp3)
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()
            MusicData(file_path)

            #30 sec timer
            if timer:
                timer.cancel()
            timer= threading.Timer(30, pygame.mixer.music.stop)
            timer.start()

        #move over to the other menu to interact with the playlists (next page)
        if menu == 6: 
            menu = 7
            menu2 = 1 

    while menu2 != 0: #playlist interaction menu
        print("- - - - - - - - - - - - ")
        print("1 - Return to Player")
        print("2 - See Yay and Nay List")
        print("3 - Play Yay List")
        print("4 - Play Nay List")
        print("0 - Exit") 
        print("- - - - - - - - - - - - ")

        print("- - - - - - - - - - - - ")
        print()
        menu2 = int(input("What would you like to do? ")) 
        print()
        print("- - - - - - - - - - - - ")

        if menu2 == 1: #not working as intended come back to this later
            menu2 = 0 
            menu = 0 

        if menu2 == 2: #displays the file paths of the songs in playlist, I was mostly using this to test that they were adding correctly. 
                         #In practice these would just display the name,artist, and cover image and be clickable to the song and maybe another menu.
            print("Yays: ", yayList)
            print("Nays: ", nayList)

        if menu2 == 3: #Play Yay List
            pygame.mixer.music.load(yayList[0]) 

            yayListPlayer = 0 
            nextSong = 0

            #interaction menu for the playlist
            while yayListPlayer != 5:

                print("- - - - - - - - - - - - ")
                print("1 - Play Music/restart current song")
                print("2 - Pause Music")
                print("3 - Resume Music")
                print("4 - Next Song")
                print("5 - Exit") 
                print("- - - - - - - - - - - - ") 


                print("- - - - - - - - - - - - ")
                yayListPlayer = int(input("What would you like to do? "))
                print("- - - - - - - - - - - - ")  

                if yayListPlayer ==  1: 
                    pygame.mixer.music.play()

                if yayListPlayer == 2: 
                    pygame.mixer.music.pause()

                if yayListPlayer == 3: 
                    pygame.mixer.music.unpause()

                if yayListPlayer == 4: #moves to the next song, need to impliment a loop so it doesn't go out of index
                    MusicData(file_path)
                    nextSong += 1

                    file_path = yayList[nextSong] 
                    pygame.mixer.music.load(file_path)
                    pygame.mixer.music.play()
                    MusicData(file_path) 

        if menu2 == 4: 
            pygame.mixer.music.load(nayList[0])

            nayListPlayer = 0 
            nextSong = 0 

            #interaction menu for the playlist
            while nayListPlayer != 5:

                print("- - - - - - - - - - - - ")
                print("1 - Play Music/restart current song")
                print("2 - Pause Music")
                print("3 - Resume Music")
                print("4 - Next song")
                print("5 - Exit") 
                print("- - - - - - - - - - - - ") 


                print("- - - - - - - - - - - - ")
                nayListPlayer = int(input("What would you like to do? "))
                print("- - - - - - - - - - - - ")  

                if nayListPlayer ==  1: 
                    pygame.mixer.music.play()

                if nayListPlayer == 2: 
                    pygame.mixer.music.pause()

                if nayListPlayer == 3: 
                    pygame.mixer.music.unpause()

                if nayListPlayer == 4: #moves to the next song, need to impliment a loop so it doesn't go out of index
                    MusicData(file_path)
                    nextSong += 1

                    file_path = nayList[nextSong] 
                    pygame.mixer.music.load(file_path)
                    pygame.mixer.music.play()
                    MusicData(file_path) 

            
#pulls the title,artist, and album cover information out of the mp3 file 
def MusicData(mp3_file):
    cover_folder = r"C:\Visual Studio Code\Play or Nay\Cover" #"C:/Users/Emma/Music/Covers"
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