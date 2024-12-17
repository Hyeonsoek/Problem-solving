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

#     data = [[0, 0] for _ in range(n + 1)]
    
#     for x in range(1, n + 1):
#         if arr[x] > 0:
#             data[x][0] = data[x][1] = arr[x]
    
#     queue = []
#     visited = [False] * (n + 1)
#     def dfs(node, maxvalue):
#         visited[node] = True
#         if maxvalue < data[node][1]:
#             return False
        
#         if data[node][1] == 0:
#             data[node][1] = maxvalue

#         minvalue = 0
#         for x in graph[node]:
#             if not visited[x]:
#                 if dfs(x, data[node][1] - 1) == False:
#                     return False
#                 minvalue = max(minvalue, data[x][0])
            
#         if data[node][0] == 0:
#             data[node][0] = minvalue + 1
        
#         if data[node][0] > data[node][1]:
#             return False

#         if arr[node] == 0:
#             heappush(queue, ((data[node][0], data[node][1]), node))
            
#         return True

#     if dfs(1, n) == False:
#         print("NO")
#         return
    
#     brr = [0] * (n + 1)
#     for x in range(1, n + 1):
#         brr[arr[x]] = 1
    
#     for x in range(1, n + 1):
#         if brr[x] == 0:
#             (s, e), node = heappop(queue)
#             if not s <= x <= e:
#                 print("NO")
#                 return
#             arr[node] = x
    
#     print("YES")
#     print(*arr[1:])

# solve()