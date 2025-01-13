from collections import defaultdict

def solve():
    n = int(input())
    graph = defaultdict(set)
    vertex = set()
    
    for i in range(n):
        sx, sy, ex, ey = map(int, input().split())
        graph[sx, sy].add((ex, ey))
        graph[ex, ey].add((sx, sy))
        vertex.add((sx, sy))
        vertex.add((ex, ey))
    
    visited = defaultdict(bool)
    component = defaultdict(list)
    
    def DFS(i, node):
        visited[node] = True
        component[i].append(node)
        for next in graph[node]:
            if not visited[next]:
                DFS(i, next)
    
    def isPolygon(component):
        for i in component:
            if len(graph[i]) != 2:
                return False
        
        s = component[0]
        e = component[-1]
        return s in graph[e]
    
    i = 0
    for v in vertex:
        if not visited[v]:
            DFS(i, v)
            i += 1
    
    result = 0
    for i, c in component.items():
        result += isPolygon(c)
    
    print(result)

solve()