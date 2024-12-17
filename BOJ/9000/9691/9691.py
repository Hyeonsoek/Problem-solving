def solve():
    n = int(input())
    
    i = 1
    k = 0
    while i <= n:
        i *= 2
        k += 1
    i //= 2
    k -= 1
    
    res = (n - i) * (n - i + 1) // 2
    for i in range(1, k + 1):
        res += ((2 ** (i-1) - 1) * 2 ** (i-1)) // 2
    
    print(res)

solve()