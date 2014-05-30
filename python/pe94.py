## Heron's formula says that for a triangle with sides a,b,c and semiperimeter s, the area A satisfies A^2=s(s-a)(s-b)(s-c)
## So the almost equilateral triangle must have two odd sides and one even side, 2a-1,2a-1,2a or 2a+1,2a+1,2a, making the perimeter 6a+-2, and the semiperimeter 3a+-1, so that A^2=(3a+1)(a+1)a^2 or A^2=(3a-1)(a-1)a^2.
## This problem is then a matter of counting values of a with 6a+2<=1000000000 and (3a+1)(a+1) a perfect square, plus values of a with 6a-2<=1000000000 and (3a-1)(a-1) a perfect square. Equivalently, we're counting as less than 166666667 (the off-by-one in case 1 doesn't matter because that doesn't give integer area)

sum=-4 #since a=1 gives false positive to (1,1,2) "triangle"
for a in range(1,166666668):
    A=(3*a+1)*(a+1)
    if int(A**.5)**2==A: sum+=6*a+2
    A=(3*a-1)*(a-1)
    if int(A**.5)**2==A: sum+=6*a-2
print sum
