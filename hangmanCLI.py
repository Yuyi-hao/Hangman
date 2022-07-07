import random
import string
from wordList import words

def isValidWord(words):
    word = random.choice(words)
    while '-' in word or ' 'in word:
        word = random.choice(words)
    return word

def hangman():
    word = isValidWord(words).upper()
    wordLetters = set(word)
    alphabet = set(string.ascii_uppercase)
    usedLetter = set()
    lives = 6

    while len(wordLetters)>0 and lives:
        currentWord = [letter if letter in usedLetter else '-' for letter in word]
        userLetter = input(f"you have {lives} lives Current word is {' '.join(currentWord)} : ").upper()
        if userLetter in alphabet - usedLetter:
            usedLetter.add(userLetter)
            if userLetter in wordLetters:
                wordLetters.remove(userLetter)
            else:
                print(f'{userLetter} is not in word')
                lives -=1
        elif usedLetter in usedLetter:
            print('You have already used this letter. Try another letter!')
        else:
            print('Invalid character')
    
    if lives:
        print(f"you guessed word it was {word.upper()}")
    else:
        print(f"You died the word was {word.upper()}")

hangman()


