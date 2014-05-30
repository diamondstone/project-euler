import itertools

def isprime(n): #returns 1 if n is prime, 0 if n is composite
    if n<2:
        return None
    if n<4:
        return 1
    t=int(n**.5)
    for i in xrange(2,t+1):
        if n % i == 0: return 0
    return 1

def S(n,d):
    otherdigits=range(10)
    otherdigits.remove(d)
    #figure out M(n,d):
    for M in xrange(n,0,-1):
        S_=0
        N=0
        for L in itertools.combinations(xrange(n),M):
            for P in itertools.product(otherdigits,repeat=n-M):
                P=list(P)
                v=0
                for i in xrange(n):
                    if i in L:
                        v+=10**i*d
                    else:
                        v+=10**i*P.pop()
                if v>=10**(n-1):
                    if isprime(v):
                        S_+=v
                        N+=1
        if S_: break
    return S_

print sum([S(10,d) for d in xrange(10)])
