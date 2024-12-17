import sys
DRX = [-1, 1, 0, 0]
DRY = [0, 0, -1, 1]
EMPTY = 2
from collections import deque

def solve():
    n, m = map(int, input().split())
    board = [[*map(int, input().split())] for _ in range(n)]
    
    count = [0, 0]
    for x in range(n):
        for y in range(m):
            count[board[x][y]] += 1
    
    if count[0] & 1 or count[1] & 1:
        print(-1)
        return

    result = []
    for x in range(n):
        for y in range(1, m):
            if board[x][y] == board[x][y-1] and board[x][y] != EMPTY:
                board[x][y] = EMPTY
                board[x][y-1] = EMPTY
                result.append((x + 1, y + 1, x + 1, y))
    
    for x in range(m):
        for y in range(1, n):
            if board[y][x] == board[y-1][x] and board[y][x] != EMPTY:
                board[y][x] = EMPTY
                board[y-1][x] = EMPTY
                result.append((y + 1, x + 1, y, x + 1))

    def isValid():
        for x in range(n):
            for y in range(m):
                if board[x][y] == EMPTY:
                    return True
        return False
    
    if not isValid():
        print(-1)
        return
    
    queue = deque()
    for x in range(n):
        for y in range(m):
            if board[x][y] < EMPTY:
                queue.append((x, y))
        
    valueQueue = [deque(), deque()]
    
    while queue:
        xx, yy = queue.popleft()
        value = board[xx][yy]
        
        if board[xx][yy] == EMPTY:
            continue
        
        if valueQueue[value]:
            tx, ty = valueQueue[value].popleft()
            result.append((xx + 1, yy + 1, tx + 1, ty + 1))
            
            board[xx][yy] = EMPTY
            board[tx][ty] = EMPTY
        else:
            for d in range(4):
                nxx = xx + DRX[d]
                nyy = yy + DRY[d]
                if 0 <= nxx < n and 0 <= nyy < m and board[nxx][nyy] == EMPTY:
                    valueQueue[value].append((xx, yy))
                    break
            else:
                queue.append((xx, yy))

    print(1)
    for x in result:
        print(*x)

solve()