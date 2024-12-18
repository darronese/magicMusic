import pytest
from music21 import key, note

from music.measure import Measure


#https://docs.pytest.org/en/6.2.x/fixture.html
@pytest.fixture
def measure():
   return Measure()

def test_generate_key(measure):
    generated_key = measure.generate_key()
    #test that it returns a key signature
    assert isinstance(generated_key, key.KeySignature), "Generate Key should return a key signature"
    #test that the key signature is within valid range
    assert -7 <= generated_key.sharps <= 7, "Key signature is between -7 and 7"
    
def test_generate_note(measure):
    generated_note = measure.generate_note()
    #test that it returns a note object
    assert isinstance(generated_note, note.Note), "Generate note should return a note"
    #test that it has a valid pitch
    assert generated_note.name[0] in 'CDEFGAB', "Note name should be one of the notes listed"
    #test that the octave is in range
    assert 3 <= generated_note.octave <= 6, "Note octave should be between 3 and 6"
    #test that the duration is one of the quarter lenghts
    assert generated_note.duration.quarterLength in [0.25, 0.5, 1, 2], "Note duration should be valid"

