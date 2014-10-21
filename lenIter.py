def lenIter(aStr):
    assert type(aStr) == str
    cnt = 0
    for letter in aStr:
        cnt += 1
    return cnt
    
#print lenIter("abcdef")

    
        
def lenRecur(aStr):    
    if aStr == "": 
        return 0
    else: 
        return 1 + lenRecur(aStr[0:-1])
            

print lenRecur('abcd')

