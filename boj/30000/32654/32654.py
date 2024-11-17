def solve():
    n = int(input())
    graph = [[] for _ in range(n + 1)]
    
    for x in range(1, n + 1):
        a, b = map(int, input().split())
        graph[a].append(x)
        graph[b].append(x)
    
    cache = [[0] * (n + 1) for _ in range(100)]
    
    for x in range(1, n + 1):
        cache[0][x] = int(x == 1)
    
    for k in range(1, 100):
        for x in range(1, n + 1):
            for before in graph[x]:
                cache[k][x] = max(cache[k][x], cache[k-1][before])
        if k >= 10 and cache[k][1] == 0:
            return k

    return -1

print(solve())