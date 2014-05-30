from math import sqrt

def divisors(n): #returns a list of the proper divisors of an integer n>1
    divs = [1]
    for i in range(2,int(sqrt(n))+1):
        if n%i==0: divs.append(i)
    l=len(divs)-1
    for i in range(l,0,-1):
        if divs[i]**2 != n: divs.append(n/divs[i])
    return divs

def isabundant(n):
    if sum(divisors(n))>n: return n
    return 0

def nonabundantsum(n):
    for i in range(n):
        if isabundant(i)*isabundant(n-i): return 0
    return n

s=0
for i in range(28124):
    s+=nonabundantsum(i)
print s
