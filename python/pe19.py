# store dates as lists of length 3: day, month, (4 digit) year

def days(date): #finds the number of days date is after january 1, 1900
    correction=[-1,0,-2,-1,-1,0,0,1,2,2,3,3] # finds appropriate correction factor for the number of days, based on month, assuming 28-day february
    numleapdays = (date[2]-1900)/4-(date[2]-1900)/100+(date[2]-1600)/400 #rounding may screw this up if negative
    leapyear = 0 # 1 if leapyear (year is divisible by 400, or by 4 but not 100), 0 if not
    if (date[2] % 4 == 0)*(date[2]%100): leapyear = 1
    if date[2] % 400 == 0: leapyear = 1
    if date[1]<3: numleapdays = numleapdays-leapyear
    days = date[0]+30*(date[1]-1)+correction[date[1]-1]+(date[2]-1900)*365+numleapdays
    return days

daynames=['monday','tuesday','wednesday','thursday','friday','saturday','sunday'] #not needed in current version, sunday = 6

numsundays=0
for y in range(1901,2001):
    for m in range(1,13):
        if days([1,m,y])%7==6: numsundays=numsundays+1
print numsundays

