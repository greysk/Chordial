import random
import os
import tkinter as tk
from tkinter import ttk, StringVar
from pathlib import Path

import pygame

# Absolute path to the directory containing chord progression files.
# The equivalent relative path is './Midi Progressions"
CHORDIAL = Path(__file__).parents[1] / 'Midi Progressions'


class ProgramBody(ttk.Frame):
    def __init__(self, midi_directory, title='Chordial'):
        """
        Sets up pygame and Tkinter for Chordial: chord progression suggester.
        
        With Chordial you can select and play random .mid from chords_dir.        
        It also allows you to conveniently open a selected .mid file using the
        default program for .mid files.
        
        Chordial program can be run by calling mainloop() on an instance of this class.
  
        Args:
            chords_dir (Pathlike):
                Path to directory containing chord progression .mid file.
            title (str, optional): Title for root tk window. Defaults to 'Chordial'.
        """
        super().__init__(master=tk.Tk(), padding=10)
       
        # All .mid files in Midi Progressions.
        self.sound_files = list(Path(midi_dir).glob('*.mid'))
        
        # Set by self.select_file() to hold current chord progression.
        self.file_to_open = None
        # Used in self.select_file() to automatically update Frame label.
        self.file_label = StringVar()
        
        # Set up basics for Tkinter.
        self.root = root
        self.root.title(title)
        self.grid()
        self._create_widgets()
        
        # Initialize pygame.music needed by self.run() and self.replay()
        pygame.mixer.init()
    
    def _create_widgets(self):
        """Set up Tkinter window labels and buttons.
        """
        ttk.Label(self, text="Chord Progression Suggester:", font="Ubuntu"
                  ).grid(column=0, row=0)
        # Label for chord progression filename.
        tk.Label(self.root, text="file name", textvariable=self.file_label,
                 font='Ubuntu').grid(column=0, row=1)
        
        # Randomize button - selects current sound.
        ttk.Button(self, text="Randomize", command=self.run
                   ).grid(column=1, row=0)
        # Open in default button - opens current sound using default program.
        ttk.Button(self, text="Open in Default", command=self.open
                   ).grid(column=2, row=0)
        # Play again button - Starts playing current sound from the beginning.
        ttk.Button(self, text="Play Again", command=self.replay
                   ).grid(column=3, row=0)
        # Exit button - closes Tkinter window.
        ttk.Button(self, text="Exit", command=self.root.destroy
                   ).grid(column=4, row=0)

    def select_file(self):
        """Select a random .mid file from chords_dir. Update filename label.
        """
        self.file_to_open = random.choice(self.sound_files)
        # Set current sound label in Tkinter window
        self.file_label.set(self.file_to_open)
        
    def run(self):
        """Play random sound from chords_dir and update filename label.
        
        Uses self.select_file().
        """
        self.select_file()
        pygame.mixer.music.load(mysound)
        pygame.mixer.music.play()

    def open(self):
        """Open chord progression in the default program for .mid files.
        """
        if self.file_to_open is not None:
            os.startfile(self.file_to_open)

    def replay(self):
        """Replay the current chord progression.
        """
        if self.file_to_open is not None:
            pygame.mixer.music.play()


if __name__ == '__main__'':
    chordial_app = ProgramBody(midi_directory=CHORDIAL)
    # Run cordial application loop.
    chordial_app.mainloop()
