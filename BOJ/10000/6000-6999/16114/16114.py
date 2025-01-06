from math import ceil

def solve():
    x, n = map(int, input().split())
    
    if n >= 3 and n & 1:
        return 'ERROR'
    
    if x == 0:
        return 0
    
    if x < 0:
        if n == 1:
            return 'INFINITE'
        else:
            return 0
    
    if n == 0:
        return 'INFINITE'
    
    if n == 1:
        return 0
    
    return ceil((x - (n // 2)) / (n // 2))

print(solve())

# 0 < x
# 0 < -x
# 0 < --x 