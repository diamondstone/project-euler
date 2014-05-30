def u(n):
    return 1-n+n**2-n**3+n**4-n**5+n**6-n**7+n**8-n**9+n**10

def c(n):
    return n**3

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

total=0
for k in xrange(1,11):
    if OP(u,k,k+1)!=u(k+1):
        total+=OP(u,k,k+1)
print total
