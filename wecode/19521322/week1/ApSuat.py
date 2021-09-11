from decimal import *
n = float(input())

result = (0.453592*n)/(2.54**2)
getcontext().prec = 6
print(Decimal(result).normalize())
