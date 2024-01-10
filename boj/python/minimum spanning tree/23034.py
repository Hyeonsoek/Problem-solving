from sys import stdin
from collections import deque
input = stdin.readline

N, M = map(int, input().split())
graph = sorted([ list(map(int, input().split())) for _ in range(M) ], key= lambda x: x[2])

parent = [ x for x in range(N + 1) ]

def find(u):
    if u == parent[u]:
        return u
    parent[u] = find(parent[u])
    return parent[u]

def merge(u, v):
    u = find(u)
    v = find(v)
    
    if u == v:
        return False
    
    parent[u] = v
    return True

MST = [ [] for _ in range(N + 1) ]
COST, count = 0, 0
for A, B, cost in graph:
    if merge(A, B):
        MST[A].append((B, cost))
        MST[B].append((A, cost))
        COST += cost
        if count == N - 1:
            break
    
max_edge = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for start in range(1, N + 1):
    queue = deque()
    check = [ True for _ in range(N + 1) ]
    
    check[start] = False
    queue.append((start, 0))
    
    while queue:
        vertex, max_cost = queue.popleft()
        
        for next, cost in MST[vertex]:
            if check[next]:
                check[next] = False
                max_edge[start][next] = max(max_cost, cost)
                queue.append((next, max(cost, max_cost)))
    
        
query = int(input())
for _ in range(query):
    start, end = map(int, input().split())
    print(COST - max_edge[start][end])

# 7 11
# 1 2 7
# 1 4 5
# 2 4 9
# 4 5 15
# 4 6 6 
# 6 5 8
# 6 7 11
# 7 5 9
# 5 3 5 
# 3 2 8
# 2 5 7
# 1
# 1 5
