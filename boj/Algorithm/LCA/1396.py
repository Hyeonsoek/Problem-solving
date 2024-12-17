import sys
sys.setrecursionlimit(150000)
input = sys.stdin.readline

MAX_DEPTH = 17

class UnionFind:
    def __init__(self) -> None:
        self.parent = [ -1 for x in range(2 * n + 1) ]

    def find(self, u) -> int:
        if self.parent[u] < 0:
            return u
        self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v, p) -> bool:
        u = self.find(u)
        v = self.find(v)
        
        if u == v:
            return (0, 0)
        
        self.parent[u] = p
        self.parent[v] = p
        return (u, v)

class MSTWithLCA:
    def __init__(self, n : int) -> None:
        self.n = n
        self.depths = [ 0 ] * (2 * n + 1)
        self.weights = [ 0 ] * (2 * n + 1)
        self.counts = [ 1 ] * (n + 1) + [ 0 ] * n
        self.tree = [ [] for _ in range(2 * n + 1) ]
        self.parent = [ [ 0 ] * MAX_DEPTH for _ in range(2 * n + 1) ]
        self.egdes = sorted([ tuple(map(int, input().split())) for _ in range(m) ], key=lambda x:x[2])
        
        self.__make_mst()
        self.__make_lca()
    
    def __dfs(self, node, depth):
        self.depths[node] = depth
        for next in self.tree[node]:
            if not self.depths[next]:
                self.parent[next][0] = node
                self.__dfs(next, depth + 1)
    
    def __make_mst(self):
        for start, end, cost in self.egdes:
            start, end = union_find.union(start, end, self.n + 1)
            
            if start == 0 and end == 0:
                continue
            
            self.n += 1
            
            self.tree[self.n].append(start)
            self.tree[self.n].append(end)
            
            self.weights[self.n] = cost
            self.counts[self.n] = self.counts[start] + self.counts[end]
    
    def __make_lca(self):
        for node in range(1, self.n + 1):
            if union_find.parent[node] < 0:
                self.__dfs(node, 1)
                
        for pow in range(1, MAX_DEPTH):
            for node in range(1, self.n + 1):
                self.parent[node][pow] = self.parent[ self.parent[node][pow - 1] ][pow - 1]
         
    def lca(self, a, b):
        if self.depths[a] < self.depths[b]:
            a, b = b, a
        
        for pow in range(MAX_DEPTH - 1, -1, -1):
            if self.depths[a] - self.depths[b] >= 2 ** pow:
                a = self.parent[a][pow]
        
        if a != b:
            for pow in range(MAX_DEPTH - 1, -1, -1):
                if self.parent[a][pow] and self.parent[a][pow] != self.parent[b][pow]:
                    a = self.parent[a][pow]
                    b = self.parent[b][pow]

            a = self.parent[a][0]

        return self.weights[a], self.counts[a]

n, m = map(int, input().split())
union_find = UnionFind()
mst = MSTWithLCA(n)

qq = int(input())
for _ in range(qq):
    a, b = map(int, input().split())
    
    weight, count = mst.lca(a, b)
    
    if weight == 0:
        print(-1)
    else:
        print(weight, count)