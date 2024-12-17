import sys
from collections import deque
MAX = 10000000
dirr = [[-1, 0], [1, 0], [0, -1], [0, 1]]
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

distance = [[MAX] * m for _ in range(n)]

for x in range(n):
    for y in range(m):
        if board[x][y] != 2:
            continue
        
        distance[x][y] = 0
        
        queue = deque([(x, y, 0)])
        while queue:
            nx, ny, cost = queue.popleft()
            
            for dx, dy in dirr:
                xx = dx + nx
                yy = dy + ny
                if 0 <= xx < n and 0 <= yy < m:
                    if board[xx][yy] == 1 and distance[xx][yy] > cost + 1:
                        distance[xx][yy] = cost + 1
                        queue.append((xx, yy, cost + 1))
        
        for x in range(n):
            line = []
            for y in range(m):
                if board[x][y] == 1:
                    if distance[x][y] == MAX:
                        line.append(-1)
                    else:
                        line.append(distance[x][y])
                else:
                    line.append(0)
            
            print(*line)
        
        exit()