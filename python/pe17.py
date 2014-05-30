def numbertowords(n): #works for numbers <1000, avoids spaces but can easily be rewritten to include them
    digits=['','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    tens=['','','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
    if n<20: return digits[n]
    if n<100: return tens[n/10]+digits[n % 10]
    if n%100==0: return digits[n/100]+'hundred'
    else: return digits[n/100]+'hundredand'+numbertowords(n%100)

print sum(len(numbertowords(i)) for i in range(1,1000))+3+8
