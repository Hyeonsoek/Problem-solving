import sys
sys.setrecursionlimit(328100)
input = sys.stdin.readline

def solve():
    n, s, root = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for x in range(n - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
        
    dist = [0] * (n + 1)
    def dfs(node, height):
        dist[node] = height
        for nbr in graph[node]:
            if not dist[nbr]:
                dfs(nbr, height + 1)
    
    dfs(root, 1)
    
    result = n - sum(sorted([ dist[x] for x in range(1, 1 + s) ])[:2]) + 1
    print(result)

solve()