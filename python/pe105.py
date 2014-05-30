import itertools

def choose_subsets(P,n,m): #yields all length n,m subsets
    for Q in itertools.combinations(P,n+m):
        for R in itertools.combinations(range(n+m),n):
            A=[]
            B=[]
            for k in xrange(n+m):
                if k in R:
                    A.append(Q[k])
                else:
                    B.append(Q[k])
            yield (A,B)

def condition1(L): #L a list of integers
    N=len(L)
    for i in xrange(2,N/2+1):
        for (A,B) in choose_subsets(L,i,i):
            if sum(A)==sum(B):
#                print L,"fails condition 1. Witness:"
#                print A
#                print B
                return False
    return True

def condition2(L): #L a sorted list of integers
    n=len(L)
    for i in xrange(2,n):
        if sum(L[:i])<=sum(L[1-i:]):
            print L,"fails condition 2. Witness:"
            print L[:i]
            print L[1-i:]
            return False
    return True

def special(L):
    return condition1(L) and condition2(L)

def main():
    file = open('pe105sets.txt')
    total=0
    for line in file:
        L=map(int,line.strip().split(','))
        L.sort()
        if special(L): total+=sum(L)
    print total

def test():
    file = open('pe105sets.txt')
    count=0
    a=map(int,file.readline().strip().split(','))
    a.sort()
    print a
    print special(a)
    b=map(int,file.readline().strip().split(','))
    b.sort()
    print b
    print special(b)

main()
