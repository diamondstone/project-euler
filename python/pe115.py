def memoize(fn):
   memo={}
   def memoized_fn(*args):
      if args in memo:
         return memo[args]
      else:
         ret=memo[args]=fn(*args)
         return ret
   return memoized_fn

@memoize
def endred(m,n):
   return sum([endblack(m,k) for k in xrange(n-m+1)])

@memoize
def endblack(m,n):
   if n==0: return 1
   return total(m,n-1)

@memoize
def total(m,n):
   return endred(m,n)+endblack(m,n)

def least(m,N):
   n=1
   while total(m,n)<N:
      n*=2
   #now binary search beween n/2 and n
   L=n/2
   H=n
   while H-L>1:
      M=(H+L)/2
      if total(m,M)<N:
         L=M
      else:
         H=M
   return H #in retrospect, could have just incremented without binary searching.   
   
def test():
   print total(3,29)
   print total(3,30)
   print least(3,1000000)
   print least(10,1000000)

def main():
   print least(50,1000000)

main()
             
