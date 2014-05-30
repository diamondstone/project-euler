def reverse(n):
    m=0
    while n>0:
        m=10*m+n-10*(n/10)
        n=n/10
    return m

def palindrome(n):
    if n == reverse(n):
        return 1
    else:
        return 0

k=0
for i in range(100,999):
    for j in range(100,999):
        if palindrome(i*j):
            if i*j>k: k=i*j
print k
