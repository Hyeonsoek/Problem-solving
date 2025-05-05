import sys
from decimal import Decimal, getcontext
input = sys.stdin.readline
getcontext().prec = 30

def solve():
    T = int(input())
    
    values = [Decimal('8' * i) for i in range(1, 19)]
    
    for _ in range(T):
        n = Decimal(input())
        count = 8
        for i in reversed(values):
            while count > 0 and n >= i:
                count -= 1
                n -= i
        
        if n == 0 and count >= 0:
            print("Yes")
        else:
            print("No")

solve()