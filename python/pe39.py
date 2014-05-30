def triples(p): # calculates the number of pythagorean triples with sum p
    n=0
    for a in range(p/3):
        for b in range(a,p/2):
            if a**2+b**2==(p-a-b)**2: n+=1
    return n

max=1
bestp=12
for p in range(13,1001):
    t=triples(p)
    if t>max:
        max=t
        bestp=p
        
print bestp
