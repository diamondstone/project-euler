import collections

def layersize(x,y,z,l):
    return 2*(x*y+y*z+x*z)+4*(x+y+z)*(l-1)+4*(l-2)*(l-1)

# if layersize=n, then x<=n/4, y<=n/(2x), z<=n/(2x+2y)
# l<=2+n**.5/2, l<=n/(4x+4y+4z)+1

def findC(maxn,target):
    counter=collections.Counter()
    for x in xrange(1,maxn/4+1):
        for y in xrange(1,min(x+1,maxn/x/2+1)):
            for z in xrange(1,min(y+1,maxn/(x+y)/2+1)):
                for l in xrange(1,min(int(maxn**.5)/2+3,maxn/(x+y+z)/4+2)):
                    counter[layersize(x,y,z,l)]+=1
    for i in xrange(maxn):
        if counter[i]==target:
            return i
    return findC(maxn*2,target)
            

print findC(50,1000)
