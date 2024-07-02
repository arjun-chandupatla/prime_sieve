from math import sqrt

def sieve(num):
    primes = []
    numArray = range(2, num + 1)
    for i in numArray:
        try:
            isPrime = True
            n = 0
            for p in primes:
                if i < p^2:
                    break
                if i % p == 0:
                    isPrime = False
            if isPrime:
                primes.append(i)
        except IndexError:
            pass
    return primes
