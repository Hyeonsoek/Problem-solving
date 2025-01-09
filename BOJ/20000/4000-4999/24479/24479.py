import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline

def solve():
    n, m, r = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
        
    for x in range(1, n + 1):
        graph[x].sort()
    
    visited = [0] * (n + 1)
    
    def dfs(node, index):
        visited[node] = index
        for nbr in graph[node]:
            if not visited[nbr]:
                index = dfs(nbr, index + 1)
        return index
    
    dfs(r, 1)
    print(*visited[1:], sep='\n')

solve()