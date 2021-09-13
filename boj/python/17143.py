from sys import stdin

input = stdin.readline
dirr = [[-1, 0], [1, 0], [0, 1], [0, -1]]
opposite = {1: 2, 2: 1, 3: 4, 4: 3}

r, c, m = map(int, input().split())
board = [[0] * (c+2) for _ in range(r)]
shark = {}

for _ in range(m):
    rr, cc, s, d, z = map(int, input().split())
    board[rr-1][cc] = 1
    s %= (r - 1) * 2 if d in [1, 2] else (c - 1) * 2
    shark[(rr, cc)] = [s, d, z]

board.insert(0, [0] * (c+2))

def near_shark(sy, sx):
    for i in range(sy+1, r+1):
        if board[i][sx] == 1:
            return i, sx
    return -1, -1

def move_shark():
    global shark
    new_shark = {}

    for key in shark:
        s, d, z = shark[key]
        y, x = key

        # print(s, d, z)

        if s > 0:
            yy, xx = y, x
            for i in range(s):
                yy = yy + dirr[d-1][0]
                xx = xx + dirr[d-1][1]
                if not ((1 <= yy <= r) and (1 <= xx <= c)):
                    d = opposite[d]
                    yy = yy + dirr[d - 1][0] * 2
                    xx = xx + dirr[d - 1][1] * 2

            if (yy, xx) in new_shark:
                if z > new_shark[(yy, xx)][2]:
                    new_shark[(yy, xx)] = [s, d, z]
            else:
                new_shark[(yy, xx)] = [s, d, z]
            board[y][x] = 0
        else:
            new_shark[(y, x)] = [s, d, z]

    shark = new_shark
    for y, x in shark:
        board[y][x] = 1
    # print("----------------")
    # print(shark)
    # for y in board:
    #     print(*y)

answer = 0
for i in range(1, c+1):
    y, x = near_shark(0, i)
    if (y, x) != (-1, -1):
        answer += shark[(y, x)][2]
        del shark[(y, x)]
        board[y][x] = 0

    # print("------------")
    move_shark()

print(answer)