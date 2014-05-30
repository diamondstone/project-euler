import itertools 

def singit():
    for n in xrange(1,21):
        yield n
    yield 25

def dubit():
    for n in xrange(1,21):
        yield 2*n
    yield 50

def tripit():
    for n in xrange(1,21):
        yield 3*n

def allit():
    for n in singit():
        yield n
    for n in dubit():
        yield n
    for n in tripit():
        yield n

def checkoutways(N):
    count=0
    for n in dubit():
        if n<N:
            count+=1
        for i in allit():
            if n+i<N:
                count+=1
        for (i,j) in itertools.combinations_with_replacement(allit(),2):
            if n+i+j<N:
                count+=1
    return count

print checkoutways(100)
