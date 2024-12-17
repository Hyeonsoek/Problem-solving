import sys
from collections import defaultdict
input = sys.stdin.readline

class Disjoint:
    def __init__(self, n):
        self.count = [1] * n
        self.parent = [x for x in range(n)]
            
    def find(self, u):
        if self.parent[u] == u:
            return u
        self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def merge(self, u, v):
        u = self.find(u)
        v = self.find(v)
        
        if u == v:
            return False
        
        self.count[u] += self.count[v]
        self.count[v] = self.count[u]
        self.parent[u] = v
        
        return True

def solve():
    n = int(input())
    data = []
    dataset = set()
    for _ in range(n):
        x, y = map(int, input().split())
        data.append((x, y))
        dataset.add((x, y))
    data.sort()
    
    lineX = defaultdict(set)
    lineY = defaultdict(set)
    union = Disjoint(n)
    for x in range(n):
        xx, yy = data[x]
        if yy in lineX and lineX[yy]:
            lineX[yy].add(i := lineX[yy].pop())
            union.merge(x, i)
        elif xx in lineY and lineY[xx]:
            lineY[xx].add(i := lineY[xx].pop())
            union.merge(x, i)
        
        lineX[yy].add(x)
        lineY[xx].add(x)
    
    p = set(union.parent)
    m = len(p)
    if m == 1:
        xx = data[i][0]
        ycoords = set(range(3 * 10 ** 5)) - set([data[i][1] for i in range(n)])
        print(xx, ycoords.pop())
    else:
        parents = list(p)
        maxvalues = sorted([(union.count[x], x) for x in parents])

        L, R = maxvalues[m-2:]
        L, R = L[1], R[1]
        LX, LY = data[L]
        RX, RY = data[R]
        
        if (LX, RY) not in dataset:
            print(LX, RY)
            return
        
        print(RX, LY)
        
solve()