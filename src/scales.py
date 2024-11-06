from chords import Chord
from music21 import scale

class Scale(Chord):
    def __init__(self, notes, duration, tonic):
        super().__init__(notes, duration)
        self._tonic = tonic
    
    @property
    def tonic(self):
        return self._tonic

    @tonic.setter
    def tonic(self, tonic):
        self._tonic = tonic
