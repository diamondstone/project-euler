from math import factorial

print sum(n for n in range(11,2540160) if sum(factorial(int(digit)) for digit in str(n))==n)
