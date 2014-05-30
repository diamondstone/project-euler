class memoize:
    def __init__(self,f):
        self.f=f
        self.memo={}

    def __call__(self,*args):
        if args in self.memo: return self.memo[args]
        self.memo[args]=ret=self.f(*args)
        return ret

def gcd(n,m):
    if n*m==0:
        return n+m
    return gcd(m,n%m)

@memoize
def capacitance_values(n):
    if n<1: return set([])
    if n==1: return set([(1,1)])
    L=set([])
    for i in xrange(1,n/2+1):
        for p1,q1 in capacitance_values(i):
            for p2,q2 in capacitance_values(n-i):
                q=q1*q2
                p=p1*q2+p2*q1
                d=gcd(p,q)
                L.add((p/d,q/d))
                L.add((q/d,p/d))
    L=L.union(capacitance_values(n-1))
    return L

def D(n):
    return len(set(capacitance_values(n)))

print D(18)
