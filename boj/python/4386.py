import math

def mst(graph):
    answer, count = 0, 0
    parent = [x for x in range(n+1)]

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

    for a, b, cost in graph:
        if merge(a, b):
            answer += cost
            count += 1

    if count == n-1:
        return answer
    else:
        return 0


n = int(input())
locations = [list(map(float, input().split())) for _ in range(n)]

GRAPH = []

for i in range(n):
    for j in range(n):
        if i != j:
            sx, sy = locations[i]
            ex, ey = locations[j]

            cost = math.sqrt((sx-ex)**2 + (sy-ey)**2)

            if (j, i, cost) not in GRAPH:
                GRAPH.append((i, j, cost))

GRAPH.sort(key=lambda x: x[2])

print(mst(GRAPH))