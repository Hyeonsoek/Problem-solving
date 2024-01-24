import sys
from collections import deque
input = sys.stdin.readline
dirr = [[-1, 0], [1, 0], [0, -1], [0, 1]]

n, k = map(int, input().split())
board = [ list(map(int, input().split())) for _ in range(n) ]
s, y, x = map(int, input().split())

targets = []

for yy in range(n):
    for xx in range(n):
        if board[yy][xx]:
            targets.append((board[yy][xx], yy, xx, 0))

targets.sort()
queue = deque(targets)
    
while queue:
    level, sy, sx, second = queue.popleft()
    
    if second == s:
        break
    
    for yd, xd in dirr:
        yy, xx = sy + yd, sx + xd
        if 0 <= yy < n and 0 <= xx < n and not board[yy][xx]:
            board[yy][xx] = level
            queue.append((level, yy, xx, second + 1))

print(board[y - 1][x - 1])