def triangles(n):
    count=0
    for x1 in xrange(n+1):
        for x2 in xrange(n+1):
            for y1 in xrange(n+1):
                for y2 in xrange(n+1):
                    if (x1,y1)==(0,0) or (x2,y2)==(0,0) or (x1,y1)==(x2,y2): continue
                    if x1*x2==-y1*y2: count+=1
                    elif y1*(y1-y2)==-x1*(x1-x2): count+=1
                    elif y2*(y1-y2)==-x2*(x1-x2): count+=1
    return count/2 #we're doublecounting

print triangles(2)
print triangles(50)
