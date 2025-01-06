import sys
sys.setrecursionlimit(110000)
input = sys.stdin.readline

class SCC:
    def __init__(self, graph, n) -> None:
        self.n = n
        self.graph = graph
        
        self.index = 1
        self.count = 0
        self.sn = [0] * n
        self.dfsn = [0] * n
        self.finished = [0] * n
        self.scc = []
        self.stack = []
        
        for x in range(n):
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

def solve():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)

    scc = SCC(graph, n)
    
    indegree = [0] * scc.count
    for x in range(n):
        for next in graph[x]:
            if scc.sn[x] != scc.sn[next]:
                indegree[scc.sn[next]] += 1
    
    count = 0
    result = []
    for x in range(scc.count):
        if indegree[x] == 0:
            count += 1
            result.extend(scc.scc[x])
    
    if count == 1:
        print(*sorted(result), sep='\n')
    else:
        print('Confused')

t = int(input())
for x in range(t):
    solve()
    if x < t - 1:
        input()
        print()