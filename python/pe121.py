from math import factorial

def memoize(fn):
    memo={}
    def memoized_fn(*args):
        if args in memo:
            return memo[args]
        else:
            ret=memo[args]=fn(*args)
            return ret
    return memoized_fn

@memoize
def ways(k,n): #number of ways of getting k blue disks in an n-round game
    if k>n: return 0
    if k==n: return 1
    if k<0: return 0
    return n*ways(k,n-1)+ways(k-1,n-1)

def invwinprob(n): #inverse win probability, rounded down
    winningways=sum([ways(k,n) for k in xrange(n/2+1,n+2)])
    totalways=factorial(n+1)
    return totalways/winningways

print invwinprob(15)
