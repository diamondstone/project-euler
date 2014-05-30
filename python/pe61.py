tri = [n*(n+1)/2 for n in range(45,141)]
squ = [n*n for n in range(32,100)]
pent = [n*(3*n-1)/2 for n in range(26,82)]
hexa = [n*(2*n-1) for n in range(23,71)]
hept = [n*(5*n-3)/2 for n in range(21,64)]
octa = [n*(3*n-2) for n in range(19,59)]
figurate = set(tri+squ+pent+hexa+hept+octa)
tri=set(tri)
squ=set(squ)
pent=set(pent)
hexa=set(hexa)
hept=set(hept)
octa=set(octa)
digits = [str(i) for i in range(10)]
affixes = [a+b for a in digits if a!='0' for b in digits]
candidates=[[a] for a in affixes]
l=1
while l<6:
    p=candidates.pop(0) #using list as a queue. May be inefficient; if so, rewrite with alternate queue data type.
    if len(p)>l:
        l=len(p)
        if len(p)==6:
            candidates.append(p)
            break
    last=p[-1]
    for a in affixes:
        if int(last+a) in figurate: candidates.append(p+[a])
print len(candidates),"candidates remaining"

newcandidates=[]
for a in candidates:
    if int(a[5]+a[0]) in figurate: newcandidates.append(a)
candidates=[]
for a in newcandidates:
    b=[]
    for i in range(6):
        b.append(int(a[i]+a[(i+1)%6]))
    candidates.append(b)
print len(candidates),"candidates remaining"

newcandidates=[]
for a in candidates:
    b=set(a)
    if a[0] not in squ: continue
    if b.isdisjoint(tri): continue
    if b.isdisjoint(pent): continue
    if b.isdisjoint(hexa): continue
    if b.isdisjoint(hept): continue
    if b.isdisjoint(octa): continue    
    newcandidates.append(a)
candidates=newcandidates
print len(candidates),"candidates remaining"

for a in candidates:
    mask=[]
    for b in a:
        c=''
        if b in tri: c=c+'3'
        if b in squ: c=c+'4'
        if b in pent: c=c+'5'
        if b in hexa: c=c+'6'
        if b in hept: c=c+'7'
        if b in octa: c=c+'8'
        mask.append(c)
    if len(set(mask))==6: print a,sum(a)
    
