#By listing the set of reduced proper fractions for d < 1,000,001 in ascending order of size, find the numerator of the fraction immediately to the left of 3/7.

#That would be stupid. We want, to find the greatest fraction <3/7 with denominator <1,000,001, write it in lowest terms, and output the numerator.

#So, FOR each denominator d, we want to find the largest numerator n s.t. n/d<3/7 (i.e. n=3*d/7 using integer math, and subtracting 1 if d is divisible by 7), compare it to our existing best, and pick the highest. By picking the old one if they are the same, we guarantee that the found fraction will be in least terms.

bestn=0
bestd=1
for d in xrange(1,1000001):
    n=(3*d-1)/7
    if n*bestd>d*bestn:
        bestn=n
        bestd=d
print bestn
