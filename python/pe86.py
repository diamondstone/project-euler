# A spider, S, sits in one corner of a cuboid room, measuring 6 by 5 by 3, and a fly, F, sits in the opposite corner. By travelling on the surfaces of the room the shortest "straight line" distance from S to F is 10 and the path is shown on the diagram.

# By considering all cuboid rooms with integer dimensions, up to a maximum size of M by M by M, there are exactly 2060 cuboids for which the shortest route has integer length when M=100, and this is the least value of M for which the number of solutions first exceeds two thousand; the number of solutions is 1975 when M=99.

# Find the least value of M such that the number of solutions first exceeds one million.

def issquare(n):
    if int(n**0.5)**2==n: return True
    return False

count=0
M=0
while count<1000000:
    M+=1
    for s in xrange(2,2*M+1):
        if issquare(s**2+M**2): count+=min(s/2,M+1-(s+1)/2) # of ways to write s as a sum of two numbers between 1 and M. s is between 2 and 2M
    if M%100==0:
        print "M =",M,": count =",count
print "M =",M,": count =",count
