def rectangles_p(w,h): #parallel to axes
    return w*(w+1)*h*(h+1)/4

def subrectangles_d(w,h,l1,l2): #diagonal to axes with lengths l1,l2
    twice_height=l1+l2+1
    total=max(0,(h+1-twice_height/2)*(1+w-(l2+1)/2-(l1+1)/2)) #top is a corner
    total+=max(0,(h-(twice_height-1)/2)*(w-l2/2-l1/2)) #top is a midpoint
    return total

def rectangles_d(w,h):
    l=2*min(w,h)
    total=0
    for i in xrange(1,l):
        for j in xrange(1,l):
            total+=subrectangles_d(w,h,i,j)
    return total
    
def rectangles(w,h):
    return rectangles_p(w,h)+rectangles_d(w,h)

def main():
    total=0
    for w in range(1,48):
        for h in range(1,44):
            total+=rectangles(w,h)
    print total

main()
