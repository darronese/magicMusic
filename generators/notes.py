import random

from music21 import note


def generate_note(key_and_accent): 
    global int_accidental
    #determine the accidental
    key = key_and_accent[0]
    accidental = key_and_accent[1]
    
    #let 0 = no accidental, 1 = flat, 2 = sharp
    if accidental == "♮":
        int_accidental = 0
    if accidental == "♭":
        int_accidental = 1
    if accidental == "♯":
        int_accidental = 2
    else:
        print("Error generating accidental value in notes.py!")

