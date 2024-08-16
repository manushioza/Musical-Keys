import pygame, csv, os, shutil
import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd


b = []
def create_btns():
    with open('hashmap.csv') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            b.append(tk.Button(content, text=row[0] ,fg="black", width=15, command= lambda s =row[1]: play_sound(s)).grid(column=row[2], row=row[3]))
            
           
def play_sound(name):
    pygame.mixer.init()
    pygame.mixer.music.load("./sounds/" + name)
    pygame.mixer.music.play()

def add_to_hashmap(sound_name):
    with open('hashmap.csv', 'r') as f:
        reader = list(csv.reader(f, delimiter=','))
        last_line = reader[-1]
        second_last_line = reader[-2]
        col, row = 0,0
        if last_line[2] == 0:
            col = 1

        if last_line[3] == second_last_line[3]:
            row = int(last_line[3]) + 1
        else:
            row = last_line[3]
        f.close()

    with open('hashmap.csv', 'a', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        sound_name
        new_button = [sound_name.replace('.mp3', ''), sound_name, col, row]
        writer.writerow(new_button)
        f.close()

        return True

def move_file(src, des):
    shutil.move(src, des + "/sounds")

      
def add_sound():
    sound_path = fd.askopenfilename();
    current_path = os.path.dirname(__file__)
    print(sound_path,current_path)
    sound_name = os.path.basename(sound_path)

    move_file(sound_path,current_path)
    if add_to_hashmap(sound_name):
        create_btns()

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
label.grid(pady=40)

Button(main, text="+" ,fg="blue", width=1, command=add_sound).grid(row=2, column=2, sticky='e', padx= 10, pady=10)

create_btns()

main.mainloop()

