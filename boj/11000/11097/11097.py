import sys
input = sys.stdin.readline

class SCC:
    def __init__(self, graph, n, result: list) -> None:
        self.n = n
        self.graph = graph
        
        self.count = 0
        self.index = 1
        self.sn = [0] * (n + 1)
        self.dfsn = [0] * (n + 1)
        self.finished = [False] * (n + 1)
        self.scc = []
        self.stack = []
        
        for x in range(1, n + 1):
            if self.dfsn[x] == False:
                self.dfs(x)
                
        for x in range(self.count):
            k = len(self.scc[x])
            if k == 1:
                continue
            for a in range(k - 1):
                result.append((self.scc[x][a], self.scc[x][a+1]))
            result.append((self.scc[x][k-1], self.scc[x][0]))

        
    def dfs(self, node):
        self.dfsn[node] = self.index
        self.index += 1
        self.stack.append(node)
        
        result = self.dfsn[node]
        for next in self.graph[node]:
            if self.dfsn[next] == 0:
                result = min(result, self.dfs(next))
            elif self.finished[next] == False:
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

def solve():
    n = int(input())
    dist = [[*map(int, input().strip())] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i == j:
                dist[i][j] = 0
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] and dist[k][j] and dist[i][j]:
                    dist[i][j] = 0
    
    graph = [[] for _ in range(n + 1)]
    for x in range(n):
        for y in range(n):
            if dist[x][y]:
                graph[x + 1].append(y + 1)
    
    result = []
    scc = SCC(graph, n, result)
    
    for x in range(1, n + 1):
        for next in graph[x]:
            if scc.sn[x] != scc.sn[next]:
                result.append((x, next))

    print(len(result))
    for x in result:
        print(*x)
    print()

for _ in range(int(input())):
    input()
    solve()