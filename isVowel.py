def isVowel3(char):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for i in vowels:
        if char == i:
            return True
        else:
            return False


def isVowel2(char):
    return char in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']


print isVowel2('a')
print isVowel2('B')
print isVowel2('E')
print isVowel2('z')
