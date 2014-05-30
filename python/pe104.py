def pandigend(i): # checks whether the numbers i ends with the digits 1...9 in some order.
    digits=map(int,str(i))
    end=digits[-9:]
    end.sort()
    return end==[1,2,3,4,5,6,7,8,9]

def pandigstart(i): # checks whether the numbers i begins with the digits 1...9 in some order.
    digits=map(int,str(i))
    start=digits[:9]
    start.sort()
    return start==[1,2,3,4,5,6,7,8,9]

def fibendgen(): # generator for fibonacci sequence (mod 10 billion).
    i=1
    j=1
    while True:
        yield i
        k=i
        i=j
        j=(j+k)%10000000000

def fib(N,n,i,j): #computes the Nth fibonacci pair, starting from the nth pair (i,j)
    for it in xrange(N-n):
        k=i
        i=j
        j=(j+k)
    return (i,j)

n,i,j=1,1,1
N=0
count=0
for F in fibendgen():
    N+=1
    if pandigend(F):
        print N
        i,j=fib(N,n,i,j)
        n=N
        if pandigstart(i):
            break
