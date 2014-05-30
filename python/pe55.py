def reverse(n): #returns the number with base-10 expansion the reverse of n
    d=str(n)
    r=''
    l=len(d)
    for i in range(l):
        r=d[i]+r
    n=int(r)
    return n

def palindrome(n):
    if n==reverse(n): return 1
    return 0

def lychrel(n):
    for i in range(50):
        n=n+reverse(n)
        if palindrome(n): return 0
    return 1

count=0
for n in range(10000):
    if lychrel(n): count+=1
print count
    
