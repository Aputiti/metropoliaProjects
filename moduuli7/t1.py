# Months in season
# 3, 4, 5 (kevät)
# 6, 7, 8 (kesä)
# 9, 10, 11 (syksy)
# 12, 1, 2 (talvi)

months = ("kevät", "kesä", "syksy", "talvi")
monthNum = int(input("Kirjoita kuukauden numero (1-12): "))

if monthNum == 3 or monthNum == 4 or monthNum == 5:
    print("Vuodenaika on " + months[0] + "!")
elif monthNum == 6 or monthNum == 7 or monthNum == 8:
    print("Vuodenaika on " + months[1] + "!")
elif monthNum == 9 or monthNum == 10 or monthNum == 11:
    print("Vuodenaika on " + months[2] + "!")
elif monthNum == 12 or monthNum == 1 or monthNum == 2:
    print("Vuodenaika on " + months[3] + "!")
else:
    print("Tapahtui virhe.")
