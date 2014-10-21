curString = s[0]
longest = s[0]
for i in range(1, len(s)):                  # start on the second index value of s
    if s[i] >= curString[-1]:               # compare the next index value with the last value
        curString += s[i]                   # if the next is > the last, append value
        if len(curString) > len(longest):   # if the current string is longer than the last...
            longest = curString             # name the current the string the longest
    else:
        curString = s[i]
print 'Longest substring in alphabetical order is:', longest