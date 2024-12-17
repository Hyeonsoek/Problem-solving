import sys
from collections import deque
sys.setrecursionlimit(700001)
input = sys.stdin.readline

class SCC:
    def __init__(self, graph, cash, rest, n):
        self.index = 0
        self.count = 1
        self.graph = graph
        self.cach = cash
        self.rest = rest
        self.sn = [0] * (n + 1)
        self.dfsn = [0] * (n + 1)
        self.finished = [False] * (n + 1)
        self.scc = [[], ]
        self.sCash = [0, ]
        self.sHasRest = [0, ]
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
            value = 0
            isrest = False
            while self.stack:
                top = self.stack.pop()
                self.sn[top] = self.count
                self.finished[top] = True
                
                value += self.cach[top-1]
                isrest |= top in self.rest
                scc.append(top)
                if top == node:
                    break
            self.count += 1
            self.sCash.append(value)
            self.sHasRest.append(isrest)
            self.scc.append(scc)
            
        return result

def solve():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        s, e = map(int, input().split())
        graph[s].append(e)
    
    cash = [int(input()) for _ in range(N)]
    S, P = map(int, input().split())
    rest = set([*map(int, input().split())])
    
    scc = SCC(graph, cash, rest, N)
    
    sn = scc.count
    sindegree = [0] * sn
    sgraph = [[] for _ in range(sn)]
    
    for x in range(1, N + 1):
        for next in graph[x]:
            if scc.sn[x] != scc.sn[next]:
                sindegree[scc.sn[next]] += 1
                sgraph[scc.sn[x]].append(scc.sn[next])
    
    sMax = [0] * sn
    sCanVisited = [False] * sn
    sCanVisited[scc.sn[S]] = True
    
    queue = deque()
    for x in range(1, sn):
        sMax[x] = scc.sCash[x]
        if sindegree[x] == 0:
            queue.append(x)
    
    for x in range(1, sn):
        if queue:
            node = queue.popleft()
            
            for next in sgraph[node]:
                if sCanVisited[node]:
                    sMax[next] = max(sMax[next], sMax[node] + scc.sCash[next])
                    sCanVisited[next] = True
                    
                sindegree[next] -= 1
                if not sindegree[next]:
                    queue.append(next)
    
    answer = 0
    for x in range(1, sn):
        if scc.sHasRest[x] and sCanVisited[x]:
            answer = max(answer, sMax[x])
    
    print(answer)

solve()