bestd=0
maxlength=0
for d in range(1,1000):
    remainders=[1]
    while remainders[-1] not in remainders[:-1]: #implements division algorithm, storing remainders in a list, until a repeated remainder is found
        remainders.append(10*remainders[-1] % d)
    repeatlength=len(remainders)-remainders.index(remainders[-1])-1
    if repeatlength>maxlength:
        bestd=d
        maxlength=repeatlength
print bestd


