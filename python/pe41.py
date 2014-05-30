from math import sqrt,factorial

def isprime(n): #returns 1 if n is prime, 0 if n is composite
    if n<2:
        return None
    if n<4:
        return 1
    t=int(sqrt(n))
    for i in range(2,t+1):
        if n % i == 0: return 0
    return 1

def numtobasef(num,l): # computes the l-"digit" "base" factorial representation of num
    # there's probably a real name for this
    basef=[0]*l
    for i in range(l):
        basef[i]=num/factorial(l-i)
        num-=basef[i]*factorial(l-i)
    return basef

def baseftoperm(basef): # converts a base-factorial representation to the corresponding permutation
    basef.append(0)
    l=len(basef)
    perm=[0]*l
    for i in range(l):
        while perm[i] in perm[:i]: perm[i] += 1
        for j in range(basef[i]):
            perm[i]+=1
            while perm[i] in perm[:i]: perm[i] += 1
    return perm

def numtoperm(num,l):
    perm=map(lambda x:str(x+1),baseftoperm(numtobasef(num,l-1)))
    number=int(reduce(lambda x,y:x+y,perm))
    return number

for i in range(5040):
    p=numtoperm(i,7)
    if isprime(p): print p
