# 덩어리가 2개가 되면 끝내는 풀이 = 외딴섬 1개 + 나머지의 MST

from sys import stdin

parent = [x for x in range(100001)]

def find(u):
    if u == parent[u]:
        return u
    parent[u] = find(parent[u])
    return parent[u]

def merge(u, v):
    global parent
    u = find(u)
    v = find(v)

    if u == v:
        return False

    parent[u] = v
    return True


N, M = map(int, input().split())
graph = [list(map(int, stdin.readline().split())) for _ in range(M)]

graph.sort(key=lambda x: x[2])

count = 0
result = []

for a, b, value in graph:
    if merge(a, b):
        count += 1
        result.append(value)

print(sum(sorted(result)[:-1]))