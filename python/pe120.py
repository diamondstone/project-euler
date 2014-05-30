def remainders1(a):
   maximum=0
   for n in range(1,a*2+10,2):
      maximum=max(maximum, (((a+1)**n+(a-1)**n)%(a**2)))
   return maximum

def remainders2(a):
   return a*(a-1-((a-1)%2))

total=0
for a in range(3,1001):
#   if remainders1(a)!=remainders2(a):
#      print a,remainders1(a),remainders2(a)
   total+=remainders2(a)
print total
