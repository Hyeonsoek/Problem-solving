import sys
MAX = sys.maxsize
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
    
    dist = [MAX] * (n + 1)
    dist[1] = 0
    
    for i in range(n):
        for start in range(1, n + 1):
            for end, cost in graph[start]:
                if dist[start] != MAX and dist[end] > dist[start] + cost:
                    dist[end] = dist[start] + cost
                    if i == n - 1:
                        print(-1)
                        return
    
    for i in range(2, n + 1):
        print(dist[i] if dist[i] != MAX else -1)

solve()