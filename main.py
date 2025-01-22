#TO-DO:
# 1: Test more of measure.py using pytest
# 2: Depending on the denominator of the time signature, change the odds of the note duration, e.g 4/4: more quarter notes, 6/8: more eigth notes, etc
# 3: Add bass clef corresponding to treble's progression
# 4: Feature where user can pick out the measure(s) they like the most, save it into a file

import music21
#i don't know why pyright is giving an error to imports even though it works
#pyright: reportPrivateImportUsage=false
from music21 import stream

from src.measure import Measure

#user settings
us = music21.environment.UserSettings()
#where my musescore is located
us['musicxmlPath'] = '/Applications/MuseScore 4.app/'

def main():
    measure = Measure()
    num_measures = 1
    progression_name = measure.generate_chord_progression()
    print(f"Progression: {progression_name}")
    #input validation loop: asks user for the amount of measures they would like to generate#
    while True:
        user_input = input("How many measures would you like to generate(has to be at least one): ").strip()
        try:
            num_measures = int(user_input)
            if num_measures >= 1:
                break
            else:
                print("Please enter an integer >= 1")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    score = measure.generate_full_piece(progression_name, num_measures)
    score.show()


if __name__ == "__main__":
    main()
