import sys
input = sys.stdin.readline

class BCC:
    def __init__(self, graph, n):
        self.n = n
        self.graph = graph
        
        self.index = 1
        self.dfsn = [0] * n
        self.stack = []
        self.bcc = []
        
        for i in range(n):
            if self.dfsn[i] == 0:
                self.DFS(i, -1)
    
    def DFS(self, vertex, prev):
        self.dfsn[vertex] = self.index
        self.index += 1
        
        result = self.dfsn[vertex]
        for next in self.graph[vertex]:
            if next == prev:
                continue
            
            if self.dfsn[vertex] > self.dfsn[next]:
                self.stack.append((vertex, next))
            
            if self.dfsn[next] > 0:
                result = min(result, self.dfsn[next])
            else:
                dfsnNext = self.DFS(next, vertex)
                result = min(result, dfsnNext)
                
                if dfsnNext >= dfsnNext[vertex]:
                    bcc = []
                    while self.stack and self.stack[-1] != (vertex, next):
                        bcc.append(self.stack.pop())
                    if self.stack:
                        bcc.append(self.stack.pop())
                    self.bcc.append(bcc)
        
        return result

def solve():
    V, E = map(int, input().split())
    graph = [[] for _ in range(V)]
    for i in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    bcc = BCC(graph, V).bcc
    
    print(len(bcc))
    for i in range(len(bcc)):
        print(f'{i} : {bcc[i]}')

solve()