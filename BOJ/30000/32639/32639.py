# import sys
# from heapq import *
# sys.setrecursionlimit(100010)
# input = sys.stdin.readline

# def solve():
#     n = int(input())
#     arr = [0, *map(int, input().split())]
#     graph = [[] for _ in range(n + 1)]
#     for _ in range(n-1):
#         u, v = map(int, input().split())
#         graph[u].append(v)
#         graph[v].append(u)

#     maxValue = [n] * (n + 1)
#     minValue = [1] * (n + 1)
#     used = [False] * (n + 1)
    
#     v = [[] for _ in range(n + 1)]
    
#     def dfs(node, parent):
#         if arr[node]:
#             maxValue[node] = min(maxValue[node], arr[node])
#             minValue[node] = max(minValue[node], arr[node])
        
#         used[arr[node]] = True
#         for next in graph[node]:
#             if next == parent:
#                 continue
#             maxValue[next] = min(maxValue[next], maxValue[node] - 1)
#             dfs(next, node)
#             minValue[node] = max(minValue[node], minValue[next] + 1)
        
#         if arr[node] == 0:
#             v[minValue[node]].append((maxValue[node], node))
    
#     dfs(1, 0)
    
#     for i in range(1, n + 1):
#         print(i, v[i])
    
#     queue = []
#     for i in range(1, n + 1):
#         for value, node in v[i]:
#             heappush(queue, (value, node))
        
#         if used[i]:
#             continue
        
#         if not queue:
#             print('NO')
#             return
        
#         value, node = heappop(queue)
#         arr[node] = i
    
#     def validate(node, parent):
#         for next in graph[node]:
#             if next == parent:
#                 continue
#             if arr[node] < arr[next]:
#                 return False
#             if not validate(next, node):
#                 return False
#         return True
    
#     if not validate(1, 0):
#         print('NO')
#         return

#     print('YES')
#     print(*arr[1:])

# solve()