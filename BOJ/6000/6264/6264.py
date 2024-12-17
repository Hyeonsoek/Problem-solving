import sys
from collections import defaultdict, deque
input = sys.stdin.readline

class SCC:
    def __init__(self, graph : dict[list], word):
        self.n = len(word)
        self.word = word
        self.graph = graph
        
        self.index = 1
        self.count = 0
        self.sn = defaultdict(int)
        self.dfsn = defaultdict(int)
        self.finished = defaultdict(bool)
        self.scc = []
        self.stack = []
        
        for x in word:
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
            
def tsort(scc : SCC):
    indegree = [0] * scc.count
    graph = [set() for _ in range(scc.count)]
    
    for word in scc.word:
        for next in scc.graph[word]:
            if scc.sn[word] != scc.sn[next]:
                indegree[scc.sn[word]] += 1
                graph[scc.sn[next]].add(scc.sn[word])
    
    queue = deque()
    result = set()

    for x in range(scc.count):
        if indegree[x] == 0:
            value = len(scc.scc[x]) > 1
            queue.append((x, value))
            if value:
                for xx in scc.scc[x]:
                    result.add(xx)
    
    for x in range(scc.count):
        if queue:
            node, value = queue.popleft()
            
            for next in graph[node]:
                component = scc.scc[next]
                if value or len(component) > 1:
                    for word in component:
                        result.add(word)
                
                indegree[next] -= 1
                if indegree[next] == 0:
                    queue.append((next, value | (len(component) > 1)))
    
    print(len(result))
    print(*sorted(result))

def solve(n):
    word = set()
    graph = defaultdict(set)
    for _ in range(n):
        end, *starts = input().split()
        word.add(end)
        for start in starts:
            graph[start].add(end)
            word.add(start)
    
    scc = SCC(graph, word)
    tsort(scc)
    

while (n := int(input())) != 0:
    solve(n)