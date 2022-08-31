userGender = str(input("Are you a male of female? "))
userHemoglobin = int(input("Input your hemoglobin level (g/l): "))

userIsMale = str("male")
userIsFemale = str("female")

if userGender == userIsMale and 134 <= userHemoglobin <= 195:
    print("Hemoglobin levels normal (male)!")
elif userGender == userIsMale and userHemoglobin < 134:
    print("Hemoglobin levels too low (male)!")
elif userGender == userIsMale and userHemoglobin > 195:
    print("Hemoglobin levels too high (male)!")
elif userGender == userIsFemale and 117 <= userHemoglobin <= 175:
    print("Hemoglobin levels normal (female)!")
elif userGender == userIsFemale and userHemoglobin < 117:
    print("Hemoglobin levels too low (female)!")
elif userGender == userIsFemale and userHemoglobin > 175:
    print("Hemoglobin levels too high (female)!")
else:
    print("Error!")
