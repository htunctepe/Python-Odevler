# ---------------------------------4. HAFTA, 4. ODEV---------------------------------

vowel = ['a','ı','o','u','e','i','ö','ü'] # Putting all Turkish vowels in a list
inputFile = open("futbolcular.txt", "r", encoding='cp1254') # iso8859_9 maybe used for encoding Turkish characters as well
fileContent = inputFile.read().split('\n')

# Splitting the file content whenever there is a newline character
# and storing them as elements of a list called 'fileContent'

# opening the file with a+, to bypass the error when the file does not exist.
# Otherwise, it could be opened with 'w'
with open("SesliHarfleBaslayanIsimler.txt", 'a+', encoding='cp1254') as fnew:
    print('\nFollowing names are written to the file "SesliHarfleBaslayanIsimler.txt":\n')
    for name in fileContent:
        if name[0].lower() in vowel:
            # Just checking the first character if it is one of the
            print(name)
            fnew.write(name.split(",")[0] + "\n")
        elif name[0] == 'İ':
            print(name)
            fnew.write(name.split(",")[0] + "\n")
            # Writing the names that starts with vowels defined in 'vowels' list

