import sys, decimal
from typing import List, Sequence
MAX = 200001
input = sys.stdin.readline

def multiply(a: Sequence[int], b: Sequence[int], digit: int = 0) -> List[int]:
    """Returns the multiplication of two polynomials."""
    decimal.setcontext(
        decimal.Context(prec=decimal.MAX_PREC, Emax=decimal.MAX_EMAX))
    if digit == 0:
        digit = min(20, len(str(min(len(a), len(b)) * max(a) * max(b))))
    f = f'0{digit}d'
    a_dec = decimal.Decimal(''.join(format(x, f) for x in a))
    b_dec = decimal.Decimal(''.join(format(x, f) for x in b))
    c_dec = a_dec * b_dec
    total_digit = digit * (len(a) + len(b) - 1)
    c = format(c_dec, f'0{total_digit}f')
    return [int(c[i:i + digit]) for i in range(0, total_digit, digit)]

def solve():
    n = int(input())
    arr = [0] * MAX
    arr[0] = 1
    
    for i in range(n):
        arr[int(input())] += 1

    X = multiply(arr, arr)
    
    count = 0
    m = int(input())
    for i in range(m):
        if X[int(input())].real > 0:
            count += 1
    
    print(count)

solve()