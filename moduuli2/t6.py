# First randomized code: 3 digits and numbers between 0 and 9
# Second randomized code: 4 digits and numbers between 1 and 6

import random

threeDigitRandomFirst = int(random.randint(0, 9))
threeDigitRandomSecond = int(random.randint(0, 9))
threeDigitRandomThird = int(random.randint(0, 9))

fourDigitRandomFirst = int(random.randint(1, 6))
fourDigitRandomSecond = int(random.randint(1, 6))
fourDigitRandomThird = int(random.randint(1, 6))
fourDigitRandomFourth = int(random.randint(1, 6))

print("Random 3-digit number between 0 and 9: " + str(threeDigitRandomFirst) + str(threeDigitRandomSecond) + str(
    threeDigitRandomThird))
print("Random 4-digit number between 1 and 1: " + str(fourDigitRandomFirst) + str(fourDigitRandomSecond) + str(
    fourDigitRandomThird) + str(fourDigitRandomFourth))
