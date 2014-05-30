def twodigitnum(a,b): return 10*a+b

file = open('pe18triangle.txt')
rows=15
triangle=[]

for i in range(rows):
    newline=list(file.readline())
    l=len(newline)-1
    newlinea=map(int,newline[0:l:3])
    newlineb=map(int,newline[1:l:3])
    newline=map(twodigitnum,newlinea,newlineb)
    triangle.append(newline)
# triangle now contains the triangle grid as a list of rows, which are lists of numbers.
# There's got to be a better way of interpreting a string with numbers separated by spaces as a list of numbers.

for i in range(rows-2,-1,-1):
    for j in range(i+1):
        triangle[i][j]=triangle[i][j]+max(triangle[i+1][j],triangle[i+1][j+1])

print triangle[0][0]
