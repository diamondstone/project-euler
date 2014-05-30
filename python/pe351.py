## Python script for Project Euler problem 354

## Problem description:
## A hexagonal orchard of order n is a triangular lattice made up of points within a regular hexagon with side n. (So there are n+1 lattice points on each side.)

## Some points  are hidden from the center by a point closer to it. It can be seen that for a hexagonal orchard of order 5, 30 points are hidden from the center.

## Let H(n) be the number of points hidden from the center in a hexagonal orchard of order n.

## H(5) = 30. H(10) = 138. H(1 000) = 1177848.

## Find H(100 000 000).

## Notes: A point is a lattice point iff it is of the form <x,y>=(x/2,sqrt(3)y/2) for integers x and y with the same parity. This point is inside the hexagonal lattice of order n if |x|+|y| <= 2n, and |y| <= n. Each point with x=0, y=0, |x|=|y|, or |x|=3|y| has 6 symmetric copies, every other point has 12. Every point has a symmetric copy where 0 <= x <= y.

## A point <x,y> is hidden if <x,y>=k<x',y'> for some pair (x',y') in the lattice, where k>1. By usual lattice properties, it's easy to see that k can be chosen to be an integer, and hence k divides gcd(x,y). If gcd(x,y)>2, then either x,y have a shared prime factor p>2, in which case <x,y> is hidden by <x,y>/p, or else x,y have a shared factor of 4, in which case <x,y> is hidden by <x,y>/2. If gcd(x,y)=1, then <x,y> is clearly not hidden. If gcd(x,y)=2, then <x,y> is hidden iff <x/2,y/2> is a lattice point iff (x+y)/2 is even.

## Therefore, we want to compute the number of same-parity pairs (x,y) with 0<x<y<=n such that gcd(x,y)>2 or gcd(x,y)=2 and (x+y)/2 is even, then multiply by 12, then add (n+floor(n/2)-2)*6 (for the points along lines of symmetry). #Note: this will undercount the points by 6 when n=1 and 12 when n=0, but we don't care.

## This is too slow to do by brute force, however, so we instead want to use a faster version of Euler's phi function to quickly compute the number of x<y with gcd(x,y)=1. Next, we can compute the number of x<y with gcd(x,y)=2 by 

import itertools

def gcd(n,m): #returns the greatest common denominator of n and m, using Euclidean algorithm. Algorithm runs for one cycle less if n<m.
    if n*m==0: return n+m
    while n>0:
        p=m
        m=n
        n=p%m
    return m

def factorize(n): #returns a set of the prime factors.
    factors=[]
    p=2
    while n>1:
        if p>int(n**0.5):
            factors.append(n)
            n=1
        elif n % p == 0:
            n=n/p
            factors.append(p)
        else:
            p+=1
    return set(factors)

def product(stuff): #returns the product of a set, list, or tuple
    p = 1
    for i in stuff:
        p *= i
    return p

def eulerphi(n): # computes Euler's totient function through a prime factorization and inclusion/exclusion. Runs in roughly O(sqrt(n)) time, as opposed to the O(n) naive algorithm. Gives the wrong answer on 0 and 1 for the sake of speedup.
    factors=factorize(n)
    phi=n-1
    for i in range(1,len(factors)+1): #we iterate over products p of subsets of prime factors
        for j in itertools.combinations(factors,i):
            p=product(j)
            if i%2: phi-=(n-1)/p
            else: phi+=(n-1)/p
    return phi

def mod_eulerphi(n): # for *odd* n, computes the number of *odd* m<n which are relatively prime to n.
    factors=factorize(n)
    phi=(n-1)/2 #number of odd numbers less than n.
    for i in range(1,len(factors)+1): #we iterate over products p of subsets of prime factors
        for j in itertools.combinations(factors,i):
            p=product(j)
            if i%2: phi-=((n-1)/p+1)/2 # how many odd numbers less than n are divisible
            else: phi+=((n-1)/p+1)/2 # by p. The +1 is because we round up.
    return phi

def pair_eulerphi(n): # returns (eulerphi(n),mod_eulerphi(n)); eliminates wasted computations. 
    factors=factorize(n)
    a=n-1
    b=(n-1)/2 #number of odd numbers less than n.
    for i in range(1,len(factors)+1): #we iterate over products p of subsets of prime factors
        for j in itertools.combinations(factors,i):
            p=product(j)
            if i%2:
                a-=(n-1)/p
                b-=((n-1)/p+1)/2
            else:
                a+=(n-1)/p
                b+=((n-1)/p+1)/2
    return (a,b)

def hiddenpoints(n):
    hidden=0
    for y in range(2,n+1):
        z=y%2
        for x in range(2-z,y,2):
            d=gcd(x,y)
            if d>2: hidden+=2
            if d==2:
                if (x+y)%4==0: hidden+=2
    hidden+=n+n/2-2
    hidden*=6
    return hidden

def varhiddenpoints(n):
    hidden=0
    for y in range(2,n+1):
        if y%2: hidden+=2*((y-1)/2-mod_eulerphi(y))
        else:
            a,b=pair_eulerphi(y/2)
            hidden+=2*((y-2)/2-a) #counts (x,y) with gcd(x,y)>2, doubled
            if y%4: hidden+=2*b #counts (x,y) with gcd(x,y)=2 and (x+y)/2 even.
    hidden+=n+n/2-2
    hidden*=6
    return hidden

print varhiddenpoints(100000000)




## This is an O(n^2) time algorithm, and takes ~1 second to compute hiddenpoints(1000). Hence it will take ~300 years to compute hiddenpoints(100,000,000).

## Would a sieve work better? Seems like it might take ~O(n log n) time, rather than O(n^2) time, which would be a big improvement.
