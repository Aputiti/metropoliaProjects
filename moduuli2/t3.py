# Pyrin käyttämään mahdollisimman paljon englannin kieltä, mutta joissain tehtävissä joudun käyttämään suomea

suorakulmioKanta = float(input("Kirjoita suorakulmion kanta (metreinä): "))
suorakulmioKorkeus = float(input(("Kirjoita suorakulmion korkeus (metreinä): ")))

suorakulmioPintaala = float(suorakulmioKanta * suorakulmioKorkeus)
suorakulmioPiiri = float((suorakulmioKanta * 2) + (suorakulmioKorkeus * 2))

print("Suorakulmion pinta-ala on " + str(suorakulmioPintaala) + " m² ja suorakulmion piiri on " +
      str(suorakulmioPiiri) + " metriä")
