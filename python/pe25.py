i=0
j=1
k=1
s=2
while len(str(k))<1000:
    i=j
    j=k
    k=i+j
    s+=1
print s
