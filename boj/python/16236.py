from collections import deque

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

dirr = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def bfs(sy, sx, ey, ex, sl):

    q = deque([(0, sy, sx)])
    check = [[0] * n for _ in range(n)]

    check[sy][sx] = 1

    while q:
        cost, y, x = q.popleft()

        if (y, x) == (ey, ex):
            return cost

        for ydir, xdir in dirr:
            yy, xx = y + ydir, x + xdir
            if (0 <= yy < n) and (0 <= xx < n) \
                    and check[yy][xx] == 0:
                check[yy][xx] = 1
                q.append((cost + 1, yy, xx))

    return -1

answer = 0
shark = None
shark_level = 2

for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            shark == (i, j)

print(answer)