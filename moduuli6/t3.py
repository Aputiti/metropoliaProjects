# 1 US gallon (liquid) equals 3.785411784 liters

# The code is a bit messy but it works correctly

print("US gallon (liquid) to liter converter:\n")
userGallonAmount = float(input("How many gallons? "))


def gallon_to_liter(gallons_to_convert):
    liters = gallons_to_convert * 3.785411784
    return liters


if userGallonAmount < 0:
    exit()
print(str(gallon_to_liter(userGallonAmount)) + " liters.\n")


while gallon_to_liter(userGallonAmount) >= 0:
    userGallonAmount = float(input("How many gallons? "))
    if userGallonAmount < 0:
        exit()
    print(str(gallon_to_liter(userGallonAmount)) + " liters.\n")
