import sys
input = sys.stdin.readline

class Disjoint:
    def __init__(self, n):
        self.parent = [x for x in range(n + 1)]
    
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

def solve():
    n, m = map(int, input().split())
    egdes = []
    for x in range(1, m + 1):
        u, v, c = map(int, input().split())
        egdes.append((c, u, v, x))
    
    if n - 1 == m:
        print("NO")
        return
    
    egdes.sort(reverse=True)
    
    maxValue = 0
    maxEgde = set()
    maxJoint = Disjoint(n)
    for c, u, v, i in egdes:
        if maxJoint.merge(u, v):
            maxValue += c
            maxEgde.add(i)
    
    result = []
    nstJoint = Disjoint(n)
    
    for c, u, v, i in egdes:
        if i in maxEgde:
            continue
        
        if nstJoint.merge(u, v):
            result.append(i)
    
    for c, u, v, i in egdes:
        if nstJoint.merge(u, v):
            result.append(i)
    
    print("YES")
    print(*sorted(result))

solve()