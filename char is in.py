def isIn(char, aStr):
    if len(aStr) == 0: return False
    elif len(aStr) == 1 and char == aStr: return True
    elif len(aStr) == 1 and char != aStr: return False
    elif char == aStr[len(aStr)/2]: return True
    
    if char < aStr[len(aStr)/2]:
        aStr = aStr[: len(aStr)/2]
        return isIn(char, aStr)
    else:
        aStr = aStr[len(aStr)/2:]
        return isIn(char, aStr)

        

print isIn("z", "abcdefghijklmnopqrstu")
