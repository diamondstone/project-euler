from math import sqrt,factorial

def sieve(n): #returns a list of all primes below n
    sievedata=[0]*2+[1]*(n-2)
    for i in range(1+int(sqrt(n))):
        if sievedata[i]==1:
            for j in range(2*i,n,i):
                sievedata[j]=0
    primes=[]
    for i in range(n):
        if sievedata[i]==1: primes.append(i)
    return primes

def countprimes(template): #counts primes that match template
    count=0
    s=0
    if template[0]=='*': s=1
    for n in range(s,10):
        teststring=template[:]
        for i in range(len(teststring)):
            if teststring[i]=='*': teststring[i]=str(n)
        teststring=reduce(lambda x,y: x+y,teststring)
        p=int(teststring)
        if p in primes:
            count+=1
    return count

def printprimes(template): #counts primes that match template
    if '*' not in template: return 1
    count=0
    s=0
    if template[0]=='*': s=1
    for n in range(s,10):
        teststring=template[:]
        for i in range(len(teststring)):
            if teststring[i]=='*': teststring[i]=str(n)
        teststring=reduce(lambda x,y: x+y,teststring)
        p=int(teststring)
        if p in primes:
            print p
            count+=1
    return count

def listproduct(list1,list2):
    output=[]
    for i in list1:
        for j in list2:
            output.append(i+j)
    return output
    
def maketemplates(length):
    digits=['0','1','2','3','4','5','6','7','8','9']
    first=['1','2','3','4','5','6','7','8','9','*']
    good=[]
    bad1=[]
    bad2=['1','3','7','9']
    for i in range(length-1):
        newgood=listproduct(first,good+bad1)+listproduct(['*'],bad2)
        bad1=listproduct(['0'],good+bad1)
        bad2=listproduct(digits,bad2)
        good=newgood
    return good

primes=sieve(10000000)
primes=set(primes)
templates=maketemplates(6)
for i in templates:
    n=countprimes(list(i))
    if n==8:
        print n,i
        printprimes(list(i))
