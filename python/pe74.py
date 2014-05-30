from math import factorial

def dig_fac_sum(n):
    return sum(factorial(int(dig)) for dig in list(str(n)))

def length_to_repeat(n):
    if n in repeatsdict.keys(): return repeatsdict[n]
    repeats=length_to_repeat(dig_fac_sum(n))+1
    repeatsdict[n]=repeats
    return repeats

repeatsdict={169:3, 363601:3, 1454:3, 871:2, 45361:2, 872:2, 45362:2, 1:1, 2:1, 145:1, 40585:1}

def falling_generator(d,n): # a falling number is one where the digits are in descending order. falling_generator generates all d-digit falling numbers with first digit at most n in ascending order.
    if d>0:
        for dig in xrange(1,n+1):
            yield dig*10**(d-1)
            for rest in falling_generator(d-1,dig):
                yield dig*10**(d-1)+rest

candidates=[]
for d in xrange(1,7):
    for n in falling_generator(d,9):
        if length_to_repeat(n)==60:
            candidates.append(n)
print candidates
print factorial(4)+factorial(4)-factorial(3)+factorial(6)/2
