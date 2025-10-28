import sys

def solve():
    n, m = map(int, input().split())
    arr = [int(input()) for _ in range(n)]
    
    prefix = [0]
    for i in range(n):
        prefix.append(prefix[-1] + arr[i])
    
    cache = [[-sys.maxsize] * (m + 1) for _ in range(n + 1)]
    
    cache[1][1] = arr[i]
    for i in range(1, n + 1):
        cache[i][1] = max(0, cache[i-1][1]) + arr[i - 1]
    
    for i in range(2, n + 1):
        for j in range(1, m + 1):
            for s in range(1, i - 1):
                value = -sys.maxsize
                for e in range(1, s + 1):
                    value = max(value, cache[e][j - 1])
                cache[i][j] = max(cache[i][j], value + prefix[i] - prefix[s + 1])
    
    result = -sys.maxsize
    for i in range(1, n + 1):
        result = max(result, cache[i][m])
    print(result)

solve()