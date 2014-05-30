import itertools

def memoize(fn):
    memo={}
    def memoized_fn(*args):
        if args in memo:
            return memo[args]
        else:
            memo[args]=ret=fn(*args)
            return ret
    return memoized_fn

@memoize
def N(a,b,c):
    if a==0 and b==0:
        return c*(c-1)
    total=0
    if a>0: #add possibilities where last is A
        total+=N(a-1,b,c)*OP(A,8,c)/c/(c-1)
    if b>0: #add possibilities where last is B
        total+=N(a,b-1,c)*OP(B,8,c)/c/(c-1)
    return total

@memoize
def N_1984_mod_100mil(a,b): #N(a,b,1984) optimized with precomputed values and modulu 10^8
    if a==0 and b==0:
        return 3934272
    total=0
    if a>0: #add possibilities where last is A
        total+=N_1984_mod_100mil(a-1,b)*65269402
    if b>0: #add possibilities where last is B
        total+=N_1984_mod_100mil(a,b-1)*84582888
    return total%10**8    

@memoize
def AB_ss(c):
    return (c-1)*(c-2)*(c-1+(c-2)*(c-3))

@memoize
def A(c): #Number of colorings of graph A, with colors on left fixed
# Node diagram:
# 0 1
#  2
#  3
#  4
# 5 6
    ways=0
    Edges=[(0,1),(0,2),(0,5),(1,2),(1,6),(2,3),(3,4),(4,5),(4,6),(5,6)]
    for C in itertools.product(xrange(c),repeat=7):
        valid=True
        for (i,j) in Edges:
            if C[i]==C[j]: valid=False
        if valid: ways+=1
    return ways

@memoize
def B(c): #Number of colorings of graph B, with colors on left fixed
# Node diagram:
# 0 1
#  2
#  3
#  4
# 5 6    ways=0
    ways=0
    Edges=[(0,1),(0,2),(0,5),(1,2),(1,6),(2,3),(3,4),(4,5),(4,6)]
    for C in itertools.product(xrange(c),repeat=7):
        valid=True
        for (i,j) in Edges:
            if C[i]==C[j]: valid=False
        if valid: ways+=1
    return ways

def p(n,k,x): #n-1st degree polynomial which is equal to 0 at 1...n except at k, equal to 1 at k, evaluated at x
    numerator=1
    denominator=1
    for i in range(1,k):
        numerator*=x-i
        denominator*=k-i
    for i in range(k+1,n+1):
        numerator*=x-i
        denominator*=k-i
    return numerator/denominator

def OP(f,n,x): #returns the xth term of the optimal polynomial generating function for the first n terms of the sequence given by the function f.
    nextval=0
    for i in xrange(1,n+1):
        nextval+=f(i)*p(n,i,x)
    return nextval

def test1():
    print "N(1,0,3) =",N(1,0,3)
    print "N(0,2,4) =",N(0,2,4)
    print "N(2,2,3) =",N(2,2,3)

def test2():
    for n in range(10):
        print B(n+1),OP(B,8,n+1)

def test3():
    print OP(A,8,1984)
    print OP(B,8,1984)

print N_1984_mod_100mil(25,75)
