import sys
from heapq import *
DRX = [-1, -1, -1, 1, 1, 1, 0, 0]
DRY = [-1, 0, 1, -1, 0, 1, -1, 1]
input = sys.stdin.readline

def solve():
    R, C = map(int, input().split())
    board = [list(input().strip()) for _ in range(R)]

    dist = [[sys.maxsize] * C for _ in range(R)]
    queue = []
    for x in range(R):
        d = int(board[x][0] != '#')
        queue.append((d, x, 0))
        dist[x][0] = d

    while queue:
        distance, vx, vy = heappop(queue)

        if vy == C - 1:
            continue

        for i in range(8):
            nx = DRX[i] + vx
            ny = DRY[i] + vy
            if 0 <= nx < R and 0 <= ny < C:
                ndistance = distance + (board[nx][ny] != '#')
                if dist[nx][ny] > ndistance:
                    dist[nx][ny] = ndistance
                    heappush(queue, (ndistance, nx, ny))

    result = sys.maxsize
    for x in range(R):
        result = min(result, dist[x][C-1])

    print(result)

solve()