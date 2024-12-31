def solve():
    n, t = map(int, input().split())
    x = input()
    
    size = 2 ** n
    digits = 2 ** (n - t)
    
    result = ''
    for i in range(0, size, digits):
        result = max(result, x[i:i+digits])
    
    print(result)

solve()