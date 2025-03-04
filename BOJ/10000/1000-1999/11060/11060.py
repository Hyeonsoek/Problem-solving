def solve():
    n = int(input())
    arr = [*map(int, input().split())]
    
    cache = [n + 1] * n
    cache[0] = 0

    for i in range(n):
        for j in range(1, arr[i] + 1):
            if i + j < n:
                cache[i + j] = min(cache[i + j], cache[i] + 1)
    
    if cache[n - 1] != n + 1:
        print(cache[n - 1])
    else:
        print(-1)
    
solve()