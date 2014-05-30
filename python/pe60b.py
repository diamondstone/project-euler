import pickle
from math import sqrt

# Comment notation: for integers a, b, a_b denotes int(str(a)+str(b))

def sieve(n): #returns a list of all primes below n
    s=int(sqrt(n))
    while s**2<n: s+=1
    sievedata=[0]*2+[1]*(n-2)
    for i in range(s+1):
        if sievedata[i]==1:
            for j in range(2*i,n,i):
                sievedata[j]=0
    primes=[]
    for i in range(n):
        if sievedata[i]==1: primes.append(i)
    return primes

def iscomposite(n): #returns 0 if n is prime, 1 if n is composite
    if n in primes: return 0
    return 1

def match(p,l): # p is a prime, l is a list of numbers. Returns 1 if n_p and p_n are primes for all n in l
    for n in l:
        if d[(n,p)]==False: return 0
    return 1

top=10000
sp=sieve(top) #small primes
f=open('primeset.txt')
primes=pickle.load(f)
f.close
print "loaded primeset"

d={} # d is a dictionary of prime pairs p,q which concatenate to primes in both orders
for p in sp:
    for q in [r for r in sp if r>p]:
        if iscomposite(int(str(q)+str(p))): d[(p,q)]=False
        elif iscomposite(int(str(p)+str(q))): d[(p,q)]=False
        else: d[(p,q)]=True
print "finished building dictionary"

families = []
for p in sp:
    new=[]
    for l in families:
        if match(p,l): new.append(l+[p])
    families.append([p])
    families=families+new
for f in families:
    if len(f)>4: print f,sum(f)
