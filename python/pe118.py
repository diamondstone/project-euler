from math import sqrt
import itertools

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

primes=set(sieve(10**7))

def isprime(n): #returns 1 if n is prime, 0 if n is composite
    if n<10**7:
        return (n in primes)
    t=int(sqrt(n))
    for i in xrange(2,t+1):
        if n % i == 0: return 0
    return 1


def alldigprimesets(digitset,maxp=10**9):
    if len(digitset)==0:
        yield []
        return
    for p in primedigits(digitset,maxp):
        newdigits=digitset.difference(digits(p))
        for L in alldigprimesets(newdigits,p):
            yield L+[p]

def digits(p):
    digits=set()
    while p:
        digits.add(p%10)
        p=p/10
    return digits
    
def primedigits(digitset,maxp=10**9):
    for n in range(1,len(digitset)+1):
        for L in itertools.permutations(digitset,n):
            p=sum([L[i]*10**i for i in xrange(len(L))])
            if isprime(p) and p<maxp: yield p

def main():
    digitset=set(range(1,10))
    total=0
    for L in alldigprimesets(digitset):
        total+=1
    print total

main()
