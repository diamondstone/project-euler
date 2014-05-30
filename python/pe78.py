# What is the least number which can be written in k*1 million ways as a sum of positive integers? (order doesn't matter)

import itertools

P={0:1}
for n in itertools.count(1): #itertools.count(0):
    s=0
    for k in xrange(1,int(n**0.5)+1):
        i=n-k*(3*k-1)/2
        j=n-k*(3*k+1)/2
        if i >= 0: s+=(-1)**(k+1)*P[i]
        if j >= 0: s+=(-1)**(k+1)*P[j]
    P[n]=s%1000000
    if s%1000000==0:
        print n
        break
