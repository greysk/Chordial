import pygame, pygame.mixer, random, os
from tkinter import *
from tkinter import ttk
from pygame import *
from pathlib import Path

Chordial = (r'.\Chord Templates\Midi Progressions')
os.chdir(Chordial)

pygame.init()
pygame.mixer.init()

class Chordial:
    #Calls the random module on the current working directory to return a '.mid' file
    def run(self): 
        mysound = random.choice(os.listdir())
        self.file_label.config(text = mysound)
        pygame.mixer.music.load(mysound)
        pygame.mixer.music.play()
        global file_to_open
        file_to_open = mysound
        return mysound;

    #Opens the chord progression in a new instance of the default program specified for '.mid' files
    def open(self):
        os.startfile(file_to_open)  
     
    #Used to replay the current audio file    
    def replay(self):
        pygame.mixer.music.load(file_to_open)
        pygame.mixer.music.play()
        return

    def __init__(self):
        self.root = Tk()
        self.root.title("Chordial")
        self.frm = ttk.Frame(self.root, padding = 10)
        self.frm.grid()
        ttk.Label(self.frm, text = "Chord Progression Suggester:", font = "Ubuntu").grid(column = 0, row = 0)

        ttk.Button(self.frm, text = "Randomize", command = self.run).grid(column = 1, row = 0)       
        ttk.Button(self.frm, text = "Open in Default", command = self.open).grid(column = 2, row = 0)
        ttk.Button(self.frm, text = "Exit", command = self.root.destroy).grid(column = 3, row = 0)     
        ttk.Button(self.frm, text = "Play Again", command = self.replay).grid(column = 4, row = 0)
        self.file_label = Label(self.root, text = "file name", font = 'Ubuntu')
        self.file_label.grid(column = 0, row = 1)

        self.root.mainloop()

Chordial()