from math import factorial

total=0
for p in range(1,22):
    count=0
    for n in range(1,10):
        if len(str(n**p))==p: count+=1
    print "there are",count,p,"digit",p,"th powers"
    total+=count
print total
