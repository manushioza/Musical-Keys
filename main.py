import pygame
import csv
import tkinter as tk
from tkinter import *
from tkinter import ttk


b = []
def create_btns():
    with open('hashmap.csv') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            b.append(tk.Button(content, text=row[1] ,fg="black", width=15, command= lambda s =row[2]: play_sound(s)).grid(column=row[3], row=row[4]))
            
           
def play_sound(name):
    pygame.mixer.init()
    pygame.mixer.music.load("./sounds/" + name)
    pygame.mixer.music.play()



main = Tk()
main.title("Musical Keys")
main.geometry("700x400")
main.columnconfigure(0, weight=1)
main.rowconfigure(0, weight=1)

content = Frame(main,width= 700, height=500, bg='white')
content.grid(padx=50, pady=75)

var = StringVar()
label = Label(main, textvariable=var)
var.set("Click on one of the sounds to get started")
label.grid(pady=50)

create_default_btns()

main.mainloop()

