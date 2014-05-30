from math import factorial

def choose(p,n):
    return factorial(p)/factorial(n)/factorial(p-n)

def catalan(n): #returns the nth catalan number
    return choose(2*n,n)/(n+1)

def doublechoose(p,n): #returns number of ways to choose two subsets, both of size n, from a set of size p
    return factorial(p)/factorial(n)**2/factorial(p-2*n)/2

def badchoices(p,n): #returns number of ways to choose two size n subsets of a size p set where one has a provably smaller sum than the other
    return choose(p,2*n)*catalan(n)

def goodchoices(p,n):
    return doublechoose(p,n)-badchoices(p,n)

def totalchoices(p):
    total=0
    for n in xrange(1,p/2+1):
        total+=doublechoose(p,n)
    return total

def totalgoodchoices(p):
    total=0
    for n in xrange(1,p/2+1):
        total+=goodchoices(p,n)
    return total

def message(p):
    print "Out of the {0} possible subset pairs that can be obtained from a set for which n = {1}, only {2} need to be tested for equality.".format(totalchoices(p),p,totalgoodchoices(p))

def main():
    message(4)
    message(7)
    message(12)

main()
