def gcd(n,m): #returns the greatest common denominator of n and m, using Euclidean algorithm
    if n*m==0: return n+m
    return gcd(m % n, n)

def lcm(n,m): return n*m/gcd(n,m)

j=1
for i in range(1,21): j=lcm(i,j)
print j
