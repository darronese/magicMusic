import random

from music21 import chord, instrument, key, meter, note, stream, tempo


class Measure:
    def __init__(self, key, chord, notes, measure, time_signature):
        self.key = key
        self.chord = chord
        self.notes = notes
        self.measure = measure
        self.time_signature = time_signature

    def generate_key(self): 
        key_signature = key.KeySignature(random.choice(range(0-7)))
        return key_signature

    def generate_note(self): 
        #Random note
        nt = random.choice(['C', 'D', 'E', 'F', 'G', 'A', 'B'])
        #random octave
        octave = random.choice(range(3,7))

    def create_starting_measure(self):
        self.measure.insert(0, key)
        self.measure.insert(0, key)
        self.measure.insert(0, key)
