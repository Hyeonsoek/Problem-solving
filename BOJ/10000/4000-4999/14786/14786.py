import math
ERROR = 10 ** -9

def solve():
    a, b, c = map(int, input().split())

    low = 0
    high = 100000
    for _ in range(50000):
        mid = (high + low) / 2
        k = a * mid + b * math.sin(mid)
        
        if abs(k - c) < ERROR:
            return mid
        
        if k < c:
            low = mid
        else:
            high = mid
    
    return low

print(solve())