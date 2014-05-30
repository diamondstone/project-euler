def digitsum(n):
    digits=map(int,list(str(n)))
    return sum(digits)

maxsum=0
for a in range(1,101):
    for b in range(1,101):
        s=digitsum(a**b)
        if s>maxsum: maxsum=s
print maxsum
