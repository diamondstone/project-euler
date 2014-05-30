file = open('pe81matrix.txt')

def transpose(matrix):
    newmatrix=[[matrix[j][i] for j in xrange(len(matrix))] for i in xrange(len(matrix[0]))]
    return newmatrix

matrix=[]
for line in file:
    matrix.append(map(int,line.strip().split(','))) #matrix[i] is the ith row
file.close()

matrix=transpose(matrix) #matrix[i] is now the ith column

sums=[matrix[i][:] for i in xrange(80)] #sums is a copy of matrix. We replace the [i][j] entry in sums with the min sum to [i][j], starting from column 1.
for c in xrange(1,80):
    for r in xrange(80):
        sums[c][r]+=sums[c-1][r]
    newcolumn=[0]*80
    while 1:
        for r in xrange(80):
            if r==0: newcolumn[r]=min(sums[c][r],matrix[c][r]+sums[c][r+1])
            elif r==79: newcolumn[r]=min(sums[c][r],matrix[c][r]+sums[c][r-1])
            else: newcolumn[r]=min(sums[c][r],matrix[c][r]+min(sums[c][r-1],sums[c][r+1]))
        if newcolumn==sums[c]:
            break
        sums[c]=newcolumn[:]

print min(sums[79])
        
        
