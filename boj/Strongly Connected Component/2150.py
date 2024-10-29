import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def solve():
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
    
    for x in range(1, v + 1):
        graph[x].sort()
    
    count = 0
    dfsn = [0] * (v + 1)
    finished = [False] * (v + 1)
    stack = []
    
    sccgroup = []
    
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
                finished[top] = True
                scc.append(top)
                if top == node:
                    break
            sccgroup.append(sorted(scc))

        return result, count

    for x in range(1, v + 1):
        if dfsn[x] == 0:
            count = dfs(x, count + 1)[1]
    sccgroup.sort()
    
    print(len(sccgroup))
    for x in sccgroup:
        print(*x, -1)

solve()