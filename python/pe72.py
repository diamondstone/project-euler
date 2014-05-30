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

sum=0
for n in xrange(2,10**6+1):
    sum+=eulerphi(n)
print sum
