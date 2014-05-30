from math import sqrt

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

def isprime(n): #returns 1 if n is prime, 0 if n is composite
    if n<5000000:
        return n in primes
    t=int(sqrt(n))
    while t*t<n:
        t+=1
    for i in range(2,t):
        if n % i == 0: return 0
    return 1

def match(i): #returns set of small primes p such that i_p and p_i are both prime, where a_b is the number whose decimal expansion is the concatenation of the expansions of a and b
    goodprimes=set([p for p in sp if isprime(int(str(i)+str(p))) and isprime(int(str(p)+str(i)))])
    return goodprimes
    

top=10000 #we only consider possible tuples of primes less than top

primes=set(sieve(5000000))
sp=set(sieve(top)).difference(set([2,5]))
# sp = small primes. We discard 2 and 5 as no primes other than 2 and 5 end in 2 or 5.
print "sieve complete"
emptyset=set([])

pd={} #dictionary of small odd primes, primes that pair with them
for i in sp:
    pd[i]=None

for i in pd.keys():
    if pd.get(i)==None: pd[i]=match(i)
    s=pd.get(i).difference(set(range(i)))
    for j in s:
        if pd.get(j)==None: pd[j]=match(j)
        t=s.intersection(pd.get(j)).difference(set(range(j)))
        for k in t:
            if pd.get(k)==None: pd[k]=match(k)
            r=t.intersection(pd.get(k)).difference(set(range(k)))
            for l in r:
                if pd.get(l)==None: pd[l]=match(l)
                q=r.intersection(pd.get(l)).difference(set(range(l)))
                for m in q: print i,j,k,l,m
print "done"
