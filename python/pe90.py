import itertools as it

def repn(i,j,n): #determines whether dice i and j can represent the 2-digit number n
    if 6 in i or 9 in i: i+=6,9
    if 6 in j or 9 in j: j+=6,9
    a=n%10
    b=n/10
    if a in i and b in j: return True
    if b in i and a in j: return True
    return False
    

def repsq(i,j): #determines whether dice i and j can represent all 1,2-digit squares
    for n in range(1,10):
        if not repn(i,j,n**2): return False
    return True

sum=0
for (i,j) in it.combinations_with_replacement(it.combinations(range(10),6),2): #itertools does all of the work of finding all pairs of labeled dice for us
    if repsq(i,j):
        sum+=1
print sum
