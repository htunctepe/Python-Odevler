# _______________________________5.Hafta, 1.Odev_______________________________
import random
noOfTrials = 0
pics = ["""
       +---+    You have {} more trials left!
       |   |
       |   O 
       |
       |
       |
=========""", """
       +---+    You have {} more trials left!
       |   |
       |   O
       |   |
       |
       |
=========""", """
       +---+    You have {} more trials left!
       |   |
       |   O
       |  /|
       |
       |
=========""", """
       +---+    You have {} more trials left!
       |   |
       |   O
       |  /|\\
       |
       |
=========""", """
       +---+    You have {} more trials left!
       |   |
       |   O
       |  /|\\
       |  /
       |
=========""", """
       +---+    You have {} more trials left!
       |   |
       |   O
       |  /|\\ 
       |  / \\
       |
=========
Oops! You killed the man!"""]
# One of the following words in the list will be selected randomly for the user to guess
secretWords = ['KAPALILIK', 'PYTHON', 'INTERNET']
# Generating a number to be used to select the word from the secretWords list.
# We could just use random.choice(secretWords) for the code between lines 52-54.
selectedWord = random.randint(0, 2)
# Storing the selected item from the secretWords list into a list of letters
answer = list(secretWords[selectedWord])
# Defining a variable to keep the number of underscores '_' to be written for unguessed letters
unguessed = ['_'] * len(answer)
# The following commented code also does the same thing as line 57
"""
for i in range(len(answer)):
    unguessed.append('_')
"""
print('<----------------Hangman Game---------------->')
if selectedWord == 0:
    print('\nHint: Noun form of closed in Turkish language.')
elif selectedWord == 1:
    print('\nHint: A programming language ;).')
else:
    print('\nHint: The digital medium with connected computers you use everyday to search information or just to surf.')

while noOfTrials < 6:
    try:
        print('\n', ' '.join(unguessed), sep='')
        userGuess = input('\nGuess a letter: ')
        if userGuess.isalpha() == True:
            for i in range(len(answer)):
                if userGuess.upper() == answer[i]:
                    unguessed[i] = userGuess.upper()
            if unguessed == answer:
                print('Congratulations! You guessed the word "{}".'.format(''.join(answer)))
                break
            else:
                noOfTrials += 1
                print(pics[noOfTrials-1].format(6 - noOfTrials))
                if noOfTrials == 6:
                    print('The word was "{}".'.format(''.join(answer)))
        else:
            raise ValueError
    except ValueError:
        print('You made an invalid entry! You should enter a letter!')
