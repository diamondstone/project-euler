file = open('pe79keylog.txt')
keys = set([int(line) for line in file])
file.close
keys = [key for key in keys]
keys.sort()
print keys
