from sys import stdin
from collections import deque
input = stdin.readline

dirr = [[-1, 0], [1, 0], [0, -1], [0, 1]]

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

def bfs(floor):
    result = 0
    visited = [[False] * n for _ in range(n)]
    
    for y in range(n):
        for x in range(n):
            if not visited[y][x] and board[y][x] > floor:
                queue = deque([(y, x)])
                visited[y][x] = True
                
                while queue:
                    ny, nx = queue.popleft()
                    
                    for dy, dx in dirr:
                        yy = ny + dy
                        xx = nx + dx
                        if 0 <= yy < n and 0 <= xx < n and not visited[yy][xx] and board[yy][xx] > floor:
                            visited[yy][xx] = True
                            queue.append((yy, xx))
                
                result += 1
    
    return result

answer = 0
for floor in range(101):
    answer = max(answer, bfs(floor))

print(answer)