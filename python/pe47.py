from math import sqrt

def isprime(n): #returns 1 if n is prime, 0 if n is composite
    if n<2:
        return None
    if n<4:
        return 1
    t=int(sqrt(n))
    for i in range(2,t+1):
        if n % i == 0: return 0
    return 1

def nextprime(n): #returns smallest prime strictly greater than n
    p=n+1
    if p % 2 == 0: p=p+1
    while isprime(p)==0:
        p=p+2
    return p

def factorize(n): #returns a list of the prime factors, with repetition, in increasing order.
    factors=[]
    p=2
    while n>1:
        if n % p == 0:
            n=n/p
            factors.append(p)
        else:
            p=nextprime(p)
    return factors

consecutive=0
for i in range(99996,1000000):
    if len(set(factorize(i)))==4:
        consecutive+=1
    else:
        consecutive=0
    if consecutive==4:
        break
print i-3
