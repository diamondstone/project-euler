i=0.0
j=1.0
k=1.0
s=0
while i<4000000:
    i=j
    j=k
    k=i+j
    if i/2 == int(i/2):
        s=s+i
print s
