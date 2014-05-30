from math import factorial

def baseftonum(basef): #computes the number with "base" factorial representation basef
    num=0
    l=len(basef)
    for i in range(l): num+=factorial(l-i)*basef[i]
    return num
    

def numtobasef(num,l): # computes the l-"digit" "base" factorial representation of num
    # there's probably a real name for this
    basef=[0]*l
    for i in range(l):
        basef[i]=num/factorial(l-i)
        num-=basef[i]*factorial(l-i)
    return basef

def baseftoperm(basef): # converts a base-factorial representation to the corresponding permutation
    basef.append(0)
    l=len(basef)
    perm=[0]*l
    for i in range(l):
        while perm[i] in perm[:i]: perm[i] += 1
        for j in range(basef[i]):
            perm[i]+=1
            while perm[i] in perm[:i]: perm[i] += 1
    return perm

def permtobasef(perm): # converts a base-factorial representation to the corresponding permutation
    l=len(perm)-1
    basef=perm[:l]
    for i in range(l):
        for j in range(basef[i]):
            if j in perm[:i]: basef[i] -= 1
    return basef

def permtonum(perm): return baseftonum(permtobasef(perm))

def numtoperm(num,l): return baseftoperm(numtobasef(num,l-1))

def nextperm(perm):
    l=len(perm)
    num=permtonum(perm)+1
    if num==factorial(l): return None
    return numtoperm(num,l)

perm=numtoperm(999999,10)
print perm
perm=reduce(lambda x,y:x+y,map(str,perm))
print perm
