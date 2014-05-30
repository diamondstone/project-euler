import collections

# we are looking for subsets S of {1...n} with wo properties:
#   1) 1,n in S
#   2) p>1 in S => p=q+r for q,r in S (possibly the same)

def doublesum(S):
    return set([p+q for p in S for q in S])

def condition2(S):
    S2=doublesum(S)
    for s in S:
        if s not in S2: return False
    return true

def candidates(L,p): #given a set in increasing order L, returns a list of possible sums of L
    n=len(L)
    yielded=set()
    for i in xrange(n):
        for j in xrange(i,n):
            if p>=L[i]+L[j]>L[n-1]:
                l=L[i]+L[j]
                if l not in yielded:
                    yield l
                    yielded.add(l)

def effpowers(p): #returns a list of the powers of n computed in order to compute n**p in the most efficient way
    if p==1: return [1]
    if p==2:
        print 2,1,[1,2]
        return [1,2]
    possibilities=collections.deque()
    possibilities.append([1,2])
    while True:
        L=possibilities.popleft()
        for n in candidates(L,p):
            possibilities.append(L+[n])
            if n==p:
                print n,len(L),L+[n]
                return L+[n]

def m(k):
    return len(effpowers(k))-1

total=0
for k in xrange(70,90):
    total+=m(k)
