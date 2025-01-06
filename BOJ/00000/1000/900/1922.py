from sys import stdin

check = False
parent = [0] * 10001

def find(u):
    global parent
    if u == parent[u]:
        return u
    parent[u] = find(parent[u])
    return parent[u]

def merge(u, v):
    global check, parent
    check = False
    u = find(u)
    v = find(v)

    if u == v:
        return

    parent[u] = v
    check = True


V = int(input())
E = int(input())
graph = [list(map(int, stdin.readline().split())) for _ in range(E)]

graph.sort(key=lambda x: x[2])

for i in range(1, V+1):
    parent[i] = i

result = 0
for a, b, value in graph:
    merge(a, b)

    if check:
        result += value

print(result)