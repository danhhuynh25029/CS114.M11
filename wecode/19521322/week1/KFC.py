from decimal import *
f = float(input())
getcontext().prec = 6
c = Decimal((f-32)/1.8000).normalize()
k = Decimal((f-32)/1.8000 + 273.15).normalize()

print(f"{c} {k}")
