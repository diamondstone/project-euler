from math import sqrt

def divisors(n): #returns a list of the proper divisors of an integer n>1
    divisors = [1]
    for i in range(2,int(sqrt(n))+1):
        if n%i==0: divisors.append(i)
    l=len(divisors)-1
    for i in range(l,0,-1):
        if divisors[i]**2 != n: divisors.append(n/divisors[i])
    return divisors

def isperfect(n):
    if sum(divisors(n))==n: return n
    return 0

def isfriendly(n):
    if isperfect(n): return 0
    if sum(divisors(sum(divisors(n))))==n: return n
    return 0

print "the friendly numbers less than 10,000 are:"
list=[]
for i in range(10001):
    if isfriendly(i): list.append(i)
print list
print "their sum is",sum(list)
