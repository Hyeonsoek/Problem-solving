from string import ascii_uppercase as upper

def solve():
    N, X = map(int, input().split())
    
    minValue = N
    maxValue = N * 26
    
    if not minValue <= X <= maxValue:
        return '!'
    
    P = X - N
    Z = P // 25
    A = N - Z
    R = P - Z * 25
    
    if R:
        return 'A' * (A - 1) + upper[R] + 'Z' * Z
    return 'A' * A + 'Z' * Z
    
print(solve())