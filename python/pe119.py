def digitsum(n):
   sum=0
   while n:
      sum+=n%10
      n=n/10
   return sum

def isinteresting(n):
   p=2
   d=digitsum(n)
   if d==1: return 0
   while d**p<n:
      p+=1
   if d**p==n: return p
   return 0

def interestingexpe(n): #generates interesting numbers with exponent n
   i=2
   while i**n<10:
      i+=1
   while 10**i<i**(10*n):
      if i==digitsum(i**n): yield i**n
      i+=1

def interestingexpl(n): #generates interesting numbers with exponent < n
   for i in reduce(merge,[interestingexpe(m) for m in xrange(2,n)]):
      yield i

def merge(iterator1,iterator2): #assuming iterator1 and iterator2 are in increasing order, iterates through their union in increasing order
   try:
      i1=iterator1.next()#want to yield neither
      i2=iterator2.next()#want to yield i1
      while True:
         if i1<i2:
            last=i1
            yield last
            i1=iterator1.next()#want to yield i2
         if i1>i2:
            last=i2
            yield last
            i2=iterator2.next()#want to yield i1
         if i1==i2:
            last=i1
            yield last
            i1=iterator1.next()#want to yield neither
            i2=iterator2.next()#want to yield i1
   except StopIteration:
      if i1>last: yield i1
      if i2>last: yield i2
      for i in iterator1: yield i
      for i in iterator2: yield i

def test1():
   count=0
   i=10
   while count<30:
      if isinteresting(i):
         print i,isinteresting(i)
         count+=1
      i+=1

def main():
   count=0
   for i in interestingexpl(50):
      count+=1
      if count==30: break
   print i

main()
