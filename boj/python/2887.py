from sys import stdin

def find(u):
    global parent
    if u == parent[u]:
        return u
    parent[u] = find(parent[u])
    return parent[u]

def merge(u, v):
    global check, parent

    u = find(u)
    v = find(v)

    if u == v:
        return False

    parent[u] = v
    return True


n = int(input())
xx, yy, zz = [], [], []

for i in range(n):
    x, y, z = map(int, stdin.readline().split())

    xx.append((x, i))
    yy.append((y, i))
    zz.append((z, i))

xx.sort()
yy.sort()
zz.sort()

check = False
parent = [x for x in range(n)]

graph = []
for i in range(1, n):
    graph.append([abs(xx[i][0] - xx[i - 1][0]), xx[i][1], xx[i-1][1]])
    graph.append([abs(yy[i][0] - yy[i - 1][0]), yy[i][1], yy[i-1][1]])
    graph.append([abs(zz[i][0] - zz[i - 1][0]), zz[i][1], zz[i-1][1]])

graph.sort(key=lambda item: item[0])

vertex = 0
result = 0
for value, a, b in graph:
    if merge(a, b):
        result += value
        vertex += 1

    if vertex == n:
        break

print(result)