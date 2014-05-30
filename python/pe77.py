# What is the least number which can be written as a sum of primes in more than 5000 different ways? (order doesn't matter)

import itertools
from math import sqrt

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

sum_ways={}
primes = set(sieve(1000000))
for n in itertools.count(0):
    for k in xrange(n+1):
        if n==0: sum_ways[(n,k)]=1
        elif k==2 and n%2==0: sum_ways[(n,k)]=1
        elif k==2: sum_ways[(n,k)]=0
        else: sum_ways[(n,k)]=sum(sum_ways[(n-i,min(i,n-i))] for i in xrange(1,k+1) if i in primes)
    if sum_ways[(n,n)]>5000:
        print n,sum_ways[(n,n)]
        break


print sum_ways[10,10]
