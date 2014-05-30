import itertools
from math import sqrt

def nd(L): #given L:exponents in factorization of n, returns number of integers in [1,n] which divide n^2
    "assumes L is a list giving multiplicities of prime factors of a number n; returns half the number of divisors of n*n" 
    return product([2*i+1 for i in L])/2+1

def sieve(n): #returns a list of all primes below n
    sievedata=[0]*2+[1]*(n-2)
    for i in xrange(1+int(sqrt(n))):
        if sievedata[i]==1:
            for j in xrange(2*i,n,i):
                sievedata[j]=0
    primes=[]
    for i in xrange(n):
        if sievedata[i]==1: primes.append(i)
    return primes

def fton(L): #given L:exponents in factorization of n, returns n
    primes=sieve(2**len(L)+1)
    total=1
    for i in xrange(len(L)):
        total*=primes[i]**L[i]
    return total

def dr(n,flag=0): #number of integers in [1,n] which divide n^2
    count=0
    for i in xrange(1,n+1):
        if n*n%i==0:
            if flag: print "1/{0}+1/{1}=1/{2}".format(n+i,n+n*n/i,n)
            count+=1
    return count
        
def product(stuff): #returns the product of iterable
    p = 1
    for i in stuff:
        p *= i
    return p

## We want to find min(fton(L)) where nd(L)>4000000

def main():
    best=fton([10,7,5,4,3,3,2,2,2,2,2,2])
    bestL=[10,7,5,4,3,3,2,2,2,2,2,2]
    for i in xrange(1,5):
      for j in xrange(1,5):
        for k in xrange(1,4):
          for l in xrange(1,4):
            for m in xrange(1,3):
              for n in xrange(1,3):
                for o in xrange(1,2):
                  for p in xrange(1,2):
                    for q in xrange(1,2):
                      for r in xrange(2):
                        for s in xrange(2):
                          for t in xrange(2):
                            for u in xrange(2):
                              L=[i,j,k,l,m,n,o,p,q,r,s,t,u]
                              if nd(L)>4000000:
                                if fton(L)<best:
                                  best=fton(L)
                                  bestL=L
    print best
    print bestL
    print nd(bestL)

def test():
    for i in xrange(5):
        for j in xrange(5):
            for k in xrange(5):
                for l in xrange(5):
                    for m in xrange(5):
                        L=[i,j,k,l,m]
                        diff=nd(L)-dr(fton(L))
                        if diff: print L,diff
    
main()
