#fix time signature, 2/4, 4/4, 6/8,
#add bpm
#make more measures

import music21

from music.measure import Measure

#user settings
us = music21.environment.UserSettings()
#where my musescore is located
us['musicxmlPath'] = '/Applications/MuseScore 4.app/'

def main():
    new_measure = Measure()
    key = new_measure.generate_key()
    note = new_measure.generate_note()
    note.show()


if __name__ == "__main__":
    main()
