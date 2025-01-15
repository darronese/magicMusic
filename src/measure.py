import random
from typing import cast

#pyright: reportPrivateImportUsage=false
from music21 import bar, duration, key, meter, note, roman, stream

from src.chord_progressions import CHORD_PROGRESSIONS
from src.helper import weighted_random_choice


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

    #generate note
    def generate_note(self): 
        pitch = random.choice(['C', 'D', 'E', 'F', 'G', 'A', 'B'])
        octave = random.choice(range(3,7))
        note_name = pitch + str(octave)
        nt = note.Note(note_name)
        nt.duration.quarterLength = random.choice([0.25, 0.5, 1, 2])

        return nt;

    #generates accidental note
    def generate_accidental_note(self):
        n = self.generate_note()
        accidental_type = self.generate_accidental
        n.accidental = accidental_type
        return n

    def generate_note_from_chord(self, symbol, generated_key):
        #ensures key is generated
        if not self.key:
            self.generate_key()
        chord = roman.RomanNumeral(symbol, generated_key)
        chord_pitches = chord.pitches

        #randomly pick within the pitches
        chosen_pitch = random.choice(chord_pitches)
        n = note.Note(chosen_pitch)

        #random length
        n.duration.quarterLength = random.choice([0.25, 0.5, 1, 2])
        return n

        #in the future, i would like to edit this so the user can choose depending on the mood they want the music to be#
        #randomly generate rest: i dont want frequent long rests so here are the percentages
        #eigth: 70%
        #quarter: 20%
        #half: 5%
        #whole: 5%
    def generate_rest(self):
        rest = note.Rest()
        #float in from [0, 100)
        roll = random.random() * 100
        
        #eigth rest
        if roll < 70:
            rest.duration = duration.Duration(0.5)
        #quarter
        elif roll < 90:
            rest.duration = duration.Duration(1.0)
        elif roll < 95:
            rest.duration = duration.Duration(1.0)
        else:
            rest.duration = duration.Duration(4.0)
        return rest

    #generate accidental
    #only one flats/sharps for now#
    def generate_accidental(self):
        accidental_type = random.choice(["sharp", "flat"])
        return accidental_type

    #generates the time signature
    def generate_time(self):
        time = random.choice(['2/4', '3/4', '4/4', '2/8', '3/8', '4/8', '6/8', '2/2', '3/2', '4/2',])
        signature = meter.TimeSignature(time)
        self.time = signature
        return self.time

    #https://www.music21.org/music21docs/moduleReference/moduleBar.html
    def create_bars(self, time):
        #number of beats that can be within a measure
        first_number = time[0][0]
        return first_number


    #generates the random chord progression listed
    def generate_chord_progression(self):
        #range of 32 chord progressions
        progression = random.choice(list(CHORD_PROGRESSIONS.keys()))
        self.progression = progression
        return self.progression

    def generate_musical_event(self, symbol):
        weights = {
            "chord": 0.40,
            "single_note": 0.47,
            "rest": 0.10,
            "accidental": 0.03
        }
        event_type = weighted_random_choice(weights)

        if event_type == "chord":
            return roman.RomanNumeral(symbol, self.key)
        elif event_type == "rest":
            return self.generate_rest()
        elif event_type == "single_note":
            return self.generate_note_from_chord(symbol, self.key)
        elif event_type == "accidental":
            return self.generate_accidental_note()

        #return the regular symbol in key
        return roman.RomanNumeral(symbol, self.key)

    #generates chords based on chord progression
    def generate_chords(self, progression_name):
        #first generate the key if not generated
        if not self.key:
            self.generate_key()

        #generate time
        if not self.time:
            self.generate_time

        progression = CHORD_PROGRESSIONS.get(progression_name)

        #error message for missing progression
        if not progression:
            raise ValueError(f"Progression '{progression_name}' not found!")

        #reset the chords each time
        self.chords = []

        for note in progression:
            try:
                roman_chord = roman.RomanNumeral(note, self.key)
                #random duration
                roman_chord.duration = duration.Duration(random.choice([0.25, 0.5, 1.0, 2.0, 4.0]))
                self.chords.append(roman_chord)
            except Exception as e:
                raise ValueError(f"Error generating chord for symbol '{note}': {e}")
        return self.chords


    #Generates Full Piece#
    #Asks users how many measures they would like to generate
    #1: Ensures key/time are set
    #2: Grabs chord progression
    #3: Fills measures with musical events
    #4: Returns music21 score
    #5: loop this 4 times
    def generate_full_piece(self, progression_name, max_measures):
        #ensure we have a key and time signature
        if not self.key:
            self.generate_key()
        if not self.time:
            self.generate_time()

        progression = CHORD_PROGRESSIONS.get(progression_name)
        if not progression:
            raise ValueError(f"Progression '{progression_name}' not found!")
        
        #create our score and part (what we are displaying)
        score = stream.Score()
        part = stream.Part()

        #build each music elemnet based on the time signature
        beats_per_measure = self.time.barDuration.quarterLength # type: ignore[union-attr]

        #create our first measure and append the time signature
        current_measure = stream.Measure()
        current_measure.append(self.key)
        current_measure_duration = 0.0
        current_measure.append(self.time)

        #current measure count (at least one)
        measure_count = 1

        #loop until we hit max measures
        while measure_count <= max_measures:
            for symbol in progression:
                event = self.generate_musical_event(symbol)
                event_duration = event.duration.quarterLength

                #can our music event fit in our current duration?
                if current_measure_duration + event_duration <= beats_per_measure:
                    current_measure.append(event)
                    current_measure_duration += event_duration
                #if not, append it to the next measure and check if we hit our max measures
                else:
                    part.append(current_measure)
                    measure_count += 1
                    if measure_count > max_measures:
                        break
                    #start a new measure if max measures was not yet reached
                    current_measure = stream.Measure()
                    current_measure_duration = 0.0

                    current_measure.append(event)
                    current_measure_duration += event_duration
            #we finished chord progression, this means we didn't break
            else:
                continue
            #we broke out of for loop, append the rest
            break
        #if we hadn't exceed max_measures and still have events, append it again
        if measure_count <= max_measures and len(current_measure.notesAndRests) > 0:
            part.append(current_measure)

        score.append(part)
        return score
