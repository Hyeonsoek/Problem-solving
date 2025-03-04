def solve():
    n = int(input())
    L = [*map(int, input().split())]
    J = [*map(int, input().split())]
    
    cache = [[0] * 101 for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(101):
            if j - L[i - 1] > 0:
                cache[i][j] = max(cache[i - 1][j], cache[i-1][j - L[i - 1]] + J[i - 1])
            else:
                cache[i][j] = cache[i - 1][j]
    
    print(max(cache[n]))

solve()