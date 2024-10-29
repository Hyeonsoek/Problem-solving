import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
        
    count = 0
    index = [1]
    sn = [0] * (n + 1)
    dfsn = [0] * (n + 1)
    finished = [False] * (n + 1)
    sccgroup = []
    
    stack = []
    def dfs(node, count):
        dfsn[node] = count
        stack.append(node)
        
        result = dfsn[node]
        for next in graph[node]:
            if dfsn[next] == 0:
                r, count = dfs(next, count + 1)
                result = min(result, r)
            elif not finished[next]:
                result = min(result, dfsn[next])
        
        if result == dfsn[node]:
            scc = []
            while stack:
                top = stack.pop()
                sn[top] = index[0]
                finished[top] = True
                scc.append(top)
                if top == node:
                    break
            index[0] += 1
            sccgroup.append(scc)
        
        return result, count
    
    for x in range(1, n + 1):
        if dfsn[x] == 0:
            count = dfs(x, count + 1)[1]
    
    indegree = [0] * index[0]
    for x in range(1, n + 1):
        for next in graph[x]:
            if sn[x] != sn[next]:
                indegree[sn[next]] += 1
    
    result = 0
    for x in range(1, index[0]):
        result += indegree[x] == 0
    print(result)

for _ in range(int(input())):
    solve()