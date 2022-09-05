# This code could be better (had a problem with mixing strings and integers)
# Also only numbers between -99 and 99 work (+ some exceptions)

# CODE LOGIC DONE BETTER IN MODUULI 5 (t2) - SIMILAR ASSIGNMENT

print("Syötä lukuja ja kun olet valmis, syötä tyhjä merkkijono.")
print("Tämän jälkeen ohjelma tulostaa annetuista luvuista suurimman ja pienimmän.")

userInputNum = input("Syötä luku: ")
userNumList = [userInputNum]

while userInputNum != "":
    userInputNum = input("Syötä luku: ")
    userNumList.append(userInputNum)
userNumList.pop()
userNumList.sort()

print("Suurin luku on " + str(max(userNumList)) + " ja pienin luku on " + str(userNumList[0]))
