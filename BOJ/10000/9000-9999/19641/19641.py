import sys
sys.setrecursionlimit(100100)
input = sys.stdin.readline
LEFT = 0
RIGHT = 1

def solve():
    n = int(input())
    graph = [[] for _ in range(n + 1)]
    for x in range(n):
        s, *nbrs = [*map(int, input().split())]
        for e in nbrs[:-1]:
            graph[s].append(e)
        graph[s].sort()
    root = int(input())
    
    tree = [[0, 0] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    
    def dfs(node, value):
        visited[node] = True
        tree[node][LEFT] = value
        for nbr in graph[node]:
            if not visited[nbr]:
                value = dfs(nbr, value + 1)
        tree[node][RIGHT] = value + 1
        return value + 1

    dfs(root, 1)
    
    for x in range(1, n + 1):
        print(x, *tree[x])

solve()