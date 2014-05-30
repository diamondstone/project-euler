def int_sqrt(n): #returns the integer part of the square root of n; guaranteed to work on long ints.
    x = n
    while 1:
        y = (x + n/x)/2
        if y >= x:
            return x
        x = y

s=0
for n in xrange(2,100):
    if n in [4,9,16,25,36,49,64,81]: continue
    d=int_sqrt(n*10**200)
    s+=sum(int(dig) for dig in list(str(d))[:100])
print s
