from decimal import *
getcontext().prec = 6*10**5 + 10
a,b=map(Decimal,input().split())
print(a*b)