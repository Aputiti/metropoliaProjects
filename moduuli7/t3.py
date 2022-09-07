whatToDo = input("Valitse:\nuusi lentoasema(ul), aikaisemmin syötetty lentoasema(asl), lopeta(exit): ")

# A few test airports included already in the system
airportSystem = {"AGGO": "Mono Airport",
                 "AGGU": "Marau Airport"}

while whatToDo != "exit":
    if whatToDo == "ul":
        addUlCode = input("Uuden lentoaseman ICAO-koodi (isolla): ")
        addUlName = input("Uuden lentoaseman nimi: ")
        airportSystem[addUlCode] = addUlName
        print(addUlName + " lisätty systeemiin!")
        whatToDo = input("\nValitse:\nuusi lentoasema(ul), aikaisemmin syötetty lentoasema(asl), lopeta(exit): ")
    elif whatToDo == "asl":
        findAslCode = input("Etsi kirjoittamalla lentoaseman ICAO-koodi (isolla): ")
        if findAslCode in airportSystem:
            print(airportSystem[findAslCode])
        else:
            print("No airport with code " + findAslCode + "!")
        whatToDo = input("\nValitse:\nuusi lentoasema(ul), aikaisemmin syötetty lentoasema(asl), lopeta(exit): ")
    else:
        print("\nError, no options for " + whatToDo + "!")
        break
exit()
