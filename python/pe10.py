from math import sqrt,ceil

def isprime(n): #returns 1 if n is prime, 0 if n is composite
    if n<2:
        return 0
    if n<4:
        return 1
    s=ceil(sqrt(n))
    t=int(s)
    for i in range(2,t+1):
        if n % i == 0: return 0
    return 1

def nextprime(n): #returns smallest prime strictly greater than n
    p=n+1
    if p % 2 == 0: p=p+1
    while isprime(p)==0:
        p=p+2
    return p

def prime(n): #returns nth prime
    if n==1: return 2
    return nextprime(prime(n-1))

j=0
for i in range(1,2000000):
    j=j+i*isprime(i)
print j
