# Calculating (more like estimating) π using the Monte Carlo method

import random

circlePoints = 0
squarePoints = 0

# 1 million random points is good

n = int(input("How many random points?: "))

# for is better than while for this assignment

for i in range(n):
    random_x = random.uniform(-1, 1)
    random_y = random.uniform(-1, 1)
    originDistance = random_x ** 2 + random_y ** 2

    # Is the random point inside the circle?
    if originDistance <= 1:
        circlePoints = circlePoints + 1
    # if it's not inside circle then it's inside the square!
    squarePoints = squarePoints + 1

    estimatedPi = 4 * circlePoints / squarePoints

print("Simulated Pi is " + str(estimatedPi) + " and real Pi is 3.14159265358979...")
