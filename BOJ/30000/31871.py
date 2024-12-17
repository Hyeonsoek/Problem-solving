from itertools import permutations

n = int(input())
m = int(input())

graph = [[0] * (n + 1) for _ in range(n+1)]
for _ in range(m):
    u, v, d = map(int, input().split())
    graph[u][v] = max(graph[u][v], d)
    
def distance(perm):
    node = 0
    value = 0
    for x in [*perm] + [0]:
        if graph[node][x] != 0:
            value += graph[node][x]
            node = x
        else:
            return -1
    
    return value

result = -1
for perm in permutations(range(1, n + 1)):
    result = max(distance(perm), result)
    
print(result)