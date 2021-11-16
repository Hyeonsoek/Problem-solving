# 덩어리가 2개가 되면 끝내는 풀이

from sys import stdin

check = False
parent = [x for x in range(100001)]

def find(u):
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


N, M = map(int, input().split())
graph = [list(map(int, stdin.readline().split())) for _ in range(M)]

graph.sort(key=lambda x: x[2])

count = N
result = 0

for a, b, value in graph:
    merge(a, b)

    if check:
        count -= 1
        result += value

        if count == 2:
            break

print(result)