from decimal import *
context = getcontext()
context.prec = 100
context.rounding = ROUND_HALF_UP
pi = Decimal('3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282')

def sin(x : Decimal):
    x = x % (2 * pi)
    i, lasts, s, fact, num, sign = Decimal('1'), Decimal('0'), x, Decimal('1'), x, Decimal('1')
    while s != lasts:
        lasts = s
        i += 2
        fact *= i * (i-1)
        num *= x * x
        sign *= -1
        s += num / fact * sign
    return +s

def solve():
    a, b, c = map(Decimal, input().split())
    
    def func(x : Decimal):
        return (a * x) + (b * sin(x))
    
    low = Decimal('0')
    high = Decimal('100000')
    for _ in range(10000):
        mid = (low + high) * Decimal('0.5')
        k = func(mid)
        
        if k == c:
            return round(mid, 6)
        
        if k < c:
            low = mid
        else:
            high = mid
    
    return round(low, 6)

print(solve())