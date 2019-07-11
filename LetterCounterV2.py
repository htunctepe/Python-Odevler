# ---------------------------------4. HAFTA, 2. ODEV 2. Versiyon---------------------------------
userInput = input("\nPlease enter a string to be processed: ")
upper = 0
lower = 0
number = 0
specialChar = 0

for letter in userInput:
    if letter.isalpha():
        if letter.isupper() == True:
            upper += 1
        elif letter.islower() == True:
            lower += 1
    elif letter.isalnum() == True:
        if letter.isdigit():
            number += 1
    specialChar = len(userInput) - (upper + lower + number)

print("""\nIn the string you entered
{} letter(s) are upper case,
{} letter(s) are lower case,
{} letter(s) are digits,
{} letter(s) are special characters.""".format(upper,lower,number,specialChar))