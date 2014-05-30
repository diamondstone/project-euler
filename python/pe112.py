import itertools

def isincr(n):
    while n>9:
        d1=n%10
        n=n/10
        d2=n%10
        if d2>d1: return False
    return True

def isdecr(n):
    while n>9:
        d1=n%10
        n=n/10
        d2=n%10
        if d2<d1: return False
    return True

def isbouncy(n):
    if isincr(n): return False
    if isdecr(n): return False
    return True

def main():
    numbouncy=0
    i=100
    while 100*numbouncy<99*i:
        i+=1
        if isbouncy(i): numbouncy+=1
    print i
       
main()
