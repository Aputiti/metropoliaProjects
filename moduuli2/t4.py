number1 = int(input("Kirjoita yksi kokonaisluku: "))
number2 = int(input("Kirjoita toinen kokonaisluku: "))
number3 = int(input("Kirjoita kolmas kokonaisluku: "))

numbersSum = int(number1 + number2 + number3)
numbersProduct = int(number1 * number2 * number3)
numbersAverageValue = int((number1 + number2 + number3) / 3)

print("Lukujen summa: " + str(numbersSum) + ", lukujen tulo: " + str(numbersProduct) + ", lukujen keskiarvo: " + str(
    numbersAverageValue))
