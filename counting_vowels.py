# Counting Vowels

"""
Write a program that counts up the number of vowels contained 
in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.  
"""

s = 'azcbobobegghakl'
vowel_cnt = 0
for char in s:
    if char == 'a':
        vowel_cnt += 1
    elif char == 'e':
        vowel_cnt += 1
    elif char == 'i':
        vowel_cnt += 1
    elif char == 'o':
        vowel_cnt += 1
    elif char == 'u':
        vowel_cnt += 1
    else:
        vowel_cnt += 0

print "Number of vowels: " + str(vowel_cnt)
           