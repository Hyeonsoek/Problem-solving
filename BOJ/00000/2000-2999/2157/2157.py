import sys
from collections import defaultdict
input = sys.stdin.readline

def solve():
    n, m, k = map(int, input().split())
    graph = [defaultdict(int) for _ in range(n + 1)]
    for _ in range(k):
        a, b, c = map(int, input().split())
        if a < b:
            graph[a][b] = max(graph[a][b], c)
    
    cache = [[0] * (m + 1) for _ in range(n + 1)]
    for i, v in graph[1].items():
        cache[i][2] = v
    
    for i in range(2, m):
        for j in range(1, n + 1):
            if cache[j][i] != 0:
                for next, value in graph[j].items():
                    cache[next][i + 1] = max(cache[next][i + 1], cache[j][i] + value)
    
    print(max(cache[n]))
    
solve()