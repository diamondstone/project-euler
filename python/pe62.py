def stringsort(s): #puts string s into sorted order
    t=list(s)
    t.sort()
    s=reduce(lambda x,y:x+y,t)
    return s

cubes = [str(n**3) for n in range(10000)]
cubedigits = map(stringsort,cubes)
sortdigits = cubedigits[:]
sortdigits.sort()
plicity=1
gooddigits=[]
for i in range(9999):
    if sortdigits[i+1]==sortdigits[i]: plicity+=1
    else:
        if plicity==5: gooddigits.append(sortdigits[i])
        plicity=1
for d in gooddigits:
    for i in range(10000):
        if cubedigits[i]==d:
            print cubes[i]
            break
