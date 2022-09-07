print("Syötä nimiä (kopiot ei sallittuja) ja lopuksi syötä tyhjä merkkijono.")
names = {""}
addName = input("Kerro nimi: ")

while addName != "":
    if addName in names:
        print("Aiemmin syötetty nimi!\n")
        addName = input("Kerro nimi: ")
    else:
        print("Uusi nimi lisätty!\n")
        names.add(addName)
        addName = input("Kerro nimi: ")
names.remove("")

print("\nSyötetyt nimet: ")
for i in names:
    print(i)
