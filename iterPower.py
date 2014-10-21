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

print iterPower(10 , 2)

def recurMul(a, b):
    if b == 1:
        return a
    else:
        return a + recurMul(a, b-1)

