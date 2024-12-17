import sys
input = sys.stdin.readline

MAX_POW = 17

n = int(input())
ants = [ 0 ] + [ int(input()) for _ in range(n) ]

tree = [ [] for _ in range(n + 1) ]
for _ in range(n - 1):
    a, b, cost = map(int, input().split())

    tree[a].append((b, cost))
    tree[b].append((a, cost))
    
check = [ True for _ in range(n + 1) ]

sparses = [ [-1 for _ in range(MAX_POW)] for _ in range(n + 1) ]
distances = [ [0 for _ in range(MAX_POW)] for _ in range(n + 1)]

def dfs(vertex):
    check[vertex] = False
    
    for next, cost in tree[vertex]:
        if check[next]:
            sparses[next][0] = vertex
            distances[next][0] = cost
            dfs(next)

dfs(1)

for pow in range(1, MAX_POW):
    for node in range(1, n + 1):
        if sparses[node][pow - 1] == -1:
            continue
        
        prev = sparses[node][pow - 1]
        if sparses[prev][pow - 1] == -1:
            continue
        
        sparses[node][pow] = sparses[prev][pow - 1]
        distances[node][pow] = distances[node][pow - 1] + distances[prev][pow - 1]

for node in range(1, n + 1):
    x, cost = node, ants[node]
    for pow in range(MAX_POW - 1, -1, -1):
        if cost >= distances[x][pow] and distances[x][pow] != 0:
            cost -= distances[x][pow]
            x = sparses[x][pow]
    
    print(x)