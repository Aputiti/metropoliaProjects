import random


def throw_dice(side_max):
    random_dice = random.randint(1, side_max)
    print(random_dice)
    return random_dice


userSideMax = int(input("Valitse nopan tahkojen yhteismäärä: "))


while throw_dice(userSideMax) != userSideMax:
    throw_dice(userSideMax)
