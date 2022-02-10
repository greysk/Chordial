import random
import os
import tkinter as tk
from tkinter import ttk, StringVar
from pathlib import Path

import pygame

# Absolute path to the directory containing chord progression files.
# The equivalent relative path is './Midi Progressions"
CHORDIAL = Path(__file__).parents[1] / 'Midi Progressions'


class ProgramBody:
    def __init__(self, midi_directory):
        """Main instance of the program."""
       
        # All .mid files in Midi Progressions.
        self.sound_files = list(Path(midi_dir).glob('*.mid'))
        
        # Set by self.run() to hold current chord progression.
        self.file_to_open = None
        # Used in self.run() to automatically update Frame label.
        self.file_label = StringVar()
        
        # Set up basics for Tkinter
        self.root = tk.Tk()
        self.root.title("Chordial")
        self.frm = ttk.Frame(self.root, padding=10)
        self.frm.grid()
        self._create_widgets()
        
        # Initialize pygame.music needed by self.run() and self.replay()
        pygame.mixer.init()
        
        # Run Tk().mainloop()
        self.root.mainloop()
    
    def _create_widgets(self):
        """Set up Tkinter window buttons and labels.
        """
        ttk.Label(self.frm, text="Chord Progression Suggester:", font="Ubuntu"
                  ).grid(column=0, row=0)
        # Label for chord progression filename.
        tk.Label(self.root, text="file name", textvariable=self.file_label,
                 font='Ubuntu').grid(column=0, row=1)
        # Randomize button - selects current sound.
        ttk.Button(self.frm, text="Randomize", command=self.run
                   ).grid(column=1, row=0)
        # Open in default button - opens current sound using default program.
        ttk.Button(self.frm, text="Open in Default", command=self.open
                   ).grid(column=2, row=0)
        # Exit button - closes Tkinter window.
        ttk.Button(self.frm, text="Exit", command=self.root.destroy
                   ).grid(column=3, row=0)

    def run(self):
        """
        Select and play a random '.mid' file from the current working
        directory as well as updates the label.
        """
        mysound = random.choice(self.sound_files)
        pygame.mixer.music.load(mysound)
        pygame.mixer.music.play()
        self.file_to_open = mysound
        self.file_label.set(self.mysound.stem)

    def open(self):
        """
        Opens the chord progression in a new instance of the default program
        specified for '.mid' files.
        """
        os.startfile(self.file_to_open)

    def replay(self):
        """Used to replay the current audio file."""
        pygame.mixer.music.play()


ProgramBody(midi_directory=CHORDIAL)
