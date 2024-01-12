import sys
input = sys.stdin.readline

n = int(input())
parent = [ x for x in range(n) ]

def find(u):
    if parent[u] == u:
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

graph = []

for y in range(n):
    costs = list(map(int, input().split()))
    for x in range(y + 1, n):
        graph.append((costs[x], y, x))
        
graph.sort()

count, answer = 0, 0
for cost, y, x in graph:
    if merge(y, x):
        count += 1
        answer += cost
        
        if count == n - 1:
            break

print(answer)