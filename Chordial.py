import random
import os
import tkinter as tk
from tkinter import ttk, StringVar
from pathlib import Path

import pygame

# Absolute path to the directory containing chord progression files.
# The equivalent relative path is './Midi Progressions"
CHORDIAL = Path(__file__).parents[1] / 'Midi Progressions'

pygame.mixer.init()


class ProgramBody:
    def __init__(self):
        """Main instance of the program."""
        self.root = tk.Tk()
        self.root.title("Chordial")
        self.frm = ttk.Frame(self.root, padding=10)
        self.frm.grid()
        ttk.Label(self.frm, text="Chord Progression Suggester:", font="Ubuntu"
                  ).grid(column=0, row=0)
        ttk.Button(self.frm, text="Randomize", command=self.run).grid(column=1,
                                                                      row=0)
        ttk.Button(self.frm, text="Open in Default", command=self.open
                   ).grid(column=2, row=0)
        ttk.Button(self.frm, text="Exit", command=self.root.destroy
                   ).grid(column=3, row=0)
        ttk.Button(self.frm, text="Play Again", command=self.replay
                   ).grid(column=4, row=0)
        self.file_label = tk.Label(self.root, text="file name", font='Ubuntu')
        self.file_label.grid(column=0, row=1)
        
        # All .mid files in Midi Progressions.
        self.sound_files = list(self.chords_dir.glob('*.mid'))
        
        self.file_to_open = None

        self.root.mainloop()

    def run(self):
        """
        Select and play a random '.mid' file from the current working
        directory as well as updates the label.
        """
        mysound = random.choice(self.sound_files)
        pygame.mixer.music.load(mysound)
        pygame.mixer.music.play()
        self.file_to_open = mysound
        pygame.mixer.music.load(self.mysound, "mid")

    def open(self):
        """
        Opens the chord progression in a new instance of the default program
        specified for '.mid' files.
        """
        os.startfile(self.file_to_open)

    def replay(self):
        """Used to replay the current audio file."""
        pygame.mixer.music.play()


ProgramBody()
