from collections import deque

def solve():
    n, m = map(int, input().split())
    k, *arr = map(int, input().split())
    p = [[]] + [[*map(int, input().split())][1:] for _ in range(m)]
    
    graph = [[] for _ in range(n + 1)]
    for x in range(1, m + 1):
        for i in p[x]:
            graph[i].append(x)
    
    queue = deque(arr)
    visitedP = [0] * (m + 1)
    visitedV = [0] * (n + 1)
    
    for x in arr:
        visitedV[x] += 1
    
    while queue:
        vertex = queue.popleft()
        
        for i in graph[vertex]:
            if not visitedP[i]:
                for vv in p[i]:
                    if not visitedV[vv]:
                        queue.append(vv)
                        visitedV[vv] = 1
                visitedP[i] += 1
    
    count = 0
    for x in range(1, m + 1):
        count += visitedP[x] == 0
    
    print(count)

solve()