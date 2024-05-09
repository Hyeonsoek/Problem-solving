import sys, heapq
input = sys.stdin.readline

def solve():
    result = 0
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        a, b, cost = map(int, input().split())
        
        result += cost
        heapq.heappush(edges, (cost, a, b))
        
    parent = [x for x in range(n + 1)]
    
    def find(u):
        if parent[u] == u:
            return u
        parent[u] = find(parent[u])
        return parent[u]
    
    count = 0
    while edges:
        cost, u, v = heapq.heappop(edges)
        
        u = find(u)
        v = find(v)
        
        if u == v:
            continue
        
        parent[u] = v
        
        count += 1
        result -= cost
    
    return -1 if count < n - 1 else result

print(solve())