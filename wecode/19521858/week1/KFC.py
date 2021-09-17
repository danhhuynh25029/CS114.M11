F = float(input())
from decimal import*
getcontext().prec=6
C = (float)((F-32)/1.8)
K = C + 273.15
print(Decimal(C).normalize(),Decimal(K).normalize())