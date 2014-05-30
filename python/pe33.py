for i in range(10):
    for j in range(10):
        if i!=j:
            for k in range(1,10):
                if i*(10*j+k)==k*(10*i+j): print str(i)+'/'+str(k)+'='+str(i)+str(j)+'/'+str(j)+str(k)
