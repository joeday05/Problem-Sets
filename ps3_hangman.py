# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letter in secretWord:
        if letter not in lettersGuessed: return False
    return True
     

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    result = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            result += letter
        else:
            result += '_ '
    return result


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    result = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for letter in alphabet:
        if letter not in lettersGuessed:
            result += letter
    return result

    
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    numberOfGuesses = 8
    lettersGuessed = []
    mistakesMade = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ""
    
    for letter in secretWord:
        if letter in alphabet:
            result += letter

    secretWord = result
    under = " _"
    guessStr = under * len(secretWord)
    
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.'
       
    while mistakesMade < numberOfGuesses:
        print '-------------'        
        print 'You have ' + str(numberOfGuesses - mistakesMade) + ' guesses left.'

        availableLetters = getAvailableLetters(lettersGuessed)
        print 'Available letters: ' + str(availableLetters)
        letter = raw_input('Please guess a letter: ')
        letter = letter.lower()
        if letter not in availableLetters:
            print "Oops! You've already guessed that letter: " + guessStr
        else:   
            lettersGuessed.append(letter.lower())
        
            spacesBefore = guessStr.count(under.strip())
            guessStr = getGuessedWord(secretWord, lettersGuessed)
            spacesAfter = guessStr.count(under.strip())
            if spacesBefore == spacesAfter:
                mistakesMade += 1
                print "Oops! That letter is not in my word: " + guessStr
            else:
                print "Good guess: " + guessStr
                if isWordGuessed(secretWord, lettersGuessed) == True: break
                spacesBefore = guessStr.count(under)                        
        
    if mistakesMade < numberOfGuesses:
        print '-------------'
        print 'Congratulations, you won!'
    else:
        print '-------------'
        print 'Sorry, you ran out of guesses. The word was ' + str(secretWord) + '.'


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = 'guanabana'
#secretWord = chooseWord(wordlist).lower()
hangman(secretWord)