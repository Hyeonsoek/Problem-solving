import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

class BCC:
    def __init__(self, graph, n):
        self.n = n
        self.graph = graph
        
        self.index = 1
        self.dfsn = [0] * n
        self.point = set()
        
        for i in range(n):
            if self.dfsn[i] == 0:
                self.DFS(i, -1)
    
    def DFS(self, vertex, prev):
        self.dfsn[vertex] = self.index
        self.index += 1
        
        count = 0
        result = self.dfsn[vertex]
        for next in self.graph[vertex]:
            if next == prev:
                continue
            
            if self.dfsn[next] > 0:
                result = min(result, self.dfsn[next])
            else:
                count += 1
                dfsnNext = self.DFS(next, vertex)
                result = min(result, dfsnNext)
                
                if prev > -1 and dfsnNext >= self.dfsn[vertex]:
                    self.point.add(vertex + 1)

        if count > 1 and prev == -1:
            self.point.add(vertex + 1)

        return result

def solve():
    V, E = map(int, input().split())
    graph = [[] for _ in range(V)]
    for i in range(E):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)

    bcc = BCC(graph, V)

    print(len(bcc.point))
    print(*sorted(bcc.point))

solve()