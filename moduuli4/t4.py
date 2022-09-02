import random

numToGuess = random.randint(1, 10)
# print(str(numToGuess)) - FOR TESTING ONLY!

guessedNumber = int(input("Arvaa luku 1-10: "))

while numToGuess < guessedNumber or numToGuess > guessedNumber or numToGuess == guessedNumber:
    if numToGuess < guessedNumber:
        print("Liian suuri arvaus!")
        guessedNumber = int(input("Arvaa luku 1-10: "))
    elif numToGuess > guessedNumber:
        print("Liian pieni arvaus!")
        guessedNumber = int(input("Arvaa luku 1-10: "))
    else:
        print("Arvasit oikein!")
        break
