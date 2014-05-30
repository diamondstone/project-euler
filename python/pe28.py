list=[1]
for n in range(1,501):
    for i in range(4):
        list.append(list[-1]+2*n)
print sum(list)
