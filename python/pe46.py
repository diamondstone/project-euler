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

for i in range(9,10000,2):
    if isprime(i)==0:
        for n in range(1+int(sqrt(i/2))):
            if isprime(i-2*(n**2)):
                break
        else:
            print i
            quit()
