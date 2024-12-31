import math

def solve():
    n, d = map(int, input().split())
    
    operator = 'L' if n < 0 else 'R'
    n = abs(n)
    gcd = math.gcd(n, d)
    n //= gcd
    d //= gcd
    
    if not math.log2(d).is_integer():
        return -1

    result = []
    while d > 1:
        result.append('D')
        d //= 2
    
    while n > 0:
        if n & 1:
            result.append(operator)
        result.append('U')
        n //= 2

    print(len(result))
    return ''.join(result)

print(solve())