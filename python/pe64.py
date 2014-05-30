import itertools
from math import sqrt

def gcd(n,m): #returns the greatest common denominator of n and m, using Euclidean algorithm. Algorithm runs for one cycle less if n<m.
    if n*m==0: return n+m
    while n>0:
        p=m
        m=n
        n=p%m
    return m

def cfrac(n): #generates the continued fraction for sqrt(n); errors if n is a perfect square.
#general mechanism: take (a*rt(n)+b)/c, subtract integer part to get (a*rt(n)+b')/c, invert to get c/(a*rt(n)+b'), rationalize, and simplify.
    expansion=[]
    remainders=[]
    a,b,c=1,0,1
    while (a,b,c) not in remainders:
        expansion.append(int((a*sqrt(n)+b)/c))
        remainders.append((a,b,c))
        b-=c*expansion[-1]
        cc=a*a*n-b*b
        a*=c
        b*=(-1)*c
        c=cc
        d=gcd(a,(gcd(b,c)))
        a=a/d
        b=b/d
        c=c/d
    return expansion

def cfraclength(n): #generates the continued fraction for sqrt(n); errors if n is a perfect square.
#general mechanism: take (a*rt(n)+b)/c, subtract integer part to get (a*rt(n)+b')/c, invert to get c/(a*rt(n)+b'), rationalize, and simplify.
    expansion=[]
    remainders=[]
    a,b,c=1,0,1
    while (a,b,c) not in remainders:
        expansion.append(int((a*sqrt(n)+b)/c))
        remainders.append((a,b,c))
        b-=c*expansion[-1]
        cc=a*a*n-b*b
        a*=c
        b*=(-1)*c
        c=cc
        d=gcd(a,(gcd(b,c)))
        a=a/d
        b=b/d
        c=c/d
    return len(remainders)-remainders.index((a,b,c))

count=0
s=2
n=2
while n<100:
    if n==s*s:
        s+=1
        n+=1
    if cfraclength(n)%2: count+=1
    print n, cfrac(n), cfraclength(n)
    n+=1
print count
