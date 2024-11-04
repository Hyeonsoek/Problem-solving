import sys
from collections import deque, defaultdict
input = sys.stdin.readline

class SCC:
    def __init__(self, graph : dict, keys : list):
        self.index = 1
        self.count = 0
        
        self.graph = graph
        self.sn = defaultdict(int)
        self.dfsn = defaultdict(int)
        self.finished = defaultdict(bool)
        self.scc = []
        self.stack = []
        
        for x in keys:
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

def tsort(scc : SCC, keys, find):
    graph = defaultdict(list)
    indegree = defaultdict(int)
    result = defaultdict(lambda : 1)
    
    for x, values in scc.graph.items():
        for next in values:
            if scc.sn[x] != scc.sn[next]:
                indegree[next] += 1
                graph[x].append(next)
    
    queue = deque()
    for x in keys:
        if indegree[x] == 0:
            queue.append(x)
    
    for _ in keys:
        if queue:
            node = queue.popleft()
            
            for next in graph[node]:
                result[next] += result[node]
                indegree[next] -= 1
                if not indegree[next]:
                    queue.append(next)
    
    return result[find]

def solve():
    n = int(input())
    keys = set()
    graph = defaultdict(list)
    for _ in range(n):
        end, m, *arr = input().split()
        keys.add(end)
        for x in arr:
            graph[x].append(end)
            keys.add(x)
    
    keys = list(keys)
    scc = SCC(graph, keys)
    find = input().strip()
    
    return tsort(scc, keys, find)

print(solve())