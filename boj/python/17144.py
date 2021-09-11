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
    # up - counter clock wide
    ur, uc = up
    up_block = copy.deepcopy(b[:ur + 1])

    


for _ in range(t):
    up, down = None, None
    for i in range(r):
        for j in range(c):
            if board[i][j] > 0:
                spread_dust(board, new_board, i, j)
            if board[i][j] == -1:
                if not up:
                    up = (i, j)
                else:
                    down = (i, j)

    # spread_wind(new_board, up, down)

    board = copy.deepcopy(new_board)

for y in board:
    print(y)

answer = 0
for i in range(r):
    for j in range(c):
        if board[i][j] > 0:
            answer += board[i][j]

print(answer)