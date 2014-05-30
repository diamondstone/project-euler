def reverse10(n): # reverses the number n, in base 10
    str1=str(n)
    l=len(str1)
    str2=''
    for i in range(l):
        str2+=str1[l-1-i]
    return int(str2)

def reverse2(n):
    m=0
    while n>0:
        m=2*m+n-2*(n/2)
        n=n/2
    return m

palindromes=[]
for i in range(1000000):
    if reverse10(i)==i:
        if reverse2(i)==i: palindromes.append(i)
print palindromes
print sum(palindromes)
