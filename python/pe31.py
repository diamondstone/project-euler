ways=0
u=201
for i in range(0,u,200):
    u=201-i
    for j in range(0,u,100):
        u=201-j
        for k in range(0,u,50):
            u=201-i-j-k
            for l in range(0,u,20):
                u=201-i-j-k-l
                for m in range(0,u,10):
                    u=201-i-j-k-l-m
                    for n in range(0,u,5):
                        u=201-i-j-k-l-m-n
                        for p in range(0,u,2):
                            ways+=1
print ways
