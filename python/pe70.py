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

minp=21.0/12
bestn=21
primes=sieve(10000)
for p in primes:
    for q in primes:
        if p*q>10000000: continue
        n=p*q
        phi=n-1-(n-1)/p-(n-1)/q
        a=list(str(n))
        b=list(str(phi))
        a.sort()
        b.sort()
        if a==b:
            p=1.0*n/phi
            if p<minp:
                minp=p
                bestn=n
print bestn
