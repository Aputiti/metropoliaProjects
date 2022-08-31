luxCabinString = str("LUX")
aCabingString = str("A")
bCabinString = str("B")
cCabingString = str("C")

userCabin = str(input("Kirjoita hyttiluokkasi (LUX, A, B tai C): "))

if userCabin == luxCabinString:
    print("LUX on parvekkeellinen hytti yläkannella.")
elif userCabin == aCabingString:
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif userCabin == bCabinString:
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif userCabin == cCabingString:
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka!")

