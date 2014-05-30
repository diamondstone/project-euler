import itertools
from math import factorial

def choose(n,k):
    return factorial(n)/factorial(n-k)/factorial(k)

def isincr(n):
    while n>9:
        d1=n%10
        n=n/10
        d2=n%10
        if d2>d1: return False
    return True

def isdecr(n):
    while n>9:
        d1=n%10
        n=n/10
        d2=n%10
        if d2<d1: return False
    return True

def isbouncy(n):
    if isincr(n): return False
    if isdecr(n): return False
    return True

def slownonbouncy(k): #returns number of bouncy numbers with at most k digits.
    numbouncy=0
    for i in xrange(1,10**k):
        i+=1
        if isbouncy(i): numbouncy+=1
    return 10**k-1-numbouncy

def slowdecr(k): #returns number of increasing numbers with exactly k digits.
    numdecreasing=0
    for i in xrange(10**(k-1),10**k):
        if isdecr(i): numdecreasing+=1
    return numdecreasing

#given an increasing k-digit number n=d_0,d_1,...,d_{k-1}, let f(n) be the length k sequnce d_0-1,d_1-d_0,...,d_{k-1}. f is one-to-one, and the range of f is the set of sequence of nonnegative numbers, of length k, with sum between 0 and 8. With sum s, there are choose(s+k-1,k-1) such sequences, so there are, in total sum([choose(s+k-1,k-1) for s in range(9)]) increasing k-digit numbers. Thus we have

def numincr(k): #number of increasing k-digit numbers
    return sum([choose(s+k-1,k-1) for s in range(9)])

#similarly,

def numdecr(k):
    return sum([choose(s+k-1,k-1) for s in range(10)])-1

def fastnonbouncy(k):
    total=0
    for i in xrange(1,k+1):
        total+=numincr(i)+numdecr(i)-9
    return total

def main():
    print fastnonbouncy(100)
       
main()
