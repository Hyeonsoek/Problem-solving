import sys
input = sys.stdin.readline

class Disjoint:
    def __init__(self, n) -> None:
        self.n = n
        self.parent = [*range(n+1)]
    
    def find(self, u):
        if u == self.parent[u]:
            return u
        self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def merge(self, u, v):
        u = self.find(u)
        v = self.find(v)
        
        if u == v:
            return False
        
        self.parent[u] = v
        return True

class MST:
    def __init__(self, edge: list, n: int, m: int) -> None:
        self.n = n
        self.m = m
        self.edge = []
        self.cost = 0
        disjoint = Disjoint(n)
        for d, u, v in edge:
            if disjoint.merge(u, v):
                self.edge.append((d, u, v))
                self.cost += d

def solve():
    n, m, k = map(int, input().split())
    edge = set()
    for x in range(1, m + 1):
        a, b = map(int, input().split())
        edge.add((x, a, b))
    
    result = [0] * k
    for x in range(k):
        mst = MST(sorted(edge), n, m)
        if len(mst.edge) < n - 1:
            return result
        
        result[x] = mst.cost
        edge.remove(mst.edge[0])
    
    return result

print(*solve())