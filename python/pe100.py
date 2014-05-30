# Project Euler 100: Find the least n > 1 trillion such that, for some m, we have n(n-1)=2m(m-1)

# If n(n-1)=2m(m-1), then (n-1)^2+n^2 = 2n(n-1)+1=4m(m-1)+1=4m^2-4m+1=(2m-1)^2, and hence (n-1,n,2m-1) is a pythagorean triple.

# Conversely, if (n-1,n,k) is a pythagorean triple, then k is odd, so k=2m-1 for some m, whence the same identity gives n(n-1)=2m(m-1).

# So we are searching for the first almost-isosceles pythagorean triple with a > 1 trillion

# By http://ajc.maths.uq.edu.au/pdf/11/ajc-v11-p263.pdf, all AIPT triples are of the form (x-1,x,a), where (2x-1)^2=2a^2-1, and a is of the form a_n for some solution to the recurrence

# a_0 = 1; a_n = 2b_{n-1}+a_{n-1}
# b_0 = 2; b_n = 2a_n + b_{n-1}

a=1
b=2
while a<707000000000: # approx 1 trillion sqrt(2)
    a=2*b+a
    b=2*a+b
y=int(a*(2.0**0.5))
while y**2<2*a**2-1:
    y+=1
while y**2>2*a**2-1:
    y-=1
x=(y+1)/2
print x,"total discs"
y=int(x/(2.0**0.5))
while 2*y*(y-1)<x*(x-1):
    y+=1
while 2*y*(y-1)>x*(x-1):
    y-=1
print y,"blue discs"

# From the forum, there is a nicer recurrence which gives disk numbers directly, rather than by way of almost-isosceles triple hypotenuses. There's (unsurprisingly) a connection with the continued fraction for sqrt(2).
