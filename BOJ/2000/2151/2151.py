# import sys
# from heapq import *
# DRX = [-1, 1, 0, 0]
# DRY = [0, 0, -1, 1]
# input = sys.stdin.readline

# def find_start(board, n):
#     pos = []
#     for x in range(n):
#         for y in range(n):
#             if board[x][y] == '#':
#                 pos.append((x, y))
#     return pos

# def solve():
#     n = int(input())
#     board = [[*input()] for _ in range(n)]
#     distance = [[[sys.maxsize] * n for _ in range(n)] for _ in range(4)]
    
#     doors = find_start(board, n)
#     sx, sy = doors[0]
#     ex, ey = doors[1]
#     queue = []
    
#     for x in range(4):
#         distance[x][sx][sy] = 0
#         heappush(queue, (0, x, sx, sy))
    
#     while queue:
#         cost, dd, xx, yy = heappop(queue)
        
#         if distance[xx][yy] < cost:
#             continue
        
#         if dd in [0, 1]:
#             for d in [2, 3]:
#                 nx = xx + DRX[d]
#                 ny = yy + DRY[d]
#                 if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != '*':
                    
    
#     print(distance[ex][ey])

# solve()