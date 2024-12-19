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
    #initialize measure
    new_measure = Measure()
    #generate components
    key = new_measure.generate_key()
    time = new_measure.generate_time()
    note = new_measure.generate_note()

    #create the measure and append the items
    m21_measure = stream.Measure()
    m21_measure.append(time)
    m21_measure.append(key)
    m21_measure.append(note)


    #append the measure to the part from stream
    part = stream.Part()
    part.append(m21_measure)


    #append the part to the score
    score = stream.Score()
    score.append(part)

    # Display the score
    score.show()

if __name__ == "__main__":
    main()
