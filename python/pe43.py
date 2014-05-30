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

def pandigit(n):
    perm=map(str,baseftoperm(numtobasef(n+362880,9)))
    number=reduce(lambda x,y:x+y,perm)
    return number

def superdivis(p):
    primes=[2,3,5,7,11,13,17]
    for i in range(7):
        if int(p[1+i:4+i])%primes[i]!=0: return 0
    return 1

total=0
for i in range(3265919):
    p=pandigit(i)
    if superdivis(p):
        print p
        total+=int(p)
print 'total is',total


#Note: this is a stupid and slow way of going about things. We should build these numbers from back to front, making sure the last three digits are divisible by 17, then the second-to-last three are divisible by 13, etc., with a tree search. This will be vastly faster.
