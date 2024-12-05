import sys
from collections import deque
sys.setrecursionlimit(10000)
input = map(int, sys.stdin.read().split())

class SCC:
    def __init__(self, graph, n) -> None:
        self.n = n
        self.graph = graph
        
        self.count = 0
        self.index = 1
        self.sn = [0] * n
        self.dfsn = [0] * n
        self.finished = [0] * n
        self.scc = []
        self.stack = []
        
        for i in range(n):
            if self.dfsn[i] == 0:
                self.dfs(i)
    
    def dfs(self, vertex):
        self.dfsn[vertex] = self.index
        self.index += 1
        self.stack.append(vertex)
        
        result = self.dfsn[vertex]
        for nv in self.graph[vertex]:
            if not self.dfsn[nv]:
                result = min(result, self.dfs(nv))
            elif not self.finished[nv]:
                result = min(result, self.dfsn[nv])
        
        if result == self.dfsn[vertex]:
            scc = []
            while self.stack:
                top = self.stack.pop()
                self.sn[top] = self.count
                self.finished[top] = 1
                if top == vertex:
                    break
            
            self.count += 1
            self.scc.append(scc)
        
        return result

def solve():
    n, m = next(input), next(input)
    graph = [[] for _ in range(n)]
    
    for _ in range(m):
        a, b = next(input), next(input)
        graph[a].append(b)
    
    scc = SCC(graph, n)
    sccgraph = [[] for _ in range(scc.count)]
    for i in range(n):
        for nv in graph[i]:
            if scc.sn[i] != scc.sn[nv]:
                sccgraph[scc.sn[i]].append(scc.sn[nv])
    
    visited = {}
    for i in range(scc.count):
        visited[i] = [0] * scc.count
        visited[i][i] = 1
        queue = deque([i])
        while queue:
            vertex = queue.popleft()
            
            for nv in sccgraph[vertex]:
                if not visited[i][nv]:
                    visited[i][nv] = 1
                    queue.append(nv)
    
    q = next(input)
    for _ in range(q):
        s, e = next(input), next(input)
        print(visited[scc.sn[s]][scc.sn[e]])

solve()