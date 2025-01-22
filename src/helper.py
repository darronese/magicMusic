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


#given last note name and by using markov chain dictionary, we can return the next note name by weighted random choice 
#weighted choices are in the dictionary
#returns pitch class names so we can still randomize the octaves and durations
def get_next_note_markov(last_note_name: str, chain: dict) -> str:
    if last_note_name not in chain:
        return random.choice(list(chain.keys()))
    transitions = chain[last_note_name]
    #weighted random choice
    rand_val = random.random()
    cumulative = 0.0
    for next_note, prob in transitions.items():
        cumulative += prob
        if rand_val <= cumulative:
            return next_note

    return random.choice(list(transitions.keys()))
