import random

#pyright: reportPrivateImportUsage=false
from music21 import chord, key, meter, note


class Measure:
    def __init__(self, measure=None, time_signature=None):
        self.key = None
        self.chord = None
        self.notes = []
        self.measure = measure
        self.time_signature = time_signature

    def generate_key(self): 
        key_signature = key.KeySignature(random.choice(range(-7, 8)))
        return key_signature

    def generate_note(self): 
        #Random note
        pitch = random.choice(['C', 'D', 'E', 'F', 'G', 'A', 'B'])
        number = random.choice(['0', '1', '2', '3', '4', '5', '6', '7'])
        #random octave
        octave = random.choice(range(3,7))
        #add on accidentals later: maybe have a certain amount per 4 measures
        accidental = random.choice([None, '#', 'b'])

        note_name = pitch + str(octave)

        nt = note.Note(note_name)

        nt.duration.quarterLength = random.choice([0.25, 0.5, 1, 2])

        return nt;

    def generate_time(self):
        time = random.choice(['2/4', '3/4', '4/4', '2/8', '3/8', '4/8', '6/8', '2/2', '3/2', '4/2',])
        signature = meter.TimeSignature(time)
        return signature

    def generate_chords(self):
        #generate chords together based on chord progression

    def generate_new_measure(self):
        #parse time signature to get first number
        #loop to generate chords and notes until measure is completed
