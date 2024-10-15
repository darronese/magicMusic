#import modules note and chord from music 21
from music21 import note

#class Note:
#10/14/24: Moved duration over to chords, figured it would be simpler to adjust rhythym and harmonies
#as I go on...
class Note:
    def __init__(self, pitch, accent):
        self._pitch = pitch
        self._accent = accent

    #getters and setters
    @property
    def pitch(self):
        return self._pitch
    @pitch.setter
    def pitch(self, pitch):
        self._pitch = pitch
    @property
    def accent(self):
        return self._accent
    @accent.setter
    def accent(self, accent):
        self._accent = accent

    #add music 21's feature to play notes

