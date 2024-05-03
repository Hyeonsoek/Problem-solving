n, m, k = map(int, input().split())
init_board = [list(map(int, input().split())) for _ in range(n)]
shark = list(map(int, input().split()))

priority = [[list(map(int, input().split())) for _ in range(4)] for _ in range(m)]

dirr = [None, [-1, 0], [1, 0], [0, -1], [0, 1]]

def spread_odor(key, type):
    global n, m, k, board, shark, shark_pos

    y, x = shark_pos[key]
    for d in priority[key - 1][shark[key - 1] - 1]:
        yy, xx = y + dirr[d][0], x + dirr[d][1]
        if (0 <= yy < n) and (0 <= xx < n):
            if (not type and board[yy][xx] == [0, 0]) \
                    or (type and board[yy][xx][0] == key):
                shark_pos[key] = (yy, xx)
                shark[key - 1] = d
                return True
    return False


def simulate():
    global n, m, k, board, shark, shark_pos

    for key in range(1, m + 1):
        if key in shark_pos:
            if not spread_odor(key, 0):
                spread_odor(key, 1)

    for y in range(n):
        for x in range(n):
            if board[y][x] != [0, 0]:
                key, time = board[y][x]
                if time == 1:
                    board[y][x] = [0, 0]
                else:
                    board[y][x] = [key, time - 1]

    rev_shark_pos = {shark_pos[key]: key for key in range(m, 0, -1) if key in shark_pos}
    shark_pos = {rev_shark_pos[key]: key for key in rev_shark_pos}

    for key in rev_shark_pos:
        y, x = key
        board[y][x] = [rev_shark_pos[key], k]


shark_pos = {}
board = [[[0, 0] for _ in range(n)] for _ in range(n)]

for y in range(n):
    for x in range(n):
        if init_board[y][x] > 0:
            shark_pos[init_board[y][x]] = (y, x)
            board[y][x] = [init_board[y][x], k]

for i in range(1000):
    simulate()
    if len(shark_pos) == 1:
        print(i + 1)
        exit()

print(-1)