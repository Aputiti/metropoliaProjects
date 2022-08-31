# Leap year = karkausvuosi

year = int(input("Type a year to check if it's a leap year: "))

if year % 4 == 0 and year % 100 == 0:
    if year % 400 == 0:
        print("Year " + str(year) + " is a leap year!")
    else:
        print("Year " + str(year) + " is not a leap year!")
elif year % 4 == 0:
    print("Year " + str(year) + " is a leap year!")
else:
    print("Year " + str(year) + " is not a leap year!")
