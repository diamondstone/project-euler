from math import factorial

count=0
for n in range(23,101):
    for r in range(4,n-3):
        if factorial(n)>1000000*factorial(r)*factorial(n-r): count+=1
print count
