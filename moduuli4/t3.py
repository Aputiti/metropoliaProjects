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
