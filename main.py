import music21
#i don't know why pyright is giving an error to imports even though it works
#pyright: reportPrivateImportUsage=false
from music21 import chord, key, meter, note, stream

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
    print(f"Generated Key: {key_signature.tonic} {key_signature.mode}")
    #generate chords
    chords = measure.generate_chords(progression_name)
    #prints out progression and chord in terminal
    print(f"Progression: {progression_name}")
    for idx, chord_obj in enumerate(chords):
            print(f"Chord {idx + 1}: {chord_obj}")

    #show within midi editor
    s = stream.Stream(chords)
    s.show()

if __name__ == "__main__":
    main()
