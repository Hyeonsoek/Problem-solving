import sys, decimal
from typing import List, Sequence
input = sys.stdin.readline

def multiply(a : Sequence[int], b : Sequence[int], digit : int = 0) -> List[int]:
    decimal.setcontext(
        decimal.Context(prec=decimal.MAX_PREC, Emax=decimal.MAX_EMAX)
    )
    if digit == 0:
        digit = min(20, len(str(min(len(a), len(b)) * max(a) * max(b))))
    
    f = f'0{digit}d'
    a_dec = decimal.Decimal(''.join(format(x, f) for x in a))
    b_dec = decimal.Decimal(''.join(format(x, f) for x in b))
    c_dec = a_dec * b_dec
    total_digit = digit * (len(a) + len(b) - 1)
    c = format(c_dec, f'0{total_digit}f')
    return [int(c[i:i+digit]) for i in range(0, total_digit, digit)]

def solve():
    n, m = map(int, input().split())
    a = [*map(int, input().split())]
    b = [*map(int, input().split())]
    
    c = multiply(a, b)
    
    result = c[0]
    for i in c[1:]:
        result ^= i
    print(result)
    
solve()