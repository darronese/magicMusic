import random

#pyright: reportPrivateImportUsage=false
from music21 import chord, key, meter, roman

from src.chord_progressions import CHORD_PROGRESSIONS


class Measure:
    #constructor
    def __init__(self):
        self.key = None
        self.time = None
        self.progression = None
        self.chords = []

    #generates the key for the chords
    def generate_key(self): 
        sharps_or_flats = random.choice(range(-7, 8))
        mode = random.choice(['major', 'minor'])

        if mode == 'major':
            self.key = key.KeySignature(sharps_or_flats).asKey(mode='major')
        else:
            self.key = key.KeySignature(sharps_or_flats).asKey(mode='minor')
        return self.key

    #generates the time signature
    def generate_time(self):
        time = random.choice(['2/4', '3/4', '4/4', '2/8', '3/8', '4/8', '6/8', '2/2', '3/2', '4/2',])
        signature = meter.TimeSignature(time)
        self.time = signature
        return self.time

    #generates the random chord progression listed
    def generate_chord_progression(self):
        #range of 32 chord progressions
        progression = random.choice(range(1, 32))
        self.progression = progression
        return self.progression

    #generates chords based on chord progression
    def generate_chords(self, progression_name):
        #if key is empty, generate a key
        if not self.key:
            self.generate_key()

        progression = CHORD_PROGRESSIONS.get(progression_name)
        #error message for missing progression
        if not progression:
            raise ValueError(f"Progression '{progression_name}' not found!")

        for note in progression:
            try:
                roman_chord = roman.RomanNumeral(note, self.key)
                self.chords.append(roman_chord)
            except Exception as e:
                raise ValueError(f"Error generating chord for symbol '{note}': {e}")
        return self.chords
