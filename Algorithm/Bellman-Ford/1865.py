import sys
MAX = sys.maxsize
input = sys.stdin.readline

def solve():
    n, m, w = map(int, input().split())
    graph = []
    for _ in range(m):
        s, e, t = map(int, input().split())
        graph.append((s, e, t))
        graph.append((e, s, t))
    
    for _ in range(w):
        s, e, t = map(int, input().split())
        graph.append((s, e, -t))
    
    dist = [MAX] * (n + 1)
    for i in range(n):
        for start, end, cost in graph:
            if dist[end] > dist[start] + cost:
                dist[end] = dist[start] + cost
                if i == n - 1:
                    return "YES"
    
    return "NO"

for _ in range(int(input())):
    print(solve())