# 1 inch (tuuma) = 2.54 cm

print("Ohjelma muuttaa annetut tuumat senttimetreiksi. "
      "Jos annat negatiivisen arvon tuumille, ohjelma lopettaa toimintansa!")

inchToConvert = float(input("Kirjoita tuumat: "))

while inchToConvert >= 0:
      print(str(inchToConvert) + " tuumaa on = " + str(inchToConvert * 2.54) + " senttimetriä.")
      inchToConvert = float(input("Kirjoita tuumat: "))
print("Ohjelma pysäytetty!")
