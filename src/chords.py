from music21 import chord 

#class Chord
#10/14/24: I added duration here, figured it would be easy to maintain.
class Chord:
    def __init__(self, notes, duration):
        self._notes = notes
        self._duration = duration

    #getters and setters
    @property
    def notes(self):
        return self._notes

    @notes.setter
    def notes(self, notes):
        self._notes = notes

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, duration):
        self._duration = duration
