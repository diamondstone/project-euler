from math import sqrt,factorial

def isprime(n): #returns 1 if n is prime, 0 if n is composite
    if n<2:
        return None
    if n<4:
        return 1
    t=int(sqrt(n))
    for i in range(2,t+1):
        if n % i == 0: return 0
    return 1

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

def permute(perm,digits): #returns the permutation perm of the 4-digit number digits
    digits=str(digits)
    while len(digits)<4:
        digits='0'+digits    
    newdigits=digits[perm[0]]+digits[perm[1]]+digits[perm[2]]+digits[perm[3]]
    return int(newdigits)

def primeperms(digits): #returns a list of all prime permutations of the 4-digit number digits
    listofperms=[]
    for i in range(24):
        perm=permute(numtoperm(i,4),digits)
        if perm not in listofperms:
            if isprime(perm):
                listofperms.append(perm)
    return listofperms

def arithmetic(digits): #returns a list of all length-3 arithmetic sequences of primes in digits
    l=primeperms(digits)
    sequences=[]
    for i in range(len(l)-2):
        for j in range(i+1,len(l)-1):
            for k in range(j+1,len(l)):
                if l[k]-l[j]==l[j]-l[i]:
                    sequences.append([l[i],l[j],l[k]])
    return sequences

d=range(10)
for i in d:
    for j in d[i:]:
        for k in d[j:]:
            for l in d[k:]:
                n=1000*l+100*k+10*j+i
                seqs=arithmetic(n)
                if seqs: print seqs
