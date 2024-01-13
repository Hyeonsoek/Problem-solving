from sys import stdin
input = stdin.readline

n, p = map(int, input().split())
visits = [ 0 ] + [ int(input()[:-1]) for _ in range(n) ]
graph = []

for _ in range(p):
    start, end, cost = map(int, input().split())
    graph.append((2 * cost + visits[start] + visits[end], start, end))

graph.sort()

parent = [ x for x in range(n + 1) ]

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
for cost, start, end in graph:
    if merge(start, end):
        answer += cost
        count += 1
        if count == n - 1:
            break

min_index = visits.index(min(visits[1:]))
print(answer + visits[min_index])