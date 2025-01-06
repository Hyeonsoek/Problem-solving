import sys
input = sys.stdin.readline

def make_tree(graph, n):
    visited = [False] * (n + 1)
    indegree = [0] * (n + 1)
    outdegree = [0] * (n + 1)
    
    def dfs(node):
        visited[node] = True
        for x in graph[node]:
            if not visited[x]:
                dfs(x)
                indegree[x] += 1
                outdegree[node] += 1
    
    dfs(1)
    
    return indegree, outdegree

def solve():
    n = int(input())
    graph = [[] for _ in range(n + 1)]
    for _ in range(n-1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    indegree, outdegree = make_tree(graph, n)
        
    m = int(input())
    for _ in range(m):
        q, a = map(int, input().split())
        if q & 1:
            print("no" if indegree[a] + outdegree[a] <= 1 else "yes")
        else:
            print("yes")

solve()