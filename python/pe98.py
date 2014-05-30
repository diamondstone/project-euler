import itertools as it

def removeduplicates(list1): #takes as input a sorted list, returns a new list consisting of the old list with repetitions removed
    if list1==[]: return []
    list2=[]
    old=list1[0]
    list2.append(old)
    for i in range(1,len(list1)):
        if list1[i]!=old:
            old=list1[i]
            list2.append(old)
    return list2

def anagram(p,q): #determines whether the words p and q are anagrams
    p=list(p)
    p.sort()
    q=list(q)
    q.sort()
    if p==q: return True
    return False

def test(long): #prints length long words, finds all anagram pairs
    longwords=[]
    found=False
    for w in words:
        if len(w)==long:
            longwords.append(w)
   # print longwords
    for i in range(len(longwords)):
        for j in range(i+1,len(longwords)):
            if anagram(longwords[i],longwords[j]):
                found = found or sawp(longwords[i],longwords[j])
    return found

def isquare(n):
    if int(n**.5)**2==n:
        return True
    else:
        return False

def sawp(p,q): #determines whether p and q are a square anagram word pair
    p=list(p)
    q=list(q)
    let=p[:]
    let.sort()
    let=removeduplicates(let)
    l=len(let)
    for k in it.permutations(range(10),l):
        letmap={}
        for i in range(l):
            letmap[let[i]]=k[i]
        if letmap[p[0]]==0 or letmap[q[0]]==0: continue
        n1=reduce(lambda a,b:10*a+b, map(lambda x:letmap[x],p))
        n2=reduce(lambda a,b:10*a+b, map(lambda x:letmap[x],q))
        if isquare(n1) and isquare(n2):
            print max(n1,n2)
            return True
    return False

file = open('pe98words.txt')
words=file.readline().strip('"').split('","') #all words are between 1 and 14 characters
for l in range(14,1,-1):
    if test(l): break
