import pickle
from math import sqrt

def isprime(n): #returns 1 if n is prime, 0 if n is composite
    if n<5000000:
        return n in primes
    t=int(sqrt(n))
    while t*t<n:
        t+=1
    for i in range(2,t):
        if n % i == 0: return 0
    return 1

def sieve(n): #returns a list of all primes below n
    sievedata=[0]*2+[1]*(n-2)
    for i in range(1+int(sqrt(n))):
        if sievedata[i]==1:
            for j in range(2*i,n,i):
                sievedata[j]=0
    primes=[]
    for i in range(n):
        if sievedata[i]==1: primes.append(i)
    return primes

primes=set(sieve(5000000))
numprimes=3
layers=1
a=9
while 10*numprimes>4*layers:
    layers+=1
    for i in range(3):
        a+=2*layers
        if isprime(a):
            numprimes+=1
    a+=2*layers
    f=numprimes/(4*layers+1.0)
width=2*layers+1
print width
