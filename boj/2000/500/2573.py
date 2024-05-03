from collections import deque

dir_ = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def bfs():
    lump = 0
    check = [[0] * m for _ in range(n)]

    for y in range(n):
        for x in range(m):
            if board[y][x] > 0 and check[y][x] == 0:
                lump += 1
                q = deque()
                q.append((y, x))
                check[y][x] = 1

                while q:
                    ny, nx = q.popleft() # << y, x = ny, nx

                    for yd, xd in dir_:
                        yy = ny + yd
                        xx = nx + xd
                        if (0 <= yy < n) and (0 <= xx < m) \
                                and board[yy][xx] > 0 \
                                and check[yy][xx] == 0:
                            check[yy][xx] = 1
                            q.append((yy, xx))
    return lump

def melt_down():
    global board

    b = [[0] * m for _ in range(n)]

    for y in range(n):
        for x in range(m):
            if board[y][x] > 0:
                sea = 0
                for yd, xd in dir_:
                    yy = y + yd
                    xx = x + xd
                    if (0 <= yy < n) and (0 <= xx < m)\
                            and board[yy][xx] == 0:
                        sea += 1
                b[y][x] = max(board[y][x]-sea, 0)

    for y in range(n):
        for x in range(m):
            board[y][x] = b[y][x]


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

answer = 0
while True:
    answer += 1
    melt_down()

    now = bfs()
    if now > 1:
        break

    if not sum(map(sum, board)):
        answer = 0
        break

print(answer)