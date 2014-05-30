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

maxnum=0
besta=0
bestb=0

for a in range(-999,1000):
    for b in range(-999,1000):
        n=0
        while isprime(n**2+a*n+b): n+=1
        if n>maxnum:
            maxnum=n
            besta=a
            bestb=b
    print a
print 'best a = ',besta
print 'best b = ',bestb
print 'a*b = ',besta*bestb

