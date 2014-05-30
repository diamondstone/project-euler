# How many ways can 100 be written as a sum of positive integers? (order doesn't matter)

sum_ways={}
for n in xrange(100+1):
    for k in xrange(n+1):
        if n==0: sum_ways[(n,k)]=1
        elif k==1: sum_ways[(n,k)]=1
        else: sum_ways[(n,k)]=sum(sum_ways[(n-i,min(i,n-i))] for i in xrange(1,k+1))


print sum_ways[5,5]-1
print sum_ways[100,100]-1
