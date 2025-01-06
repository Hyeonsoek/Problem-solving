import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

class SCC:
    def __init__(self, graph, n) -> None:
        self.n = n
        self.graph = graph
        
        self.count = 0
        self.index = 1
        self.sn = [0] * (n + 1)
        self.dfsn = [0] * (n + 1)
        self.finished = [0] * (n + 1)
        self.scc = []
        self.stack = []
        
        for x in range(1, n + 1):
            if self.dfsn[x] == 0:
                self.dfs(x)
        
    def dfs(self, node):
        self.dfsn[node] = self.index
        self.index += 1
        self.stack.append(node)
        
        result = self.dfsn[node]
        for next in self.graph[node]:
            if self.dfsn[next] == 0:
                result = min(result, self.dfs(next))
            elif self.finished[next] == 0:
                result = min(result, self.dfsn[next])
        
        if result == self.dfsn[node]:
            scc = []
            while self.stack:
                top = self.stack.pop()
                self.sn[top] = self.count
                self.finished[top] = True
                scc.append(top)
                if top == node:
                    break
            self.count += 1
            self.scc.append(scc)
        
        return result

def solve(n, m):
    graph = [[] for _ in range(n + 1)]
    data = [*map(int, input().split())]
    for x in range(0, 2 * m, 2):
        v, w = data[x], data[x + 1]
        graph[v].append(w)
    
    scc = SCC(graph, n)
    
    outdegree = [0] * scc.count
    for x in range(1, n + 1):
        for next in graph[x]:
            if scc.sn[x] != scc.sn[next]:
                outdegree[scc.sn[x]] += 1
    
    result = []
    for x in range(scc.count):
        if outdegree[x] == 0:
            result.extend(scc.scc[x])
    
    print(*sorted(result))
    

while (n := input().strip()) != '0':
    nn, mm = map(int, n.split())
    solve(nn, mm)