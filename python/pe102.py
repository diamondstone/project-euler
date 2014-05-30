def contains0(triangle):
    a,b,c=convexcomb(triangle)
    return (a>0 and b>0 and c>0) or (a<0 and b<0 and c<0)


def convexcomb(vector): #takes a 6-vector, thought of as 3 2-vectors, and returns the coefficients (multiplied by det) in the convex combination giving 0.
    x1,x2,y1,y2,z1,z2=tuple(vector)
    det=(y2-z2)*(x1-z1)-(z1-y1)*(z2-x2)
    a=(z2-y2)*z1+(y1-z1)*z2
    b=(x2-z2)*z1+(z1-x1)*z2
    c=det-a-b
    return a,b,c
 
file = open('pe102triangles.txt')
count=0
for line in file:
    triangle=map(int,line.strip().split(','))
    if count<3: print contains0(triangle)
    if contains0(triangle): count+=1
print count
