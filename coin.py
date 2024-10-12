import random

def flip():
    emblem = ''
    flip = random.randint(1, 5)
    if flip == 1 or flip == 2:
        emblem = 'heads'
    elif flip == 3 or flip == 4:
        emblem = 'tails'
    else:
        emblem = 'the coin stood on the edge'
    return emblem
