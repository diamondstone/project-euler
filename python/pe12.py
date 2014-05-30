from math import sqrt,ceil

def product(a,b): return a*b

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
    
def numdivisors(n):
    factors=factorize(n)
    multiplicities=[2] #this is a lie, because we actually store 1 plus the multplicity
    for i in range(1,len(factors)):
        if factors[i] != factors[i-1]: multiplicities.append(2)
        else: multiplicities[len(multiplicities)-1]=multiplicities[len(multiplicities)-1]+1
    return reduce(product,multiplicities)

n=2000
k=0
while k<500:
    n=n+1
    k=numdivisors((n*(n+1))/2)
print n,(n*(n+1))/2,k
