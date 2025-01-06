import sys
sys.setrecursionlimit(300100)
input = sys.stdin.readline

def solve():
    n = int(input())
    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 2):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    visited = [False] * (n + 1)
    def dfs(node):
        visited[node] = True
        for nbr in graph[node]:
            if not visited[nbr]:
                dfs(nbr)

    result = []
    for x in range(1, n + 1):
        if not visited[x]:
            dfs(x)
            result.append(x)
    
    print(*result)
    
solve()