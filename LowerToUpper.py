# ---------------------------------4. HAFTA, 1. ODEV---------------------------------

userInput = input("\nPlease enter a what you wish to capitalize: ")
userInputUpper = userInput.upper()
print("""
{}   All Capitalized
{}  ----------------->  {}""".format(len(userInput)*' ',userInput,userInputUpper))