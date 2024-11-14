import random

def generate_key(): 
    #get the key we want to start with
    Notes = ["C", "D", "E", "F", "G", "A", "B"]
    Accent = ["♭", "♯", "♮"]
    which_key = random.choice(Notes)
    which_accent = random.choice(Accent)
    key_and_accent = [which_key, which_accent]
    return key_and_accent
