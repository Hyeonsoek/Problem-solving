import sys, heapq
sys.setrecursionlimit(200000)
input = sys.stdin.readline

def solve():
    n, m, r = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        heapq.heappush(graph[u], -v)
        heapq.heappush(graph[v], -u)
    
    visited = [0] * (n + 1)
    
    def dfs(node, index):
        visited[node] = index
        while graph[node]:
            nbr = -heapq.heappop(graph[node])
            if not visited[nbr]:
                index = dfs(nbr, index + 1)
        return index
    
    dfs(r, 1)
    print(*visited[1:], sep='\n')

solve()