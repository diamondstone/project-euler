from math import sqrt

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

primes=sieve(1000000)

for n in range(500,548): #summing more than 547 consecutive primes yields a total too large
    p=0
    i=0
    if n%2==0:
        p=sum(primes[0:n])
        if p in primes:
            print n,p
            continue
    while p<1000000:
        p=sum(primes[i:i+n])
        i+=1
        if p in primes:
            print n,p
            break
