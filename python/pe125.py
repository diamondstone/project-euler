from time import time

# Method 1: iterate through palindromes, check whether palindrome is a sum of squares.

def palindrome(n,b):
    if b: return int(str(n)+reverse(str(n)))
    else: return int(str(n)+reverse(str(n)[0:-1]))

def palindromes(n):
    for d in xrange(1,n+1):
        for k in xrange(10**((d-1)/2),10**((d+1)/2)):
            yield palindrome(k,1-d%2)

def ss(bot,top):
    return sum([i**2 for i in xrange(bot,top+1)])

def iss(n):
    for bot in xrange(1,(n*.5)**.5+1):
        top=bot+1
        while ss(bot,top)<n:
            top*=2
        t1=top/2
        t2=top
        while t2>t1+1:
            top=(t1+t2)/2
            if ss(bot,top)<n:
                t1=top
            else:
                t2=top
        if ss(bot,t2)==n: return True
    return False

def method1(d):
    total=0
    for n in palindromes(d):
        if iss(n):
            total+=n
    return total

# method 2: iterate through sums of squares, check whether sum is a palindrome

def ssit(maxsum):
    for a in xrange(1,(maxsum*.5)**.5+1):
        total=a**2+(a+1)**2
        a+=2
        while total<maxsum:
            yield total
            total+=a**2
            a+=1

def reverse(s):
    r=""
    for c in s: r=c+r
    return r

def ispalindrome(s):
    return str(s)==reverse(str(s))

def method2(d):
    pset=set()
    for s in ssit(10**d):
        if ispalindrome(s):
            pset.add(s)
    return sum(pset)

def test():
    for d in xrange(1,7):
        start=time()
        print "Method 1: S(%s)=%s in %s seconds"%(d,method1(d),time()-start)
        start=time()
        print "Method 2: S(%s)=%s in %s seconds"%(d,method2(d),time()-start)

# Testing shows that method 2 is far superior to method 1.

print method2(8)
