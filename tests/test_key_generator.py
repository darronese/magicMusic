from music21.pitch import Pitch

from generators import key_generator


def test_key_generator():
    key = key_generator.generate_key()

    assert isinstance(key, Pitch), f"Expected Pitch Object, got {type(key)}"

    assert key.step in ["C", "D", "E", "F", "G", "A", "B"], f"Invalid note step: {key.step}"

    if key.accidental:
        assert key.accidental.name in ["flat", "sharp", "natural"], f"Invalid accidental: {key.accidental.name}"

    print(f"Test passed! Generated key: {key.nameWithOctave}")

if __name__ == "__main__":
    test_key_generator()
