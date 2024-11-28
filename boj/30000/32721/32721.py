# import sys
# from collections import deque
# sys.setrecursionlimit(1000001)
# input = sys.stdin.readline

# class SCC:
#     def __init__(self, graph, n):
#         self.n = n
#         self.graph = graph
        
#         self.index = 1
#         self.count = 0
#         self.sn = [0] * (n + 1)
#         self.dfsn = [0] * (n + 1)
#         self.finished = [0] * (n + 1)
#         self.scc = []
#         self.stack = []
        
#         for x in range(1, n + 1):
#             if self.dfsn[x] == 0:
#                 self.init(x)
    
#     def init(self, node):
#         self.dfsn[node] = self.index
#         self.index += 1
#         self.stack.append(node)
        
#         result = self.dfsn[node]
#         for next in self.graph[node]:
#             if self.dfsn[next] == 0:
#                 result = min(result, self.init(next))
#             elif self.finished[next] == 0:
#                 result = min(result, self.dfsn[next])
            
#         if self.dfsn[node] == result:
#             scc = []
#             while self.stack:
#                 top = self.stack.pop()
#                 self.sn[top] = self.count
#                 self.finished[top] = 1
#                 scc.append(top)
#                 if top == node:
#                     break
            
#             self.count += 1
#             self.scc.append(scc)
        
#         return result
    
# def tsort(scc : SCC):
#     if scc.count == 1:
#         return 0
    
#     graph = [[] for _ in range(scc.count)]
#     indegree = [0] * scc.count
#     for x in range(1, scc.n + 1):
#         for next in scc.graph[x]:
#             if scc.sn[x] != scc.sn[next]:
#                 indegree[scc.sn[next]] += 1
#                 graph[scc.sn[x]].append(scc.sn[next])
    
#     length = [len(x) for x in scc.scc]
    
#     queue = deque()
#     for x in range(scc.count):
#         if indegree[x] == 0:
#             queue.append((x, length[x]))
    
#     result = [1] * scc.count
#     for x in range(scc.count):
#         if queue:
#             node, dist = queue.popleft()
#             for next in graph[node]:
#                 nextdist = dist + max(1, length[next] - 1)
#                 result[next] = max(result[next], nextdist)
                
#                 indegree[next] -= 1
#                 if not indegree[next]:
#                     queue.append((next, nextdist))
    
#     return scc.n - max(result)

# def solve():
#     n = int(input())
#     graph = [[] for _ in range(n + 1)]
#     for i, x in enumerate(map(int, input().split())):
#         graph[i+1].append(x)
    
#     print(tsort(SCC(graph, n)))
    
# solve()