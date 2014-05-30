from math import sqrt

def factorize(n): #returns a list of the prime factors, with multiplicity.
    factors=[]
    p=2
    while n>1:
        if p>sqrt(n):
            factors.append(n)
            n=1
        elif n % p == 0:
            n=n/p
            factors.append(p)
        else:
            p+=1
    return factors

def product(iterable):
    p=1
    for i in iterable:
        p*=i
    return p

def rad(n):
    return product(set(factorize(n)))

def test1():
    for n in range(1,11):
        print n,rad(n)

def test2():
    E=[(rad(n),n) for n in range(1,11)]
    E.sort()
    for (i,j) in E: print (j,i)
    print "E(4) =",E[3][1]
    print "E(6) =",E[5][1]

def main():
    E=[(rad(n),n) for n in range(1,100001)]
    E.sort()
    print "E(1000) =",E[9999][1]

main()
