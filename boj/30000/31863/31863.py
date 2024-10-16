import sys
from collections import deque
DRX = [-1, 1, 0, 0]
DRY = [0, 0, -1, 1]
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    board = [list(input().strip()) for _ in range(n)]
    hp = [[0] * m for _ in range(n)]
    
    sx = sy = 0
    for x in range(n):
        for y in range(m):
            if board[x][y] == '@':
                sx, sy = x, y
            elif board[x][y] == '*':
                hp[x][y] += 1
            elif board[x][y] == '#':
                hp[x][y] += 2
    
    queue = deque([])
    for x in range(4):
        for k in range(1, 3):
            xx = sx + DRX[x] * k
            yy = sy + DRY[x] * k
            if 0 <= xx < n and 0 <= yy < m and board[xx][yy] != '|':
                if board[xx][yy] in '*#' and hp[xx][yy] > 0:
                    hp[xx][yy] -= 1
                    if hp[xx][yy] == 0:
                        queue.append((xx, yy, 1))
            else:
                break
            
    while queue:
        next = []
        while queue:
            nx, ny, count = queue.popleft()
                
            for d in range(4):
                xx = nx + DRX[d]
                yy = ny + DRY[d]
                if 0 <= xx < n and 0 <= yy < m and board[xx][yy] != '|':
                    if board[xx][yy] in '*#' and hp[xx][yy] > 0:
                        hp[xx][yy] -= 1
                        if hp[xx][yy] == 0:
                            next.append((xx, yy, 1))
                    
                    if count > 1:
                        next.append((xx, yy, count - 1))
            
        while next:
            queue.append(next.pop())
    
    result = [0, 0]
    for x in range(n):
        for y in range(m):
            if board[x][y] in '*#':
                result[hp[x][y] != 0] += 1
        
    print(*result)

solve()