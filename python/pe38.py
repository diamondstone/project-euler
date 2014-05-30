def ispandigital(string): # checks whether the string is pandigital
    digits=map(int,string)
    digits.sort()
    return digits==[1,2,3,4,5,6,7,8,9]

pandigprods=[]
for i in range(1,9877):
    for j in range(2,9):
        string=reduce(lambda x,y:x+y,[str(i*(k+1)) for k in range(j)])
        if ispandigital(string): pandigprods.append(int(string))

pandigprods.sort()
print pandigprods
