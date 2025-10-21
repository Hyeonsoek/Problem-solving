from math import log2

def solve():
    a, b = map(int, input().split())

    if not log2(b).is_integer():
        return -1
    
    result = ""
    while a != 0:
        if a < b:
            result = "K" + result
            b >>= 1
        else:
            result = "G" + result
            a -= b
    
    return result

print(solve())