import itertools

def sieve(n): #returns a list of all primes below n
    sievedata=[0]*2+[1]*(n-2)
    for i in xrange(1+int(n**.5)):
        if sievedata[i]==1:
            for j in xrange(2*i,n,i):
                sievedata[j]=0
    primes=[]
    for i in xrange(n):
        if sievedata[i]==1: primes.append(i)
    return primes

scf=[]
primes=sieve(9000)
squares=map(lambda x: x**2, primes)
cubes=map(lambda x: x**3, primes)
cubes=cubes[:100]
fourths=map(lambda x: x**4, primes)
fourths=fourths[:50]
for s in squares:
    for c in cubes:
        for f in fourths:
            if s+c+f<50000000:
                scf+=[s+c+f]
scf=set(scf)
print len(scf)
