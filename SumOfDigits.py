# ---------------------------------4. HAFTA, 3. ODEV---------------------------------
# Kullanıcıdan bir input alınız. Girmiş olduğu inputtaki rakamların toplamını veren bir program yazınız.
# (Kullanıcı rakam girmek zorunda değil.
# farklı karakter girişi de yapabilir.)
# Örnek input = "art12kl4*"



userInput = input("\nPlease enter a string to be processed: ")
sumOfDigits = 0
listOfDigits = []
index = 0

for letter in userInput:
    #if letter.isalnum():
    if letter.isdigit():
        listOfDigits.insert(index, letter)
        sumOfDigits += int(letter)
        index += 1

print("""\nIn the string you entered
The digits are: {}
And the sum of digits: {}""".format(listOfDigits,sumOfDigits))