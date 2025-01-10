#TO-DO:
#- Add in more chords, seperate the chords with bars,
#- Integrate separate notes
#- Change length of notes

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
    progression_name = "Pachelbel's Canon"  # Change this to test other progressions
    #progression_name = measure.generate_chord_progression()

    key_signature = measure.generate_key()
    tempo = measure.generate_time()
    print(f"Generated Key: {key_signature.tonic} {key_signature.mode}")
    #generate chords
    chords = measure.generate_chords(progression_name)
    #prints out progression and chord in terminal for testing
    print(f"Progression: {progression_name}")
    for idx, chord_obj in enumerate(chords):
            print(f"Chord {idx + 1}: {chord_obj}")

    #test directly#
    #s = stream.Stream(chords)#

    #first measure
    f_measure = stream.Measure()
    f_measure.append(key_signature)
    f_measure.append(tempo)
    f_measure.append(chords)

    #show within midi editor
    part = stream.Part()
    part.append(f_measure)

    score = stream.Score()
    score.append(part)

    score.show()

if __name__ == "__main__":
    main()
