import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    cost = 0
    edges = []
    for _ in range(m):
        a, b, c, d = map(int, input().split())
        edges.append((d, c, a, b))
        cost += c
    edges.sort(reverse=True)
    
    parent = [x for x in range(n + 1)]
    
    def find(u):
        if parent[u] == u:
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

    result = 0
    for d, c, a, b in edges:
        if (d and merge(a, b)) or merge(a, b):
            result += c
    
    print(cost - result)

solve()