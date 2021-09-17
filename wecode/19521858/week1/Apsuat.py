psi = float(input())
from decimal import*
getcontext().prec=6
print(Decimal(psi*0.453592/2.54/2.54).normalize())

