from math import sqrt
import itertools

def product(stuff): #returns the product of a set, list, or tuple
    p = 1
    for i in stuff:
        p *= i
    return p

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

def factorize(n): #returns a set of the prime factors.
    factors=[]
    p=2
    while n>1:
        if p>sqrt(n):
            factors.append(n)
            n=1
        elif n % p == 0:
            n=n/p
            factors.append(p)
        else:
            p=nextprime(p)
    return set(factors)

def eulerphi(n): # computes Euler's totient function through a prime factorization and inclusion/exclusion. Runs in roughly O(sqrt(n)) time, as opposed to the O(n) naive algorithm. Gives the wrong answer on 0 and 1 for the sake of speedup.
    factors=factorize(n)
    phi=n-1
    for i in range(1,len(factors)+1): #we iterate over products p of subsets of prime factors
        for j in itertools.combinations(factors,i):
            p=product(j)
            if i%2: phi-=(n-1)/p
            else: phi+=(n-1)/p
    return phi

def gcd(n,m):
    if n*m==0: return n+m
    while n>0:
        p=m
        m=n
        n=p%m
    return m

def slow_eulerphi(n):
    phi=0
    for i in xrange(1,n+1):
        if gcd(i,n)==1: phi+=1
    return phi

candidates=[]
for n in xrange(1,10**7+1):
    p=eulerphi(n)
    a=list(str(p))
    b=list(str(n))
    a.sort()
    b.sort()
    if a==b: candidates.append(n)
minp=21.0/12
bestn=21
for n in candidates:
    p=1.0*n/eulerphi(n)
    if p<minp:
        minp=p
        bestn=n
print bestn
