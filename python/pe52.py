notfound=1
i=0
while notfound:
    i+=1
    notfound=0
    d=list(str(i))
    d.sort()
    for j in range(2,7):
        dd=list(str(i*j))
        dd.sort()
        if d!=dd: notfound=1
print i
