import math
from sys import stdin
input = lambda : map(int, stdin.readline().split())

n, m = input()
vertices = [ list(input()) for _ in range(n) ]
already = []

for _ in range(m):
    start, end = sorted(input())
    already.append((start - 1, end - 1))

parent = [ x for x in range(n) ]

def find(v):
    global parent
    if v == parent[v]:
        return v
    parent[v] = find(parent[v])
    return parent[v]

def merge(u, v):
    global parent
    
    u = find(u)
    v = find(v)
    
    if u == v:
        return False

    parent[u] = v
    return True

GRAPH = []

for y, x in already:
    merge(y, x)

for y in range(n - 1):
    for x in range(y + 1, n):
        sx, sy = vertices[y]
        ex, ey = vertices[x]
        cost = math.sqrt((sx - ex) ** 2 + (sy - ey) ** 2)
        
        GRAPH.append((cost, y, x))

GRAPH.sort(key=lambda x: x[0])

edges = []
count = 0
for edge in GRAPH:
    cost, y, x = edge
    if merge(y, x):
        edges.append(edge)
        count += 1
        
        if count == n - m:
            break

answer = 0
for edge in edges:
    cost, y, x = edge
    answer += cost

print("{:.2f}".format(answer))