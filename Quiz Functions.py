#Quiz Functions

def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    logVal = x // 2
    while b ** logVal > x:
       logVal -= 1
    return logVal
            
#print myLog(15, 3)
#
#for x in range(1,30):
#        print myLog(x, 2)
        
        
def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """

    lace = str("")
    if s1 == "":
        lace += s2
    elif s2 == "":
        lace += s1
    elif len(s1) <= len(s2):
        for i in range(len(s1)):
            lace += s1[i]
            lace += s2[i]
        lace += s2[i+1:]
    else: 
        for j in range(len(s2)):
            lace += s1[j]
            lace += s2[j]
        lace += s1[j+1:]

    return lace


#print laceStrings('jn', 'mdjarqpfislywc')       


def laceStringsRecur(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    def helpLaceStrings(s1, s2, out):    #not sure what 'out' is used for
        if s1 == '':
            return s2
        if s2 == '':
            return s1
        else:
            print s1, s2
            return s1[0] + s2[0] + helpLaceStrings(s1[1:len(s1)], s2[1:len(s2)], out)  #base case is when at least one string gets to ''
    return helpLaceStrings(s1, s2, '')    

#print laceStringsRecur('jn', 'mdjarqpfislywc')       
#print laceStringsRecur('', 'mdjarqpfislywc')       
#print laceStringsRecur('jn', '')
#print laceStringsRecur('jna', 'md')
#print laceStringsRecur('mdjarqpfislywc', 'jn')



def McNuggets(n):

    a = 0
    b = 0
    c = 0
    for c in range(0, n):
        for b in range(0, n):
            for a in range(0, n):
                if 6*a + 9*b +20*c == n: 
                    print "a: " + str(a),
                    print "b: " + str(b),
                    print "c: " + str(c), 
                    print 6*a + 9*b + 20*c
                    return True
    return False



print McNuggets(15)


#fix the next three functions by changing only one line of code
def fixedPoint(f, epsilon):                                #guesser function
    """
    f: a function of one argument that returns a float
    epsilon: a small float
  
    returns the best guess when that guess is less than epsilon 
    away from f(guess) or after 100 trials, whichever comes first.
    """
    guess = 1.0
    for i in range(100):
        if abs(f(guess) - guess) < epsilon:   #added abs()
            
            return guess
        else:
            guess = f(guess)
            print f(guess), guess, epsilon

    return guess
    


#epsilon = .0001
#print fixedPoint(f, epsilon)



def sqrt(a):                               #this is the sqrt function
    def tryit(x):
        return 0.5 * (a/x + x)             #this is the function f
    return fixedPoint(tryit, 0.0001)       # changed tryit(a) to tryit


#print sqrt(4)



def babylon(a):
    def test(x):
        return 0.5 * ((a / x) + x)
    return test

def sqrt2(a):
    return fixedPoint(babylon(a), 0.0001)  # Changed babylon to babylon(a)


#print sqrt2(4)
