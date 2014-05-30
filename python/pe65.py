import itertools

def cfracterms(): #generator for terms in the continued fraction of e
    yield 2
    for n in itertools.count(2):
        if n%3: yield 1
        else: yield 2*n/3

l=100
terms=list(itertools.islice(cfracterms(), l))
d=terms.pop()
n=1
while terms:
    dd=d
    d=n+d*terms.pop()
    n=dd
print "the {0}th continued fraction expansion for e is\n{1}\n/\n{2}".format(l,d,n)
print "e ~ {0:.20}".format(1.0*d/n)
print "the sum of digits in the numerator is",sum(int(k) for k in str(d))
