from math import sqrt

def cycle(n,r): # rotates the number n by r
    str1=str(n)
    l=len(str1)
    str2=''
    for i in range(l):
        str2+=str1[(i+r)%l]
    return int(str2)

def isprime(n): #returns n if n is prime, 0 if n is composite (or bad arguments like 0, 1, negatives)
    if n<2:
        return 0
    if n<4:
        return 1
    t=int(sqrt(n))
    for i in range(2,t+1):
        if n % i == 0: return 0
    return n

def cyclicprime(n):
    for r in range(len(str(n))):
        if isprime(cycle(n,r))==0: return 0
    return n

cycleprimes=[]
for i in range(2,999999):
    if cyclicprime(i): cycleprimes.append(i)
print cycleprimes
print len(cycleprimes)
