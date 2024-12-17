import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

class BCC:
    def __init__(self, graph, n):
        self.n = n
        self.graph = graph
        
        self.index = 1
        self.dfsn = [0] * n
        self.cut = set()
        
        for i in range(n):
            if self.dfsn[i] == 0:
                self.DFS(i, -1)
        
        self.cut = sorted(self.cut)
        
    def DFS(self, vertex, prev):
        self.dfsn[vertex] = self.index
        self.index += 1
        
        result = self.dfsn[vertex]
        for next in self.graph[vertex]:
            if next == prev:
                continue
            
            if self.dfsn[next] > 0:
                result = min(result, self.dfsn[next])
            else:
                dfsnNext = self.DFS(next, vertex)
                result = min(result, dfsnNext)
                
                if dfsnNext > self.dfsn[vertex]:
                    s, e = vertex + 1, next + 1
                    if s > e:
                        s, e = e, s
                    self.cut.add((s, e))
        
        return result

def solve():
    V, E = map(int, input().split())
    graph = [[] for _ in range(V)]
    for _ in range(E):
        u, v = map(int, input().split())
        u -= 1; v -= 1
        graph[u].append(v)
        graph[v].append(u)

    bcc = BCC(graph, V)

    c = len(bcc.cut)
    print(c)
    for s, e in bcc.cut:
        print(s, e)

solve()