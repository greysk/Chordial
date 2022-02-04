import pygame, pygame.mixer, random, os
from hi import file_name
from tkinter import *
from tkinter import ttk
from pygame import *
from pathlib import Path

Chordial = Path(r'C:\Users\bretm\source\repos\Chordial\Chord Templates\Midi Progressions')
os.chdir(Chordial)


pygame.init()
pygame.mixer.init()

def run(): 
        mysound = random.choice(os.listdir(r"C:\Users\bretm\source\repos\Chordial\Chord Templates\Midi Progressions"))
        print(mysound)
        pygame.mixer.music.load(mysound)
        pygame.mixer.music.play()

root = Tk()
root.title("Chordial")
frm = ttk.Frame(root, padding = 10)
frm.grid()
ttk.Label(frm, text = "Chord Progression Suggester:").grid(column = 0, row = 0)
ttk.Button(frm, text = "Exit", command = root.destroy).grid(column = 2, row = 0)
ttk.Button(frm, text = "Randomize", command = run).grid(column = 1, row = 0)
#ttk.Label(frm, text = file_name).grid(column = 0, row = 0)

canvas = Canvas(root, width = 350, height = 175)
canvas.create_text(180, 50, text = "Progression:", fill="black", font=('Helvetica 15 bold'))
canvas.create_text(180, 70, text = file_name, fill="black", font=('Helvetica 15 bold'))
canvas.grid(row = 2, column = 0)

root.mainloop()