def dig_sq_sum(n):
    return sum(int(dig)**2 for dig in list(str(n)))

def terminator(n):
    if n==1 or n==89: return n
    return terminator(dig_sq_sum(n))

count=0
for d in xrange(1,10**7+1):
    if terminator(d)==89: count+=1
print count
