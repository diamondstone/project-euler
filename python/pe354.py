## Python script for Project Euler problem 354

## Problem description:
## Consider a honey bee's honeycomb where each cell is a perfect regular hexagon with side length 1. One particular cell is occupied by the queen bee. For a positive real number L, let B(L) count the cells with distance L from the queen bee cell (all distances are measured from centre to centre); you may assume that the honeycomb is large enough to accommodate for any distance we wish to consider. 

## For example, B(3) = 6, B(21) = 12 and B(111 111 111) = 54.

## Find the number of L  5*10^11 such that B(L) = 450.

## Note: There are 12 symmetries of the honeycomb. Each cell not on one of the six major axes has 12 symmetric copies, whereas those on the axes have 6. 450 is a multiple of 12 but not 6, so if B(L)=450, then L contains a point on one of the 12 major axes, and hence is an integer multiple of either sqrt(3) or 3.

from math import sqrt,ceil

def countpairs(L): #counts the number of pairs (x,y) with x=y (mod 2) that satisfy (9x^2+3y^2)=12L. This is equivalent to computing B(sqrt(3L)), since points at distance d are in one to one correspondence with pairs (x,y) with x=y (mod 2) such that 9x^2+3y^2=4d^2. Note that if (x,y) is such a pair, then so are (pmx,pmy), (pm(x-y)/2,pm(3x+y)/2), and (pm(x+y)/2,pm(3x-y)/2). This gives 12 pairs (x,y) arising from each pair (x,y) with 0<y<x, and 6 pairs arising from each pair with x>0 and y=0 or y=x. So it suffices to count the number of pairs (x,y) with x=y (mod 2), (9x^2+3y^2)=L, and 0<y<x, multiply by 12, and then add 6 if L/9 or L/12 is a perfect square. Furthermore, assuming 9x^2+3y^2=L, then 0<y<x iff sqrt(L/12)<x<sqrt(L/9)
    num=0
    Lower=int(ceil(sqrt(L))) #first we compute lower and upper bounds on the values of x to check
    Upper=int(sqrt((L*4)/3))
    if Lower**2==L:
        num+=1
        Lower+=1
    if 3*Upper**2==4*L:
        if Upper%2==0: num+=1
        Upper-=1
    for x in range(Lower,Upper+1):
        y=int(sqrt(4*L-3*x**2))
        if x%2==y%2:
            if 3*x**2+y**2==4*L:
                num+=2
    return num*6

for i in range (1,101):
    print 21*i,': ',countpairs(3*(7*i)**2)
    
## If x=y (mod 2), then x^2=y^2 (mod 4), and hence 9x^2+3y^2=0 (mod 12). Hence countpairs(L)=0 if L is not a multiple of 12.

## Problem: with current plan, we need to run computeB(L) for almost 5*10^11 values of L. So it needs to run a LOT faster, or a new plan is needed. Also, this needs to be compiled rather than scripted.
