def unknown(val):
    f = [0]*(val+1)
    f[1]=1
    g = [0]*(val+1)
    q = [0]*(val+1)

    for n in xrange(1,val+1): q[n]=(1-pv)**n
    for n in xrange(2,val+1):
        kmin=umin=100000
        for i in xrange(1,n):
            qv = (q[n-i]-q[n])/(1-q[n])
            x = f[i]+g[n-i]
            gv = 1+x+qv*(g[i]-x)
            fv = f[i]+f[n-i]
            kmin=min(kmin,gv)
            umin=min(umin,fv)
        g[n]=kmin
        f[n]=umin=min(umin,1+(1-q[n])*kmin)
    return f[val]

N=10000

from time import time

total=0
start=time()
for i in xrange(1,50+1):
    pv=i/100.0
    lst=time()
    v=unknown(N)
    total+=v
    print "T(%s,%s) = %s\t%s"%(pv,N,v,time()-lst)
print "Total: %s\tTotal Time: %s"%(total,time()-start)
