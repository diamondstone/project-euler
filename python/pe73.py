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

def totient_range(n,a,b): # computes the number of integers in [a,b] which are relatively prime to n. As in the algorithm for Euler's totient function, uses a prime factorization and inclusion/exclusion.
    if b<a: return 0
    factors=factorize(n)
    phi=b-a+1
    for i in xrange(1,len(factors)+1): #we iterate over products p of subsets of prime factors
        for j in itertools.combinations(factors,i):
            p=product(j)
            if i%2: phi-=b/p-(a-1)/p
            else: phi+=b/p-(a-1)/p
    return phi

def slow_totient_range(n,a,b): # computes the number of integers in [a,b] which are relatively prime to n. Is in the algorithm for Euler's totient function, uses a prime factorization and inclusion/exclusion.
    phi=0
    for i in xrange(a,b+1):
        if gcd(i,n)==1: phi+=1
    return phi

def gcd(n,m): #returns the greatest common denominator of n and m, using Euclidean algorithm. Algorithm runs for one cycle less if n<m.
    if n*m==0: return n+m
    while n>0:
        p=m
        m=n
        n=p%m
    return m

sum=0
for d in xrange(2,1000000+1):
    a=d/3+1 #we want fractions strictly larger than 1/3
    b=(d-1)/2 #we want fractions strictly less than 1/2
    sum+=totient_range(d,a,b)
print sum
