def twodigitnum(a,b): return 10*a+b

file = open('pe11array.txt')
array=[]

for i in range(20):
    newline=list(file.readline())
    l=len(newline)
    newlinea=map(int,newline[0:l:3])
    newlineb=map(int,newline[1:l:3])
    newline=map(twodigitnum,newlinea,newlineb)
    array.append(newline)
#array now contains the 20x20 grid as a list of 20 lists of 20 numbers.

maxprod=0
#iterate over horizontal products
for i in range(20):
    for j in range(17):
        prod=array[i][j]*array[i][j+1]*array[i][j+2]*array[i][j+3]
        if prod>maxprod: maxprod=prod

#iterate over vertical products
for i in range(17):
    for j in range(20):
        prod=array[i][j]*array[i+1][j]*array[i+2][j]*array[i+3][j]
        if prod>maxprod: maxprod=prod

#iterate over diagonal products
for i in range(17):
    for j in range(17):
        prod1=array[i][j]*array[i+1][j+1]*array[i+2][j+2]*array[i+3][j+3]
        prod2=array[i+3][j]*array[i+2][j+1]*array[i+1][j+2]*array[i][j+3]
        if prod1>maxprod: maxprod=prod1
        if prod2>maxprod: maxprod=prod2
        
print maxprod        
