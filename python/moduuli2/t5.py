# This code could be simpler

import math

leiviska = input('Anna leiviskät: ')
naulat = input('Anna naulat: ')
luodit = input('Anna luodit: ')

leiviskaMultiplier = float(leiviska)
naulaMultiplier = float(naulat)
luotiMultiplier = float(luodit)

luotiGrammat = float(13.3)

leiviskaWeight = float(leiviskaMultiplier * (20 * 32 * 13.3))
naulaWeight = float(naulaMultiplier * (32 * 13.3))
luotiWeight = float(luotiMultiplier * luotiGrammat)

combinedWeightGrams = leiviskaWeight + naulaWeight + luotiWeight
combinedWeightGramsString = str(combinedWeightGrams)
combinedWeightKilograms = (combinedWeightGrams / 1000)
combinedWeightKilogramsString = str(combinedWeightKilograms)
combinedWeightKilogramsStringMain = math.floor(combinedWeightKilograms)

combinedWeightInGrams = float(combinedWeightGrams - (math.floor(combinedWeightKilograms) * 1000))

print("Massa nykymittojen mukaan: " + str(combinedWeightKilogramsStringMain) + " kilogrammaa ja " + str(
    combinedWeightInGrams) + " grammaa.")
