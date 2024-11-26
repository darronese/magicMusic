import random

from music21 import note


def generate_note(key_and_accent): 
    global int_accidental
    #determine the key and accidental
    key = key_and_accent[0]
    accidental = key_and_accent[1]
