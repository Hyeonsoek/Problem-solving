import sys
from collections import deque
input = sys.stdin.readline

horizontal = 0
vertical = 1
diagonal = 2

d = [[1, 0], [0, 1], [1, 1]]

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
board[0][0] = board[0][1] = 1

cache = [[[-1] * 3 for _ in range(n)] for _ in range(n)]
cache[n-1][n-1] = [1, 1, 1]

def dp(sy, sx, arrow):
    if cache[sy][sx][arrow] != -1:
        return cache[sy][sx][arrow]

    board[sy][sx] = 1
    result = 0

    if arrow in [vertical, diagonal]:
        yy = sy + 1
        if yy < n and board[yy][sx] != 1:
            result += dp(yy, sx, vertical)
            
    if arrow in [horizontal, diagonal]:
        xx = sx + 1
        if xx < n and board[sy][xx] != 1:
            result += dp(sy, xx, horizontal)
            
    count = 0
    for dx, dy in d:
        xx = dx + sx
        yy = dy + sy
        if xx < n and yy < n and board[yy][xx] != 1:
            count += 1
    
    if count == 3:
        result += dp(sy + 1, sx + 1, diagonal)
    
    board[sy][sx] = 0
    cache[sy][sx][arrow] = result
    return result

print(dp(0, 1, horizontal))