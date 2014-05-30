def gcd(n,m):
    if n*m==0: return n+m
    while n>0:
        p=m
        m=n
        n=p%m
    return m

def eulerphi(n):
    phi=0
    for i in xrange(1,n+1):
        if gcd(i,n)==1: phi+=1
    return phi

for i in xrange(5):
    bestn=1
    bestv=1
    for n in xrange(1,10**i+1):
        v=(1.0*n)/eulerphi(n)
        if v>bestv:
            bestv=v
            bestn=n
    print bestn
print "Obvious pattern is obvious."
