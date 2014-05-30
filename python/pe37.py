from math import sqrt

def isprime(n): #returns 1 if n is prime, 0 if n is composite
    if n<2:
        return 0
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

def ltrunc(n): #returns 1 if the prime number is truncatable from the left, otherwise 0
    n=str(n)
    n=n[1:]
    while n!='':
        if isprime(int(n))==0: return 0
        n=n[1:]
    return 1

def rtrunc(n): #returns 1 if the prime number is truncatable from the right, otherwise 0
    n=str(n)
    n=n[:-1]
    while n!='':
        if isprime(int(n))==0: return 0
        n=n[:-1]
    return 1

p=11
n=0
total=0
while n<11:
    if ltrunc(p):
        if rtrunc(p):
            print p
            n+=1
            total+=p
    p=nextprime(p)
print 'total=',total
