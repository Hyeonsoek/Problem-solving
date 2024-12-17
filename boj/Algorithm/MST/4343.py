import math
import sys
input = sys.stdin.readline

def mst(graph, satelite, outpost):
    answer, count = [], 0
    parent = [x for x in range(outpost + 1)]

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
            answer.append(cost)
            count += 1
            
            if count == outpost - satelite:
                break
    
    return answer[-1]

n = int(input())
for _ in range(n):
    satelite, outpost = map(int, input().split())
    locations = [list(map(float, input().split())) for _ in range(outpost)]

    GRAPH = []

    for i in range(outpost):
        for j in range(i + 1, outpost):
            sx, sy = locations[i]
            ex, ey = locations[j]

            cost = math.sqrt((sx-ex)**2 + (sy-ey)**2)
            GRAPH.append((i, j, cost))

    GRAPH.sort(key=lambda x: x[2])

    print('{:.2f}'.format(mst(GRAPH, satelite, outpost)))