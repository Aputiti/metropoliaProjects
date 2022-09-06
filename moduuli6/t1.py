import random


def throw_dice():
    random_dice = random.randint(1, 6)
    print(random_dice)
    return random_dice


while throw_dice() != 6:
    throw_dice()
