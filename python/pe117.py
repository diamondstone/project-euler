def RGB(n):
   L=[0,0,0,1]
   while n:
       n-=1
       L=[L[1],L[2],L[3],L[0]+L[1]+L[2]+L[3]]
   return L[3]

print RGB(5)
print RGB(50)
