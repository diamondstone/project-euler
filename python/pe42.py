from math import sqrt

def stringvalue(letters):
    letters=letters.lower()
    value=sum(map(lambda x: ord(x)-ord('a')+1,letters))
    return value

def triangle(letters):
    letters=letters.lower()
    value=sum(map(lambda x: ord(x)-ord('a')+1,letters))
    n=int(sqrt(2*value))
    if n*(n+1)==2*value: return 1
    return 0

file = open('pe42words.txt')

words=file.readline().strip('"').split('","')
trianglewords=[]
for word in words:
    if triangle(word):
        trianglewords.append(word)
print len(trianglewords)
