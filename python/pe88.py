## Given k, n=1*...*1*2*k = 1+...+1+2+k = 2k is a product sum number for k. ## Easy to see that n is a product sum number iff n is composite.
## So want to take all composite numbers<=12000 and rule out the ones which are not minimal product sum numbers.

def productsum(K): #returns a list of all minimal product-sum numbers where the arity is at most K. (We know these are all at most 2K.)
    arities=ps_arity(2*K+1)
    minimals=[]
    for k in xrange(2,K+1):
        for i in xrange(2*k+1):
            if k in arities[i]:
                minimals.append(i)
                break
    return minimals

###Better plan: given that n is a product-sum number for all k in K (including 1), q*n is a product-sum number for {nq-n-q+k+1 : k in K}, since we can write qn as the sum/product of q_1...q_k,q,1...1 with nq-n-q 1s. NEED TO SHOW ALL ARISE THIS WAY. This gives a dynamic approach to finding productsum(n) for all n<12000


def ps_arity(N): #returns a list of product-sum arities for numbers below N
    a=1,
    sievedata=[a]*N
    sievedata=map(list,sievedata)
    for n in xrange(2,N):
        for q in xrange(2,N/n):
            sievedata[n*q]+=map(lambda k: n*q-n-q+k+1, sievedata[n])
    sievedata=map(set,sievedata)
    return sievedata

minimals=set(productsum(12000))
sum=0
for i in minimals:
    sum+=i
print sum
