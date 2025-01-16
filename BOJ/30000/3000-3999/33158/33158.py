# import sys
# DATA = 'DATA'
# input = sys.stdin.readline

# def euler(trie : dict):
#     end = {}
#     start = {}
#     visited = {}
    
#     def dfs(node, head, index):
#         start[node] = index
#         visited[node] = True
#         for nbr in head:
#             if (node + nbr) not in visited:
#                 index = dfs(node + nbr, head[nbr], index + 1)
#         end[node] = index
#         return index

#     index = 1
#     for k in trie.keys():
#         index = dfs(k, trie[k], index) + 1
#     return start, end

# def solve():
#     n, q = map(int, input().split())
    
#     data = []
#     datadict = {}
#     trie = {}
#     for i in range(n):
#         string, weight = input().split()
#         weight = int(weight)
        
#         data.append((string, weight))
#         datadict[string] = (i + 1, weight)
        
#         head = trie
#         for letter in string:
#             head = head.setdefault(letter, {})
#             if DATA in head:
#                 if head[DATA][0] < weight:
#                     head[DATA][0] = weight
#                     head[DATA][1] = i + 1
#             else:
#                 head[DATA][0] = weight
#                 head[DATA][1] = i + 1
    
#     s, e = euler(trie)
#     indexes = { s : i for i, s in enumerate(s.keys(), 1) }
    
#     tree = []
    
#     for _ in range(q):
#         t, d = input().split()
#         if t not in s:
#             print(-1)
#         else:
#             print()

# solve()