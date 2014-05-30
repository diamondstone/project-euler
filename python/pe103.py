import itertools

def condition1(L): #L a list of integers
    sums=set([])
    for n in xrange(1,len(L)/2+1):
        for A in itertools.combinations(L,n):
            if sum(A) in sums: return False
            sums.add(sum(A))
    return True

def condition2(L): #L a sorted list of integers
    n=len(L)
    for i in xrange(2,n):
        if sum(L[:i])<=sum(L[1-i:]):
            return False
    return True

def special(L):
    return condition1(L) and condition2(L)

def setsum(S,n,l): #generator for all n-element subsets with sum S and all elements at least l.
    if n==1:
        if S>=l: yield [S]
        return
    u=(2*S+n*(1-n))/(2*n)
    for i in xrange(l,u+1):
        for L in setsum(S-i,n-1,i+1):
            yield [i]+L

def specialsetsum(S,n,L): #generator for all n-element special subsets with initial segment L.
    if len(L)==n:
        yield L
        return
    n1=n-len(L)
    S1=S-sum(L)
    if L:
        l=L[-1]+1
    else:
        l=1
    u=(2*S1+n1*(1-n1))/(2*n1)
    for i in xrange(l,u+1):
        if special(L+[i]):
            for L1 in specialsetsum(S,n,L+[i]):
                yield L1

def findspecial(S,n):
    for L in specialsetsum(S,n,[]):
        print L,"is a special set with sum",S
        return L
    print "There are no",n,"element special sets with sum",S
    return None

def main(n,S=0):
    if S==0:
        S=n*(n+1)/2
    while True:
        if findspecial(S,n): return
        S+=1

def test():
    for L in setsum(18,3,1):
        print L

main(7,255) #checked through 248.
