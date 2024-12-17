import sys
from collections import deque
sys.setrecursionlimit(10000)
input = sys.stdin.readline

class SCC:
    def __init__(self, graph, n, s):
        self.n = n
        self.graph = graph

        self.index = 1
        self.count = 1
        self.sn = [0] * (n + 1)
        self.dfsn = [0] * (n + 1)
        self.finished = [0] * (n + 1)
        self.scc = [[]]
        self.stack = []
        
        self.dfs(s)
        self.count -= 1

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

def tsort(scc : SCC, start, end):
    n = scc.count
    start = scc.sn[start]
    end = scc.sn[end]
    count = [len(scc.scc[x]) for x in range(n + 1)]
    graph = [set() for _ in range(n + 1)]
    
    for x in range(1, scc.n + 1):
        for next in scc.graph[x]:
            if scc.sn[x] and scc.sn[next] and scc.sn[x] != scc.sn[next]:
                graph[scc.sn[x]].add(scc.sn[next])
    
    dist = [0] * (n + 1)
    dist[start] = count[start]
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        
        if vertex == end:
            continue
        
        for next in graph[vertex]:
            nextvalue = dist[vertex] + count[next]
            if dist[next] < nextvalue:
                dist[next] = nextvalue
                queue.append(next)
    
    print(dist[end])

def solve():
    n, m, s, t = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)

    scc = SCC(graph, n, s)
    tsort(scc, s, t)

solve()