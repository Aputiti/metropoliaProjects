# Calculating the area of a circle area using its radius

import math

circleRadiusMeter = input("Insert the radius of the circle (meters): ")
circleRadiusMeterFloat = float(circleRadiusMeter)

circleArea = float(math.pi * (circleRadiusMeterFloat * circleRadiusMeterFloat))

print("The area of the circle is: " + str(circleArea) + " m²")
