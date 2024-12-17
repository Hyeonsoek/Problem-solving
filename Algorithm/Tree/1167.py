import sys
from collections import defaultdict
sys.setrecursionlimit(150000)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
costs = [defaultdict(int) for _ in range(n + 1)]
indegree = [0] * (n + 1)

for _ in range(n):
    start, *ends = list(map(int, input().split()))[:-1]
    for x in range(0, len(ends), 2):
        graph[start].append((ends[x], ends[x+1]))
        indegree[ends[x]] += 1

def dfs_cost(node, visited):
    result = 0
    visited[node] = True
    
    for child, egde in graph[node]:
        if not visited[child]:
            nncost = dfs_cost(child, visited) + egde
            costs[node][child] = max(nncost, costs[node][child])
            result = max(nncost, result)
            
    return result

def dfs_diamter(node, visited = [False] * (n + 1)):
    result = 0
    targets = []
    visited[node] = True
    
    for child, _ in graph[node]:
        if not visited[child]:
            result = max(result, dfs_diamter(child, visited))
            targets.append(costs[node][child])
    
    result = max(result, sum(sorted(targets)[-2:]))
    return result
            
dfs_cost(1, [False] * (n + 1))
print(dfs_diamter(1))


# 5
# 1 3 2 -1
# 2 4 4 -1
# 3 1 2 4 3 -1
# 4 2 4 3 3 5 6 -1
# 5 4 6 -1