from tkinter import *
from tkinter import ttk
import pygame

main = Tk()
main.title("Musical Keys")
main.geometry("1000x700")
main.columnconfigure(0, weight=1)
main.rowconfigure(0, weight=1)

content = Frame(main,width= 700, height=500, bg='white')
content.grid(padx=100, pady=150)

# var = StringVar()
# label = Label(content, textvariable=var)
# var.set("Click on one of the sounds below for some fun")
# label.grid()


pygame.mixer.init()

def play_sound1():
   pygame.mixer.music.load("./sounds/evil-laugh-89423.mp3")
   pygame.mixer.music.play()
def play_sound2():
   pygame.mixer.music.load("./sounds/cricket-sound-113945.mp3")
   pygame.mixer.music.play()

def play_sound3():
   pygame.mixer.music.load("./sounds/ba-dum-tss-8279.mp3")
   pygame.mixer.music.play()

def play_sound4():
   pygame.mixer.music.load("./sounds/small-applause-6695.mp3")
   pygame.mixer.music.play()

def play_sound5():
   pygame.mixer.music.load("./sounds/cartoon-scream-1-6835.mp3")
   pygame.mixer.music.play()

def play_sound6():
   pygame.mixer.music.load("./sounds/yay-6326.mp3")
   pygame.mixer.music.play()


default_sound_1 = Button(content, text="Evil Laugh" ,fg="black", width=15, command=play_sound1)
default_sound_2 = Button(content, text="Crickets" ,fg="black", width=15, command=play_sound2)
default_sound_3 = Button(content, text="Drums" ,fg="black", width=15, command=play_sound3)
default_sound_4 = Button(content, text="Clap" ,fg="black", width=15, command=play_sound4)
default_sound_5 = Button(content, text="Scream" ,fg="black", width=15, command=play_sound5)
default_sound_6 = Button(content, text="Yay" ,fg="black", width=15, command=play_sound6)

default_sound_1.grid(column = 0, row = 0)
default_sound_2.grid(column = 1, row = 0)
default_sound_3.grid(column = 0, row = 1)
default_sound_4.grid(column = 1, row = 1)
default_sound_5.grid(column = 0, row = 2)
default_sound_6.grid(column = 1, row = 2)






main.mainloop()