# Counting Bobs

"""
Write a program that prints the number of times the string 'bob' occurs 
in s. For example, if s = 'azcbobobegghakl', then your program should print
Number of times bob occurs is: 2
"""

s = 'azcbobobegghakl'
bob_cnt = 0
for index in range(len(s)-2):
    if s[index:index+3] == "bob":
          bob_cnt += 1

print "Number of times bob occurs is: " + str(bob_cnt)
