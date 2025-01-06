# from decimal import *
# import sys
# context = getcontext()
# context.prec = 50
# context.rounding = ROUND_HALF_UP
# input = sys.stdin.readline

# LOW = Decimal('-1000000')
# HIGH = Decimal('1000000')
# MAGIN = Decimal('1e-20')
# ROUND = 20

# def solve():
#     a, b, c, d = map(Decimal, input().split())
    
#     def FX(x : Decimal):
#         return a * x * x * x + b * x * x + c * x + d

#     LowFX = FX(LOW)
#     HighFX = FX(HIGH)

#     def bsearch(low : Decimal, high : Decimal):
#         FXlow = FX(low)
#         while high - low > MAGIN:
#             mid = (low + high) * Decimal('0.5')
#             FXMid = FX(mid)
            
#             if FXMid * FXlow > 0:
#                 low = mid
#             else:
#                 high = mid

#         result = round(low, ROUND)
#         if result <= MAGIN:
#             return Decimal('0')

#         return Decimal(f'{result:.15f}')

#     D =  b * b - 3 * a * c
#     if D < 0:
#         print(f'{bsearch(LOW, HIGH):.15f}')
#         return

#     XMid = -b / (3 * a)

#     if D == 0:
#         if round(LowFX * FX(XMid), ROUND) <= 0:
#             print(f'{bsearch(LOW, XMid):.15f}')
#         else:
#             print(f'{bsearch(XMid, HIGH):.15f}')
#         return 

#     result = []

#     D = D ** Decimal('0.5') / (3 * a)
#     XLow = XMid - D
#     XHigh = XMid + D

#     if XLow > XHigh:
#         XLow, XHigh = XHigh, XLow

#     FXLow = FX(XLow)
#     FXHigh = FX(XHigh)
#     K = round(FXLow * FXHigh, ROUND)

#     low = lambda : bsearch(LOW, XLow)
#     mid = lambda : bsearch(XLow, XHigh)
#     high = lambda : bsearch(XHigh, HIGH)

#     result = []
    
#     if K < 0:
#         result.extend([low(), mid(), high()])
#     elif K == 0 or 0 <= round(FXLow, ROUND) <= MAGIN or 0 <= round(FXHigh, ROUND) <= MAGIN:
#         if 0 <= round(FXLow, ROUND) <= MAGIN:
#             result.extend([XLow, high()])
#         else:
#             result.extend([low(), XHigh])
#     else:
#         result.append(bsearch(LOW, HIGH))

#     result.sort()
#     print(*result)

# for _ in range(int(input())):
#     solve()

# TRASH GARBAGE