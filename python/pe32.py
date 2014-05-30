def ispandigital(i,j,k): # checks whether the numbers i,j,k between them have all nine digits exactly once
    digits=map(int,str(i)+str(j)+str(k))
    digits.sort()
    return digits==[1,2,3,4,5,6,7,8,9]

pandigprods=[]
for i in range(1,9):
    for j in range(1234,9876):
        if ispandigital(i,j,i*j): pandigprods.append(i*j)
for i in range(12,98):
    for j in range(123,987):
        if ispandigital(i,j,i*j): pandigprods.append(i*j)

print pandigprods
print set(pandigprods)
print sum(set(pandigprods))

