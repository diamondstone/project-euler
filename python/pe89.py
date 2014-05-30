def romnum(n): # returns a string given the efficient roman numeral for n
    numeral=''
    while n>0:
        if n>=1000:
            n-=1000
            numeral+='M'
        elif n>=900:
            n-=900
            numeral+='CM'
        elif n>=500:
            n-=500
            numeral+='D'
        elif n>=400:
            n-=400
            numeral+='CD'
        elif n>=100:
            n-=100
            numeral+='C'
        elif n>=90:
            n-=90
            numeral+='XC'
        elif n>=50:
            n-=50
            numeral+='L'
        elif n>=40:
            n-=40
            numeral+='XL'
        elif n>=10:
            n-=10
            numeral+='X'
        elif n>=9:
            n-=9
            numeral+='IX'
        elif n>=5:
            n-=5
            numeral+='V'
        elif n>=4:
            n-=4
            numeral+='IV'
        else:
            n-=1
            numeral+='I'
    return numeral

def numrom(numeral): # returns the number represented by the numeral
    n=0
    while numeral:
        if numeral[:1]=='M':
            n+=1000
            numeral=numeral[1:]
        elif numeral[:2]=='CM':
            n+=900
            numeral=numeral[2:]
        elif numeral[:1]=='D':
            n+=500
            numeral=numeral[1:]
        elif numeral[:2]=='CD':
            n+=400
            numeral=numeral[2:]
        elif numeral[:1]=='C':
            n+=100
            numeral=numeral[1:]
        elif numeral[:2]=='XC':
            n+=90
            numeral=numeral[2:]
        elif numeral[:1]=='L':
            n+=50
            numeral=numeral[1:]
        elif numeral[:2]=='XL':
            n+=40
            numeral=numeral[2:]
        elif numeral[:1]=='X':
            n+=10
            numeral=numeral[1:]
        elif numeral[:2]=='IX':
            n+=9
            numeral=numeral[2:]
        elif numeral[:1]=='V':
            n+=5
            numeral=numeral[1:]
        elif numeral[:2]=='IV':
            n+=4
            numeral=numeral[2:]
        else:
            n+=len(numeral)
            numeral=[]
    return n
    
file = open('pe89roman.txt')
numerals=[line.strip() for line in file]
newnums = map(romnum,map(numrom,numerals))
print sum(len(s) for s in numerals)-sum(len(s) for s in newnums)
