#TO-DO:
#- Change length of notes
#- Add in more chords, seperate the chords with bars,
#- Integrate separate notes
#- Integrate seperate parts: different notes mixed in with chords

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
    #testing progression
    progression_name = measure.generate_chord_progression()
    print(f"Progression: {progression_name}")
    score = measure.generate_full_piece(progression_name)
    score.show()


if __name__ == "__main__":
    main()
