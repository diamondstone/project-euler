i=0.0
j=0.0
while i<1000:
    if i/3 == int(i/3):
        j=j+i
    else:
        if i/5 == int(i/5):
             j=j+i
    i=i+1
print j
