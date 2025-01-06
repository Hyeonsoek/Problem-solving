import sys
sys.setrecursionlimit(1001)
input = sys.stdin.readline

def solve():
    n = int(input())
    graph = [[] for _ in range(n + 1)]
    for i, v in enumerate(map(int, input().split()), 1):
        graph[i].append(v)
        graph[v].append(i)
    
    visited = [0] * (n + 1)
    def dfs(vertex):
        visited[vertex] = 1
        for nbr in graph[vertex]:
            if not visited[nbr]:
                dfs(nbr)
    
    result = 0
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)
            result += 1
    
    print(result)

t = int(input())
for _ in range(t):
    solve()