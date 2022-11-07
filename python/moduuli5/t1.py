import random

diceAmount = int(input("How many dices to roll?: "))
diceSum = int(0)

# Let's assume that a die has six sides.

for i in range(0, diceAmount):
    diceSum += random.randint(1, 6)
print("Rolled " + str(diceAmount) + " dices and the sum of them is " + str(diceSum) + ".")
