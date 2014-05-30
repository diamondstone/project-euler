file = open('pe81matrix.txt')

matrix=[]
for line in file:
    matrix.append(map(int,line.strip().split(',')))
file.close()

sums=[matrix[i][:] for i in xrange(80)] #sums is a copy of matrix. We replace the [i][j] entry in sums with the min sum to [i][j]
for s in xrange(1,79+79+1):
    for i in xrange(max(0,s-79),min(79,s)+1):
        j=s-i
        if i==0:
            sums[i][j]+=sums[i][j-1]
        elif j==0:
            sums[i][j]+=sums[i-1][j]
        else:
            sums[i][j]+=min(sums[i][j-1],sums[i-1][j])
print sums[79][79]
        
        
