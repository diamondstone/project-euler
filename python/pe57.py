a=1
b=1
count=0
for i in range(1000):
    c=a+2*b
    b=a+b
    a=c
    if len(str(a))>len(str(b)): count+=1
print count
