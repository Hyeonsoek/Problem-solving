from math import factorial

def solve():
    n = int(input())

    if not n:
        return "NO"
        
    for xx in reversed([ factorial(x) for x in range(21) ]):
        if xx <= n:
            n -= xx
            
    return "NO" if n else "YES"

print(solve())