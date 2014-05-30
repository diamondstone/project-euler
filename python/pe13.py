def add(a,b): return a+b

precision=15 #we calculate the sum using only the first precision digits, because truncating after the 10^n place reduces the sum by at most 10^(n+3).

file = open('pe13array.txt')
array=[]

for i in range(100):
    newline=file.readline()
    newint=int(newline[0:precision])
    array.append(newint)
#array now contains the 100 50-digit numbers, truncated to the first precision digits, as a list.

sum=reduce(add, array)
print sum
