import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]

    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a-1].append((b-1, c))
        graph[b-1].append((a-1, c))
    
    if n == 1:
        return 0

    cache = [0] * n
    visited = [False] * n
    def dynamic(node, value):
        result = 0
        visited[node] = True
        for nbr, cost in graph[node]:
            if not visited[nbr]:
                result += dynamic(nbr, cost)
        cache[node] = min(value, result) if result else value
        return cache[node]

    return dynamic(0, 99999999999)
    
t = int(input())
for _ in range(t):
    print(solve())