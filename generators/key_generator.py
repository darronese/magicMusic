import random

from music21 import note, pitch, stream


def generate_key(): 
    #get the key we want to start with
    Notes = ["C", "D", "E", "F", "G", "A", "B"]
    Accent = ["♭", "♯", None]
    #randomly choose a note and accent
    which_key = random.choice(Notes)
    which_accent = random.choice(Accent)
    #combine key and accidental
    if which_accent:
        key_with_accent = f"{which_key}{which_accent}"
    else:
        key_with_accent = which_key
    key_pitch = pitch.Pitch(key_with_accent)
    return key_pitch
