# _______________________________5.Hafta, 2.Odev_______________________________

number = "5487"
answer = list(number)
userGuess = ''
print("""
+1 ------> You guessed a digit in the right place value
-1 ------> You guessed a digit but not in the right place value
""")

while userGuess != number:
    try:
        isInPlace = 0
        isNotInPlace = 0
        userGuess = input('\nEnter a 4-digit number to guess that does not contain 0: ')
        if userGuess.isdigit() == True:
            for i in range(len(answer)):
                if userGuess[i] == answer[i]:
                    isInPlace += 1
                elif userGuess[i] in answer:
                    isNotInPlace -= 1
                else:
                    continue
            if isNotInPlace != 0 and isInPlace != 0:
                print('+', isInPlace, ' ', isNotInPlace, sep='')
            elif isNotInPlace != 0:
                print(isNotInPlace)
            elif isInPlace != 0:
                print('+', isInPlace, sep='')
            if isInPlace == 4:
                print('Congratulations! You guessed the number {}'.format(number))
        else:
            raise ValueError
    except ValueError:
        print('You must enter only numbers!')