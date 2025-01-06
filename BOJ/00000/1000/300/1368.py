import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    edges = []
    for x in range(1, n + 1):
        edges.append((int(input()), 0, x))
    
    for x in range(1, n + 1):
        arr = list(map(int, input().split()))
        for y in range(x + 1, n + 1):
            edges.append((arr[y-1], x, y))
    
    edges.sort()
    
    parent = [x for x in range(n+1)]
    
    def find(v):
        if v == parent[v]:
            return v
        parent[v] = find(parent[v])
        return parent[v]
    
    def merge(u, v):
        u = find(u)
        v = find(v)
        
        if u == v:
            return False
        
        parent[u] = v
        return True
    
    result = 0
    for cost, u, v in edges:
        if merge(u, v):
            result += cost
            
    print(result)
    
solve()
    
# 4
# 5 4 4 3

# 0 2 2 2
# 2 0 3 3
# 2 3 0 4
# 2 3 4 0