def R(n):
   L=[1,1]
   while n:
       n-=1
       L=[L[1],L[0]+L[1]]
   return L[0]-1

def G(n):
   L=[1,1,1]
   while n:
       n-=1
       L=[L[1],L[2],L[0]+L[2]]
   return L[0]-1

def B(n):
   L=[1,1,1,1]
   while n:
       n-=1
       L=[L[1],L[2],L[3],L[0]+L[3]]
   return L[0]-1

def RGB(n):
    return R(n)+G(n)+B(n)

print R(5)
print G(5)
print B(5)
print RGB(5)
print RGB(50)
