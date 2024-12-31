import sys
sys.setrecursionlimit(2**22)
input = sys.stdin.readline
DRX = [-1, 0, 1, 0]
DRY = [0, 1, 0, -1]

class Node:
    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.d = d
    
    def gettuple(self):
        return self.x, self.y, self.d

def solve():
    H, W = map(int, input().split())
    R, C, D = map(int, input().split())

    def isinner(r, c):
        return 0 <= r < H and 0 <= c < W
    
    def tolinear(r, c, d):
        return d * H * W + r * W + c
    
    def tocube(index):
        return index // (H * W), (index // W) % H, index % W

    ruleA = [[*map(int, input().strip())] for _ in range(H)]
    ruleB = [[*map(int, input().strip())] for _ in range(H)]

    visited = [[0] * W for _ in range(H)]
    parent = [i for i in range(H * W * 4 + 1)]
    dist = [0] * (H * W * 4 + 1)
    
    def find(u):
        if parent[u] == u:
            return u, 0
        p, d = find(parent[u])
        parent[u] = p
        dist[u] += d
        return p, dist[u]
    
    def merge(u, v):
        u, ud = find(u)
        v, vd = find(v)
        if u == v:
            return
        parent[u] = v
        dist[u] = ud + vd + 1
    
    result = 0
    while True:
        for d in range(4):
            start = tolinear(R, C, d)
            nd = (d + ruleB[R][C]) % 4
            nr = R + DRX[nd]
            nc = C + DRY[nd]
            end = tolinear(0, 0, 4) if not isinner(nr, nc) else tolinear(nr, nc, nd)
            merge(start, end)
        
        visited[R][C] = 1
        result += 1
        
        nd = (D + ruleA[R][C]) % 4
        nr = R + DRX[nd]
        nc = C + DRY[nd]
        
        if not isinner(nr, nc):
            break
        
        next, distance = find(tolinear(nr, nc, nd))
        if next == tolinear(0, 0, 4):
            break
        
        D, R, C = tocube(next)
        if visited[R][C]:
            break
        
        result += distance
    
    return result

print(solve())