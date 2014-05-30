import pickle
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

f=open('primeset.txt')
primes=pickle.load(f)
f.close
numprimes=3
layers=1
a=9
while 10*numprimes>4*layers:
    layers+=1
    for i in range(3):
        a+=2*layers
        if a in primes:
            numprimes+=1
    a+=2*layers
    f=numprimes/(4*layers+1.0)
width=2*layers+1
print width
if width**2>49979687:
    print "ERROR: Prime list too short"
    print "numbers up to",width**2,"considered"
    print "Prime list goes up to 49,979,687"
