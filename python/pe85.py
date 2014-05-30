from math import factorial,sqrt

def choose(n,k):
    return factorial(n)/factorial(k)/factorial(n-k)

def rectangles(n,m):
    return choose(n+1,2)*choose(m+1,2)

def abs(n):
    if n<0: return -1*n
    return n

best=2000000
for n in xrange(1,54):
    for m in xrange(int(sqrt(8000000.0/n/(n+1)))-1,int(sqrt(8000000.0/n/(n+1)))+2):
        error=abs(2000000-rectangles(n,m))
        if error<best:
            best=error
            size=n*m
print size,best
