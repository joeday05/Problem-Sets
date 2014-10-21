# 6.00x Problem Set 6
#
# Part 1 - HAIL CAESAR!

import string
import random

WORDLIST_FILENAME = "words.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print "  ", len(wordList), "words loaded."
    return wordList

def isWord(wordList, word):
    """
    Determines if word is a valid word.

    wordList: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.

    Example:
    >>> isWord(wordList, 'bat') returns
    True
    >>> isWord(wordList, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList

def randomWord(wordList):
    """
    Returns a random word.

    wordList: list of words  
    returns: a word from wordList at random
    """
    return random.choice(wordList)

def randomString(wordList, n):
    """
    Returns a string containing n random words from wordList

    wordList: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([randomWord(wordList) for _ in range(n)])

def randomScrambled(wordList, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordList: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words

    NOTE:
    This function will ONLY work once you have completed your
    implementation of applyShifts!
    """
    s = randomString(wordList, n) + " "
    shifts = [(i, random.randint(0, 25)) for i in range(len(s)) if s[i-1] == ' ']
    return applyShifts(s, shifts)[:-1]

def getStoryString():
    """
    Returns a story in encrypted text.
    """
    return open("story.txt", "r").read()


# (end of helper code)
# -----------------------------------


#
# Problem 1: Encryption
#
def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    assert type(shift) == int
    coder = {}
    
    alphabet = string.ascii_uppercase
    for i in range(2):
        for letter in range(len(alphabet)):
            letterShift = (letter - shift) % 26
            coder[alphabet[letterShift]] = alphabet[letter]
        alphabet = string.ascii_lowercase
    
    return coder

def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    outText = ""
    for letter in text:
        if letter not in string.ascii_uppercase and letter not in string.ascii_lowercase:
            outText += str(letter)
        else:
            outText += str(coder.get(letter))

    return outText

def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    
    wrapper function
    """
    coder = buildCoder(shift)
    return applyCoder(text, coder)
    
#
# Problem 2: Decryption
#
def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    #split text into a list of words
    wordSplit = text.split(" ")
    #print wordSplit

    #function to test letter for upper or lower case
    def capsTest(letter):
        if letter in string.ascii_uppercase: alphabet = string.ascii_uppercase
        elif letter in string.ascii_lowercase: alphabet = string.ascii_lowercase
        else: alphabet = ""
        return alphabet

    '''
    take the smallest word and shift each letter through all 26 letters in the alphabet, 
    saving the shifts that make valid words
    '''
    def checkShift(word, wordList):
        newWord = ""
        saveShiftKeys = []
        for shift in range(26):
            for letter in word:
                alphabet = capsTest(letter)
                if alphabet != "":
                    letterIndex = alphabet.index(letter)
                    letterShift = (shift + letterIndex) % 26
                    newWord += str(alphabet[letterShift])

            if isWord(wordList, newWord):
                #print newWord,
                #print shift
                saveShiftKeys.append(shift)

            newWord = ""
        return saveShiftKeys

    '''
    check all the words through the saved shift keys and save the shift with 
    the best success rate
    '''
    def checkAllShift(testList, saveShiftKeys, wordList):
        bestFit = 0
        newWord = ""
        #totalSuccess = []
        maxSuccess = 0
        #print 'possible shift key values: ', saveShiftKeys
        
        for shift in saveShiftKeys:
            success = 0
            for word in testList:
                for letter in word:
                    alphabet = capsTest(letter)
                    if alphabet != "":
                        letterIndex = alphabet.index(letter)
                        letterShift = (letterIndex + shift) % 26
                        newWord += str(alphabet[letterShift])

                if isWord(wordList, newWord):
                    #print 'successful word: ',newWord
                    success += 1

                newWord = ""
            if success > maxSuccess:
                maxSuccess = success
                #print 'shift: ', shift
                bestFit = shift
            #totalSuccess.append([shift, success])
            #print 'success list: ',totalSuccess

        return bestFit
     
    '''
    take encrypted words that have been split into a list (wordSplit). starting with the shortest word,
    take each letter through 26 shifts and save the shifts that form correct words.  If none, go to next biggest word.
    run the remaining words through the successful ShiftKeys.  keep the ShiftKey that has the best
    success rate on all the words. 
    '''
    saveShiftKeys = []
    bestFit = 0
    wordSplitSort = wordSplit[:]
    wordSplitSort.sort(key = len)
    for word in wordSplitSort:
        saveShiftKeys = checkShift(word, wordList)
        if len(saveShiftKeys) > 0:
            break
    bestFit = checkAllShift(wordSplit, saveShiftKeys, wordList)
    return bestFit

def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Use the functions getStoryString and loadWords to get the
    raw data you need.

    returns: string - story in plain text
    """
    wordList = loadWords()
    encryptedStory = getStoryString()
    #print encryptedStory
    #print
    bestFit = findBestShift(wordList, encryptedStory)
    decryptedStory = applyShift(encryptedStory, bestFit)
    return decryptedStory

#
# Build data structures used for entire session and run encryption
#

if __name__ == '__main__':
    # To test findBestShift:
    wordList = loadWords()
    s = applyShift('Hello, world!', 8)
    bestShift = findBestShift(wordList, s)
    assert applyShift(s, bestShift) == 'Hello, world!'
    # To test decryptStory, comment the above four lines and uncomment this line:
    #    decryptStory()
