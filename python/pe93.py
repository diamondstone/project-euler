import itertools as it

operations='+','-','*','/','m','d'

def arithmetic(a,b,bool,o):
    if o=='+': return (a+b,bool)
    if o=='-': return (a-b,bool)
    if o=='m': return (b-a,bool)
    if o=='*': return (a*b,bool)
    if o=='/':
        if b!=0: return (1.*a/b,bool)
        else: return (0,False)
    if o=='d':
        if a!=0: return (1.*b/a,bool)
        else: return (0,False)
    return (0,False)

def expressible(A): #given set N of 4 distinct numbers, returns all possible values
    values=[]
    for B in it.permutations(A,4):
        for o1 in operations:
            for o2 in operations:
                for o3 in operations:
                    e,bool=arithmetic(B[2],B[3],True,o1)
                    e,bool=arithmetic(B[1],e,bool,o2)
                    e,bool=arithmetic(B[0],e,bool,o3)
                    if bool and e>0 and e==1.*int(e): values.append(int(e))
                    e,bool1=arithmetic(B[2],B[3],True,o1)
                    f,bool2=arithmetic(B[0],B[1],True,o2)
                    bool = bool1 and bool2
                    e,bool=arithmetic(e,f,bool,o3)
    values.sort()
    last=values.pop()
    newvalues=[]
    newvalues.append(last)
    while(len(values)>0):
        next=values.pop()
        if next!=last:
            newvalues.append(next)
            last=next
    newvalues.reverse()
    return newvalues

def nonexpressible(A): #given set N of 4 distinct numbers, returns least nonexpressible natural number
    L=expressible(A)
    for i in range(len(L)):
        if L[i]!=i+1: return i+1
    return len(L)+1

best=29
bestA=1,2,3,4
for A in it.combinations(range(1,10),4):
    l=nonexpressible(A)
    if l>best:
        best=l
        bestA=A
print bestA,best
