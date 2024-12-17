import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    capacity = [0, *map(int, input().split())]
    rain = [0, *map(int, input().split())]
    
    parent = list(range(n + 1))
    counts = [1] * (n + 1)
    
    result = 0
    
    for x in range(1, n + 1):
        result += capacity[x] < rain[x]
    
    def find(u):
        if parent[u] == u:
            return u
        parent[u] = find(parent[u])
        return parent[u]
    
    def merge(u, v, res: int):
        u = find(u)
        v = find(v)
        
        if u == v:
            return res
        
        if u > v:
            u, v = v, u
        
        parent[v] = u
        
        if capacity[u] < rain[u]:
            res -= counts[u]

        if capacity[v] < rain[v]:
            res -= counts[v]
        
        rain[u] += rain[v]
        counts[u] +=  counts[v]
        capacity[u] += capacity[v]
        
        if capacity[u] < rain[u]:
            res += counts[u]
            
        return res
        
    for _ in range(m):
        q = list(map(int, input().split()))
        
        if q[0] & 1:
            qq, aa, bb = q
            result = merge(aa, bb, result)
        else:
            print(result)

solve()