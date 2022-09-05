# There is a similar assignment in moduuli 4 (t3) that I didn't do very well,
# but this one is better

print("\nSyötä lukuja ja kun olet valmis, syötä tyhjä merkkijono.\n"
      "Tämän jälkeen ohjelma tulostaa annetuista luvuista viisi suurinta.\n")

userNumberListString = []
userNumberListInt = []
userNumber = (input("Syötä luku: "))

while userNumber != "":
    userNumberListString.append(userNumber)
    userNumber = (input("Syötä luku: "))

# Doing this to not get errors on mixing up strings and integers in while loop
for i in userNumberListString:
    userNumberListInt.append(int(i))

userNumberListInt.sort(reverse=True)
print("Syötettyjen lukujen viisi suurinta lukua: " + str(userNumberListInt[0:5]))
