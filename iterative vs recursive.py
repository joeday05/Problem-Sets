def iterMul(a, b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result

def iterPower(base, exp):
    result = 1
    while exp > 0:
        result *= base
        exp -= 1
    return result

#print iterPower(10 , 2)

def recurMul(a, b):
    if b == 1:
        return a
    else:
        return a + recurMul(a, b-1)

#print recurMul(5, 3)


def factI(n):
    """assumes that n is an int > 0
       returns n!"""
    res = 1
    while n > 1:
        res = res * n
        n -= 1
    return res

def factR(n):
    """assumes that n is an int > 0
       returns n!"""
    if n == 1:
        return n
    return n*factR(n-1)
    
#print factR(5)

def recurPower(base, exp):
    if exp == 0:
        return 1
    return base * recurPower(base, exp-1)
    
#print recurPower(4, 2)


def recurPowerNew(base, exp):
    if exp == 0:
        return 1
    if exp % 2 == 1:
        return base * recurPowerNew(base, exp-1)
    else:
        return base * base * recurPowerNew(base, exp-2)
    
#print recurPowerNew(4, 6)


def gcd(a, b):
    c = a
    while c > 0:
        if b % c == 0 and a % c == 0: 
            return c
        c -= 1
    
#print gcd(2, 12)
    
    
#Euclidean algorithm to calculate greatest common denomenator
def gcdRecur(a, b):
    if b == 0: 
        return a
    else:
        return gcdRecur(b, a % b)
        
                
print gcdRecur(4, 3)



