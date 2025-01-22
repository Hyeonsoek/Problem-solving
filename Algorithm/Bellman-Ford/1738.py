# import sys
# MAX = sys.maxsize
# input = sys.stdin.readline

# def solve():
#     n, m = map(int, input().split())
#     edge = []
#     for _ in range(m):
#         s, e, w = map(int, input().split())
#         edge.append((s, e, w))
    
#     dist = [-MAX for i in range(n + 1)]
#     dist[1] = 0
    
#     for i in range(n - 1):
#         for s, e, cost in edge:
#             if dist[s] != -MAX and dist[e] < dist[s] + cost:
#                 dist[e] = dist[s] + cost
    
#     print(dist)

# solve()