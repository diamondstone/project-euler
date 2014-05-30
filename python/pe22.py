def stringvalue(letters):
    letters=letters.lower()
    value=sum(map(lambda x: ord(x)-ord('a')+1,letters))
    return value

file = open('pe22names.txt')

names=file.readline().strip('"').split('","')
names.sort()
values=map(stringvalue,names)
total=0
for i in range(len(values)):
    total+=values[i]*(i+1)
print total
