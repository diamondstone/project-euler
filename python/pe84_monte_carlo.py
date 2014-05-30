import random

def chance(n): # moves player on square n using chance card algorithm
    x=random.randrange(16)
    if x==0:
        return 0
    elif x==1:
        return 10
    elif x==2:
        return 11
    elif x==3:
        return 24
    elif x==4:
        return 39
    elif x==5:
        return 5
    elif x<=7:
        return n+10-((n+5)%10)
    elif x==8:
        if 12<=n and n<28:
            return 28
        else:
            return 12
    elif x==9:
        return (n-3)
    else:
        return n
    
def chest(n): # moves player on square n using community chest card algorithm
    x=random.randrange(16)
    if x==0:
        return 0
    elif x==1:
        return 10
    else:
        return n

def move(n,d): # moves player on square n using the normal algorithm (after d consecutive doubles); also returns number of consecutive doubles.
    x=random.randrange(sides)+1
    y=random.randrange(sides)+1
    roll=x+y
    if x==y:
        d+=1
        if d==3: return (10,0)
    else:
        d=0
    n+=roll
    if n in (2,17,33): # community chest squares
        n=chest(n)
        return (n%40,d)
    if n in (7,22,36): # chance squares
        n=chance(n)
        return (n%40,d)
    if n==30:
        return (10,d)
    else:
        return (n%40,d)

def maximums(listobject,n): # returns n tuples giving (index,data) for maximum values of data in list.
    # runs in O(len(listobject)*n) time, so slower than efficient sorting algorithms if n gets large.
    l=len(listobject)
    listobject.append(0) #value 0 should be less than top n values.
    best=[l]*n
    for i in range(l):
        for j in range(n):
            if listobject[i]>listobject[best[j]]:
                best.insert(j,i)
                best.pop()
                break
    best=map(lambda x:(x,listobject[x]),best)
    listobject.pop()
    return best

    
random.seed()
sides=4
trials=10000000
n=0
d=0
visits=[0]*40
for i in range(trials):
    (n,d)=move(n,d)
    visits[n]+=1
best=maximums(visits,3)
best=map(lambda (x,y):(x,y*100.0/trials),best)
print best
