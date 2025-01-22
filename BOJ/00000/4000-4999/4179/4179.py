import sys
from collections import *
input = sys.stdin.readline
DRX = [-1, 1, 0, 0]
DRY = [0, 0, -1, 1]

def solve():
    R, C = map(int, input().split())
    board = [[*input().strip()] for _ in range(R)]
    
    def inner(xx, yy):
        return 0 <= xx < R and 0 <= yy < C

    queue = deque()
    fqueue = deque()
    for i in range(R):
        for j in range(C):
            if board[i][j] == 'J':
                queue.append((i, j))
            elif board[i][j] == 'F':
                fqueue.append((i, j))

    time = 1
    while queue:
        count = len(fqueue)
        for i in range(count):
            xx, yy = fqueue.popleft()
            for j in range(4):
                nx = xx + DRX[j]
                ny = yy + DRY[j]
                if inner(nx, ny) and board[nx][ny] == '.':
                    board[nx][ny] = 'F'
                    fqueue.append((nx, ny))
        
        
        count = len(queue)
        for i in range(count):
            xx, yy = queue.popleft()
            
            for j in range(4):
                nx = xx + DRX[j]
                ny = yy + DRY[j]
                if inner(nx, ny):
                    if board[nx][ny] == '.':
                        board[nx][ny] = 'J'
                        queue.append((nx, ny))
                else:
                    return time
        
        time += 1

    return "IMPOSSIBLE"

print(solve())