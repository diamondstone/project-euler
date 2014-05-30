from math import log

file = open('pe99_base_exp.txt')
pairs=file.readlines() # list of lines of the form "x,y\n"
pairs=map(lambda x: x.strip('\n').split(','),pairs) # list of pairs x,y (strings representing ints)
logs=map(lambda x: log(int(x[0]))*int(x[1]),pairs) # list of log(x^y)
best=0
for j in range(1000):
    if logs[j]>logs[best]: best=j
print best+1 # add 1 to correct for line 1 being index 0.
