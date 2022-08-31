kuhaLengthCm = float(input("Kirjoita kuhan pituus senttimetreinä: "))

kuhaLengthTooShort = float(37 - kuhaLengthCm)

if kuhaLengthCm >= 37:
    print("Hyvä, kuha ei ole alamittainen!")
else:
    print("Kuha on alamittainen, se on " + str(kuhaLengthTooShort) + " cm liian lyhyt, minimipituus on 37 cm.")
