import sys

def mst(graph):
    global m, n

    answer, count = 0, 0
    parent = [x for x in range(m)]

    def find(u):
        if parent[u] != u:
            parent[u] = find(parent[u])
        return parent[u]

    def merge(u, v):
        u = find(u)
        v = find(v)

        if u == v:
            return False

        if u < v:
            parent[v] = u
        else:
            parent[u] = v

        return True

    for a, b, cost in graph:
        if merge(a, b):
            answer += cost
            count += 1

        if count == m - 1:
            return answer

    return 0


while True:
    m, n = map(int, input().split())

    if n == 0 and m == 0:
        break

    MAX = 0
    GRAPH = []

    for _ in range(n):
        edge = list(map(int, sys.stdin.readline().split()))
        GRAPH.append(edge)
        MAX += edge[2]

    GRAPH.sort(key=lambda x: x[2])

    print(MAX - mst(GRAPH))