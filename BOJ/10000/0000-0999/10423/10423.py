import sys
input = sys.stdin.readline

def solve():
    n, m, k = map(int, input().split())
    p = set(map(int, input().split()))
    
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((w, u, v))
    edges.sort()

    convert = {}
    parent = {}
    
    for i in range(1, n + 1):
        if i in p:
            parent[-i] = -i
            convert[i] = -i
        else:
            parent[i] = i
            convert[i] = i
    
    def find(x):
        if parent[x] == x:
            return x
        parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        x = find(x)
        y = find(y)
        
        if x == y:
            return False
        
        if x < 0 and y < 0:
            return False
        
        if y < x:
            x, y = y, x
        
        parent[y] = x
        return True
    
    result = 0
    for w, u, v in edges:
        if union(convert[u], convert[v]):
            result += w
    
    print(result)
    
solve()