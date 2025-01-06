import sys
from collections import deque
direc = [[-1, 0], [1, 0], [0, -1], [0, 1]]
input = sys.stdin.readline

def solve():
    h, w = map(int, input().split())
    board = [list(input().strip()) for _ in range(h)]
    
    result = 0
    visited = [[False] * w for _ in range(h)]
    
    for x in range(h):
        for y in range(w):
            if board[x][y] == '#' and not visited[x][y]:
                result += 1
                visited[x][y] = True
                queue = deque([(x, y)])
                
                while queue:
                    nx, ny = queue.popleft()
                    
                    for xd, yd in direc:
                        xx = nx + xd
                        yy = ny + yd
                        if 0 <= xx < h and 0 <= yy < w\
                                and not visited[xx][yy] and board[xx][yy] == '#':
                            visited[xx][yy] = True
                            queue.append((xx, yy))
    
    return result

t = int(input())
for _ in range(t):
    print(solve())