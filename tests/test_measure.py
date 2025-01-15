import pytest
from music21.roman import RomanNumeral

from src.measure import Measure


def test_generate_key():
    measure = Measure()
    generated_key = measure.generate_key()
    assert generated_key is not None, "Key generator returned none"
    assert generated_key.mode in ["major", "minor"], "Key mode is neither major nor minor"

def test_generate_time():
    measure = Measure()
    generated_time = measure.generate_time
    assert generated_time is not None, "Time Signature generation returned none"
    assert hasattr(generated_time, 'numerator'), "Time Signature has no numerator"
    assert hasattr(generated_time, 'denominator'), "Time Signature has no denominator"

def test_generate_chords():
    measure = Measure()
    measure.generate_key()
    measure.generate_time()
    
    progression_name = "Pachabel's Canon"
    chords = measure.generate_chords(progression_name)

    assert len(chords) > 0, "No chords were generated"

    for c in chords:
        assert isinstance(c, RomanNumeral), "Generated chord is not following Roman Numerals"

def test_generate_chords_invalid_progression():
    measure = Measure()
    measure.generate_key()
    measure.generate_time()

    with pytest.raises(ValueError, match=r"Progression .* not found!"):
        measure.generate_chords("InvalidProgressionName")
