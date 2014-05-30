from math import sqrt

def divisors(n): #returns a list of the proper divisors of an integer n>1
    divisors = [1]
    for i in xrange(2,int(sqrt(n))+1):
        if n%i==0: divisors.append(i)
    l=len(divisors)-1
    for i in xrange(l,0,-1):
        if divisors[i]**2 != n: divisors.append(n/divisors[i])
    return divisors

def amicablenext(n):
    return sum(divisors(n))

def chainlength(n):
    chain=[]
    while n not in chain:
        if n>1000000: return 0
        chain.append(n)
        n=amicablenext(n)
    if n==chain[0]: return len(chain)
    else: return 0

maxlength=1
bestn=0
for n in xrange(1000000):
    l=chainlength(n)
    if l>maxlength:
        maxlength=l
        bestn=n
print bestn, "has a length", maxlength, "chain"
    
