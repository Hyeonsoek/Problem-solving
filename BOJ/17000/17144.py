import copy

r, c, t = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(r)]
new_board = copy.deepcopy(board)
dirr = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def spread_dust(a, b, y, x):
    count = 0
    for ydir, xdir in dirr:
        yy, xx = y + ydir, x + xdir
        if (0 <= yy < r) and (0 <= xx < c) and a[yy][xx] != -1:
            b[yy][xx] += a[y][x] // 5
            count += 1
    b[y][x] -= (a[y][x] // 5) * count


def spread_wind(b, up, down):

    for i in range(up-2, -1, -1):
        b[i+1][0] = b[i][0]
    for i in range(c-1):
        b[0][i] = b[0][i+1]
    for i in range(up):
        b[i][c-1] = b[i+1][c-1]
    for i in range(c-2, -1, -1):
        b[up][i+1] = b[up][i]
    b[up][1] = 0

    for i in range(down+1, r-1):
        b[i][0] = b[i+1][0]
    for i in range(c-1):
        b[r-1][i] = b[r-1][i+1]
    for i in range(r-2, down-1, -1):
        b[i+1][c-1] = b[i][c-1]
    for i in range(c-2, -1, -1):
        b[down][i+1] = b[down][i]
    b[down][1] = 0

for k in range(t):
    up, down = None, None
    for i in range(r):
        for j in range(c):
            if board[i][j] > 0:
                spread_dust(board, new_board, i, j)
            if board[i][j] == -1:
                if not up:
                    up = i
                else:
                    down = i

    spread_wind(new_board, up, down)

    board = copy.deepcopy(new_board)

answer = 0
for i in range(r):
    for j in range(c):
        if board[i][j] > 0:
            answer += board[i][j]

print(answer)