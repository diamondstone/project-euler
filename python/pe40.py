numbers=''
for i in range(200000):
    numbers=numbers+str(i)
print reduce(lambda x,y:x*y,[int(numbers[10**n]) for n in range(7)])
