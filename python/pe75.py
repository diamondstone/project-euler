import itertools

def gcd(n,m): #returns the greatest common denominator of n and m, using Euclidean algorithm. Algorithm runs for one cycle less if n<m.
    if n*m==0: return n+m
    while n>0:
        p=m
        m=n
        n=p%m
    return m

def perimeter_gen(): #generates perimeters of integer right triangles which are less than 1.5 million
    for m in xrange(1,866):
        for n in xrange(1+m%2,min(m,750000/m-m+1),2): #want 2*m**2+2*m*n<1500000
            if gcd(m,n)!=1: continue
            p=2*m**2+2*m*n
            for k in xrange(1,1500000/p+1):
                yield k*p

perimeters=set([])
duplicates=set([])
for i in perimeter_gen():
    if i in perimeters: duplicates.add(i)
    perimeters.add(i)
print len(perimeters)-len(duplicates) # 161667
