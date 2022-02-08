import pygame, pygame.mixer, random, os, threading, subprocess
from tkinter import *
from tkinter import ttk
from pygame import *
from pathlib import Path

Chordial = Path('.\Midi Progressions')
os.chdir(Chordial)

pygame.init()
pygame.mixer.init()

class program_body:

    #Selects and plays a random '.mid' file from the current working directory as well as updates the label
    def run(self, *args): 
        self.mysound = random.choice(os.listdir())
        self.file_label.config(text = self.mysound)
        pygame.mixer.music.load(self.mysound)
        pygame.mixer.music.play()
        self.file_to_open = self.mysound
        self.file_label.config(text = self.mysound.replace('.mid',''))
        return self.file_label

    #Opens the chord progression in a new instance of the default program specified for '.mid' files
    def open(self, args=(1)):
        #self.key = b'self.file_to_open'
        #self.value = os.getenvb(self.key)
        #print(self.value)
        #subprocess.run(['J:\Studio One\Studio One 5\Studio One.exe', self.file_to_open])
        os.startfile(self.file_to_open)
        #x = threading.Thread(target = open, args=(1,))
        #x.start()
     
        #Used to replay the current audio file    
    def replay(self, *args):
        pygame.mixer.music.load(self.file_to_open)
        pygame.mixer.music.play()
        return

        #main instance of the program 
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

program_body()
