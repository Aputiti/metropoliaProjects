isNotPrimeNum = False
userNum = int(input("Check if this number is a prime number: "))

if userNum > 1:
    for i in range(2, userNum):
        # If there is a number found that is exactly divisible by something else than one and the userNum itself
        if userNum % i == 0:
            isNotPrimeNum = True
            break
    if isNotPrimeNum:
        print(str(userNum) + " is not a prime number.")
    else:
        print(str(userNum) + " is a prime number.")
else:
    print(str(userNum) + " is not a prime number.")
