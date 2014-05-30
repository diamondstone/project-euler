class memoize:
    def __init__(self,f):
        self.f=f
        self.memo={}
    def __call__(self,*args):
        if args in self.memo: return self.memo[args]
        self.memo[args]=ret=self.f(*args)
        return ret

def triominoes():
    L1=[(0,0),(0,1),(1,0)]
    L2=[(0,0),(0,1),(1,1)]
    L3=[(0,0),(1,0),(1,1)]
    L4=[(0,0),(0,1),(-1,1)]
    S1=[(0,0),(0,1),(0,2)]
    S2=[(0,0),(1,0),(2,0)]
    return [L1,L2,L3,L4,S1,S2]

def firstblank(partialtiling):
    for y in xrange(len(partialtiling[0])):
        for x in xrange(len(partialtiling)):
            if partialtiling[x][y]==0:
                return x,y
    return None,None
                    
@memoize
def tile(PT):
    x,y=firstblank(PT)
    if x==None: return 1
    ways=0
    for p in range(6):
        PTcopy=make_mut(PT)
        fit=True
        for dx,dy in triominoes()[p]:
            if x+dx<0 or x+dx>=len(PT) or y+dy>=len(PT[0]):
                fit=False
                continue
            if PTcopy[x+dx][y+dy]!=0: fit=False
            PTcopy[x+dx][y+dy]=1
        if fit: ways+=tile(make_immut(PTcopy))
    return ways

def draw(T):
    S=""
    for row in T:
        for i in row:
            S+=str(i)+" "
        S+="\n"
    return S            

def numways(w,h):
    if w>h:
        return numways(h,w)
    PT=make_immut([[0]*h for i in xrange(w)])
    return tile(PT)

def make_mut(t):
    return map(list,t)

def make_immut(t):
    return tuple(map(tuple,t))

print numways(9,12)
