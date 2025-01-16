# import sys
# UMAX = 100
# MAX = sys.maxsize
# input = sys.stdin.readline

# def solve():
#     n = int(input())
#     arr = [int(input()) for _ in range(n)]
#     graph = [[] for _ in range(n)]
#     for _ in range(n - 1):
#         a, b = map(int, input().split())
#         graph[a-1].append(b-1)
#         graph[b-1].append(a-1)
#     U = int(input())
    
#     def dfs(node):
#         visited[node] = 1
#         u = arr[node]
#         cache[node][u] = (U - u) ** 2
#         for nbr in graph[node]:
#             if not visited[nbr]:
#                 print(node, '->', nbr)
#                 dfs(nbr)
#                 for i in range(2, U + 1):
#                     for j in range(1, i):
#                         if cache[node][j] != MAX and cache[nbr][i-j] != MAX:
#                             cache[node][i] = min(
#                                 cache[node][i],
#                                 cache[node][j] + cache[nbr][i-j] - (U - j) ** 2 - (U - i + j) ** 2 + (U - i) ** 2
#                             )

#     cache = [[MAX] * (U + 1) for _ in range(n)]
#     visited = [0] * n
    
#     dfs(0)
    
#     for i in range(n):
#         for j in range(U + 1):
#             if cache[i][j] == MAX:
#                 cache[i][j] = 'M'
    
#     for i in range(n):
#         print(*cache[i])

# solve()