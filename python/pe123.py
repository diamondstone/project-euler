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

def r(p,n):
    if n%2:
        return (2*n*p)%(p**2)
    else:
        return 2
    

def test():
    primes=sieve(10**5)
    n=0
    while r(primes[n],n+1)<10**9:
        n+=1
    print n+1

def main():
    primes=sieve(10**7)
    n=0
    while r(primes[n],n+1)<10**10:
        n+=1
    print n+1

main()

