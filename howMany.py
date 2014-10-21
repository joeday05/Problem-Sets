def howMany(aDict):
    count = 0
    for i in aDict:
        for j in aDict[i]:
            count += 1
    return count
    
def biggest(aDict):
    largest = 0
    aKey = ""
    if len(aDict) == 0: return None
    for i in aDict:
        count = 0
        for j in aDict[i]:
            count += 1
        if count >= largest:
            largest = count
            aKey = i
    return aKey
            
                
                        
#animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
#animals['d'] = ['donkey']
#animals['d'].append('dog')
#animals['d'].append('dingo')
#animals = {}
animals = {'V':[]}
print howMany(animals)
print biggest(animals)
