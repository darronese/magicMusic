import random

#For randomizing logic, here are the percentage#
#Chords: 50%#
#Single Notes: 30%#
#Rest: 15%#
#Accidentals 5%#

def weighted_random_choice(weights):
    total = sum(weights.values())
    r = random.uniform(0, total)
    cumulative = 0.0
    for event_type, w in weights.items():
        cumulative += w
        if r < cumulative:
            return event_type
    return None

