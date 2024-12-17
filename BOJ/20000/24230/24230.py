import sys
sys.setrecursionlimit(200100)
ROOT = 1
input = sys.stdin.readline

def solve():
    n = int(input())
    color = [0, *map(int, input().split())]
    graph = [[] for _ in range(n + 1)]
    for x in range(n - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * (n + 1)
    def dfs(node, parent):
        result = int(parent != color[node])
        visited[node] = True
        for nbr in graph[node]:
            if not visited[nbr]:
                result += dfs(nbr, color[node])
        return result

    print(dfs(1, 0))

solve()