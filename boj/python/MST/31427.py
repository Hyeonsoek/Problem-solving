import sys, itertools
from collections import defaultdict
input = sys.stdin.readline

n, m, q = map(int, input().split())
edges = defaultdict(list)

for _ in range(m):
    start, end, owner = input().split()
    edges[owner].append([int(start), int(end)])
    
def find(parent, u):
    if u == parent[u]:
        return u
    parent[u] = find(parent, parent[u])
    return parent[u]

def merge(parent, u, v):
    u = find(parent, u)
    v = find(parent, v)
    
    if u == v:
        return False
    
    if u < v:
        parent[v] = u
    else:
        parent[u] = v
        
    return True

MST = {}

for x in itertools.permutations("ABCDE", 5):
    mst = defaultdict(int)
    parent = [x for x in range(n + 1)]
    for owner in x:
        for start, end in edges[owner]:
            if merge(parent, start, end):
                mst[owner] += 1
    MST[x] = mst

for _ in range(q):
    query = sorted(list(zip(map(int, input().split()), 'ABCDE')))
    target = list(zip(*query))[1]
    mst = MST[target]
    
    result = 0
    for cost, owner in query:
        result += mst[owner] * cost
    print(result)