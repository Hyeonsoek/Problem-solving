def solve():
    n, d = map(int, input().split())
    
    if n < len(str(d)):
        return 'No solution'
    
    if len(str(d)) == n:
        return str(d)

    x = 1
    for _ in range(n - 1):
        x = (x * 10) % d
    
    if x > 0:
        x = str(d - x)
    else:
        x = str(x)

    result = '1' + '0' * (n - len(x) - 1) + x
    return result
    
print(solve())