import sys, collections
dirr = [[-1, 0], [1, 0], [0, -1], [0, 1]]
input = sys.stdin.readline

n = int(input())
board = [ list(map(int, input().split())) for _ in range(n) ]
visited = [ [0] * n for _ in range(n) ]

color = 1
groups = []
for y in range(n):
    for x in range(n):
        if board[y][x] and not visited[y][x]:
            group = []
            queue = collections.deque()

            visited[y][x] = 1
            queue.append((y, x))
            group.append((y, x))
            
            while queue:
                sy, sx = queue.popleft()
                
                for dy, dx in dirr:
                    yy, xx = dy + sy, dx + sx
                    
                    if 0 <= yy < n and 0 <= xx < n and not visited[yy][xx] and board[yy][xx]:
                        visited[yy][xx] = 1
                        group.append((yy, xx))
                        queue.append((yy, xx))
                        
            groups.append(group)

result = 300
group_len = len(groups)   
for front in range(group_len - 1):
    for end in range(front + 1, group_len):
        for fy, fx in groups[front]:
            for ey, ex in groups[end]:
                target = abs(fy - ey) + abs(fx - ex) - 1
                result = min(result, target)
                
print(result)

# color = 1
# for y in range(n):
#     for x in range(n):
#         if board[y][x] > 0 and not visited[y][x]:
#             queue = collections.deque()
            
#             visited[y][x] = 1
#             board[y][x] = color
#             queue.append((y, x))
            
#             while queue:
#                 sy, sx = queue.popleft()
                
#                 for dy, dx in dirr:
#                     yy, xx = dy + sy, dx + sx
#                     if 0 <= yy < n and 0 <= xx < n:
#                         if visited[yy][xx]:
#                             continue
                        
#                         if board[yy][xx] == 1:
#                             visited[yy][xx] = 1
#                             board[yy][xx] = color
#                             queue.append((yy, xx))
            
#             color += 1

# result = 300
# for y in range(n):
#     for x in range(n):
#         if board[y][x]:
#             queue = collections.deque()
#             visited = [[0] * n for _ in range(n)]
            
#             visited[y][x] = 1
#             queue.append((y, x, board[y][x], 0))
            
#             while queue:
#                 sy, sx, color, cost = queue.popleft()
                
#                 for dy, dx in dirr:
#                     yy, xx = dy + sy, dx + sx
#                     if 0 <= yy < n and 0 <= xx < n:
#                         if not visited[yy][xx]:
#                             visited[yy][xx] = 1
                            
#                             if board[yy][xx] == 0:
#                                 queue.append((yy, xx, color, cost + 1))
#                             elif board[yy][xx] != color:
#                                 result = min(result, cost)

# print(result)

# 10
# 1 1 1 0 0 0 0 1 1 1
# 1 1 1 1 0 0 0 0 1 1
# 1 0 1 1 0 0 0 0 1 1
# 0 0 1 1 0 0 0 0 0 1
# 0 0 0 0 0 0 0 0 0 1
# 0 0 0 0 0 0 0 0 0 1
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 1 1 0 0 0 0
# 0 0 0 0 1 1 1 0 0 0
# 0 0 0 0 0 0 0 0 0 0