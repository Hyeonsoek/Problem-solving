import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    
    egdes = []
    for x in range(m):
        x, y, z, w = map(int, input().split())
        egdes.append((z, w, x, y))
    
    egdes.sort()
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
    
    result = ''
    mincost = 0
    count = 0
    for x in range(m):
        zz, ww, xx, yy = egdes[x]
        if merge(xx, yy):
            result += str(zz)
            mincost += ww
            count += 1
    
    if count == n - 1:
        print(result, mincost)
    else:
        print(-1)

solve()