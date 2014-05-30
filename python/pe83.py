file = open('pe83matrix.txt')

def transpose(matrix):
    newmatrix=[[matrix[j][i] for j in xrange(len(matrix))] for i in xrange(len(matrix[0]))]
    return newmatrix

def makearray(n,m,k=0): #makes an n by m array, with all entries equal to k
    newmatrix=[[k for j in xrange(n)] for i in xrange(m)]
    return newmatrix


matrix=[]
for line in file:
    matrix.append(map(int,line.strip().split(','))) #matrix[i] is the ith row
file.close()

sums=makearray(80,80)
while 1:
    newsums=makearray(80,80) # newsums[i][j] is the [i][j] entry in sums with matrix[i][j]+the min neighbor of [i][j] in sums.
    for i in xrange(80):
        for j in xrange(80):
            neighbormin=500000 #guaranteed to be at least the min of the neighbors.
            if i>0: neighbormin=min(neighbormin,sums[i-1][j])
            if i<79: neighbormin=min(neighbormin,sums[i+1][j])
            if j>0: neighbormin=min(neighbormin,sums[i][j-1])
            if j<79: neighbormin=min(neighbormin,sums[i][j+1])
            newsums[i][j]=matrix[i][j]+neighbormin
    newsums[0][0]=matrix[0][0]
    if newsums==sums: break
    sums=newsums

print sums[79][79]  
print [sums[i][:5] for i in xrange(5)]
sums[0][0]+=1
print [sums[i][:5] for i in xrange(5)]
