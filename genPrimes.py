def genPrimes():
    primeList = [2]
    x = 3
    while True:
        prime = True
        for p in primeList:
            if (x % p) == 0:
                prime = False
                break
        if prime == True:
            primeList = primeList + [x]
            yield p
        x += 1

def genPrimesAlt():
    primes = []   # primes generated so far
    last = 1      # last number tried
    while True:
        last += 1
        for p in primes:
            if last % p == 0:
                break
        else:
            primes.append(last)
            yield last


prime = genPrimes()
for x in range(20):
     print prime.next()   

        