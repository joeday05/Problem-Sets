# 6.00x Problem Set 6
#
# Part 2 - RECURSION

#
# Problem 3: Recursive String Reversal
#
def reverseString(aStr):
    """
    Given a string, recursively returns a reversed copy of the string.
    For example, if the string is 'abc', the function returns 'cba'.
    The only string operations you are allowed to use are indexing,
    slicing, and concatenation.
    
    aStr: a string
    returns: a reversed string
    """
    bStr = ""
    if aStr == "":
        return bStr
    else: 
        bStr = aStr[-1]
        return bStr + str(reverseString(aStr[:-1]))

    
#aStr = 'abc'
#print reverseString(aStr)


#
# Problem 4: X-ian
#
def x_ian(x, word):
    """
    Given a string x, returns True if all the letters in x are
    contained in word in the same order as they appear in x.

    >>> x_ian('eric', 'meritocracy')
    True
    >>> x_ian('eric', 'cerium')
    False
    >>> x_ian('john', 'mahjong')
    False
    
    x: a string
    word: a string
    returns: True if word is x_ian, False otherwise
    """
    if x == "":
        return True
    elif word == "":
        return False
    else:
        if x[0] == word[0]:
            print x, word
            return x_ian(x[1:], word[1:])
        else:
            print x, word
            return x_ian(x[0:], word[1:])


#x = 'john'
#word = 'mahjong'
#print x_ian(x, word)


#
# Problem 5: Typewriter
#
def insertNewlines(text, lineLength, letterCnt = 0):
    """
    Given text and a desired line length, wrap the text as a typewriter would.
    Insert a newline character ("\n") after each word that reaches or exceeds
    the desired line length.

    text: a string containing the text to wrap.
    line_length: the number of characters to include on a line before wrapping
        the next word.
    returns: a string, with newline characters inserted appropriately. 
    """
    newText = ''
    if text == '':
        return newText
    else:
        if letterCnt == lineLength:
            if text[0] == " ":
                newText = "\n"
                letterCnt = 0
            else:
                newText = text[0]
        else:
            newText = text[0]
            letterCnt += 1
        return newText + str(insertNewlines(text[1:], lineLength, letterCnt))



text = 'Given text and a desired line length, wrap the text as a typewriter would. Insert a newline character after each word that reaches or exceeds he desired line length.'
lineLength = 40

print insertNewlines(text, lineLength)