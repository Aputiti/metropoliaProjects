realUsername = "python"
realPassword = "rules"

print("Type the username and password, if you guess 5 times wrong all access will be blocked.")

guessedUsername = input("Username: ")
guessedPassword = input("Password: ")

failedGuesses = int(0)

while realUsername != guessedUsername or realPassword != guessedPassword:
    if failedGuesses <= 3:
        print("Wrong username or password, please try again!")
        failedGuesses = failedGuesses + 1
        print("Failed guesses: " + str(failedGuesses))
        guessedUsername = input("Username: ")
        guessedPassword = input("Password: ")
    else:
        print("Access denied!")
        break
if realUsername == guessedUsername and realPassword == guessedPassword:
    print("Welcome!")
