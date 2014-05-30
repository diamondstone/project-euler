def dr(n,flag=0):
    count=0
    for i in xrange(1,n+1):
        p,q=i,i*n+n*n
        if q%p==0:
            if flag: print "1/{0}+1/{1}=1/{2}".format(n+i,q/p,n)
            count+=1
    return count

def main():
    n=100000
    while(dr(n)<=1000 and n<200000): n+=1
    print n

def test():
    for n in xrange(2,7): dr(n,1)

main()
