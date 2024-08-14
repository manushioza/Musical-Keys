from tkinter import *
from tkinter import ttk

main = Tk()
main.title("Musical Keys")
main.geometry("1000x700")
main.columnconfigure(0, weight=1)
main.rowconfigure(0, weight=1)

content = Frame(main,width= 700, height=500, bg='white')


default_sound_1 = Button(content, text="Evil Laugh" ,fg="black", width=15)
default_sound_2 = Button(content, text="Crickets" ,fg="black", width=15)
default_sound_3 = Button(content, text="Drums" ,fg="black", width=15)
default_sound_4 = Button(content, text="Clap" ,fg="black", width=15)
default_sound_5 = Button(content, text="Womp-womp" ,fg="black", width=15)
default_sound_6 = Button(content, text="Cheers" ,fg="black", width=15)

default_sound_1.pack()
default_sound_2.pack()
default_sound_3.pack()
default_sound_4.pack()
default_sound_5.pack()
default_sound_6.pack()


content.pack(padx=100, pady=150)





main.mainloop()