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
def endred(n):
   return sum([endblack(k) for k in xrange(n-2)])

@memoize
def endblack(n):
   if n==0: return 1
   return total(n-1)

@memoize
def total(n):
   return endred(n)+endblack(n)

print total(50)
             
