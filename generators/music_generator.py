import random
from music21 import stream, note, chord, key, meter, tempo, instrument

class MusicGenerator:
    def __init__(self, key, chords, tempo, rest_notes):
        self.key = key
        self.chords = chords
        self.tempo = tempo
        self.rest_notes = rest_notes
