import random

#pyright: reportPrivateImportUsage=false
from music21 import duration, key, meter, note, roman, stream

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
        #Random note
        pitch = random.choice(['C', 'D', 'E', 'F', 'G', 'A', 'B'])
        #random octave
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
            "chord": 0.50,
            "single_note": 0.30,
            "rest": 0.15,
            "accidental": 0.05
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
                random_duration = random.choice([0.25, 0.5, 1.0, 2.0, 4.0])
                roman_chord.duration = duration.Duration(random_duration)
                self.chords.append(roman_chord)
            except Exception as e:
                raise ValueError(f"Error generating chord for symbol '{note}': {e}")
        return self.chords
    #Generates Full Piece#
    #1: Ensures key/time are set
    #2: Grabs chord progression
    #3: Fills measures with musical events
    #4: Returns music21 score
    #5: loop this 4 times
    def generate_full_piece(self, progression_name):
        """
        Generates a full piece by:
        1. Ensuring key/time are set,
        2. Grabbing the chord progression,
        3. Filling measures with musical events (some from the chord progression),
        4. Returning a music21 Score containing a Part of Measures.
        """
        # Ensure we have a key and time signature
        if not self.key:
            self.generate_key()
        if not self.time:
            self.generate_time()

        progression = CHORD_PROGRESSIONS.get(progression_name)
        if not progression:
            raise ValueError(f"Progression '{progression_name}' not found!")
        
        # Create a Score and a Part to hold the measures
        score = stream.Score()
        part = stream.Part()

        # We'll build measures according to the time signature
        beats_per_measure = self.time.numerator  # e.g., 4 in 4/4

        current_measure = stream.Measure()
        current_measure_duration = 0.0

        # Optionally, place the time signature in the first measure
        current_measure.append(self.time)

        repeats = 4

        for _ in range(repeats):
            # Iterate over each chord symbol in the progression
            for symbol in progression:
                # We might want to generate *one* musical event for each chord symbol,
                # or generate multiple events. Below is *one* event per symbol.
                event = self.generate_musical_event(symbol)
                
                # The event's duration in quarter notes
                event_duration = event.duration.quarterLength

                # Check if this event still fits in the current measure
                if current_measure_duration + event_duration <= beats_per_measure:
                    # Add the event to the measure
                    current_measure.append(event)
                    current_measure_duration += event_duration
                else:
                    # The measure is "full" (or will overflow), so wrap it up
                    part.append(current_measure)

                    # Create a new measure
                    current_measure = stream.Measure()
                    current_measure_duration = 0.0

                    # Start the new measure with the current event
                    current_measure.append(event)
                    current_measure_duration += event_duration

        # After the loop, if there are any leftover events in the measure, add them
        if len(current_measure.notesAndRests) > 0:
            part.append(current_measure)

        # Finally, put the part into the score
        score.append(part)

        return score
