import sys
input = sys.stdin.readline

n, m = map(int, input().split())
colleges = list(input().split())

graph = []
for _ in range(m):
    u, v, d = map(int, input().split())
    
    if colleges[u-1] == colleges[v-1]:
        continue
    
    graph.append((d, u, v))

graph.sort()

parent = [ x for x in range(n) ]

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

count, answer = 0, 0
for cost, u, v in graph:
    if merge(u - 1, v - 1):
        count += 1
        answer += cost
        
        if count == n - 1:
            break

print(answer if count == n - 1 else -1)