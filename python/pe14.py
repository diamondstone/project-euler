def collatz(n):
    if n % 2 == 0: return n/2
    return 3*n+1

def colchain(n):
    chain=[n]
    while n>1:
        n=collatz(n)
        chain.append(n)
    return chain

record=0

for n in range(1,1000000):
    length=len(colchain(n))
    if length>record:
        record=length
        print n,length
print 'finished'

    
