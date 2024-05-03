import copy
from collections import deque

MAX = 987654321

def bfs(sy, sx, y, x, d1, d2, case, check):
    global n, board

    dirr = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    pattern = [
        lambda r, c: 1 <= r < y+d1 and 1 <= c <= x,
        lambda r, c: 1 <= r <= y+d2 and x < c <= n,
        lambda r, c: y+d1 <= r <= n and 1 <= c < x - d1 + d2,
        lambda r, c: y+d2 < r <= n and x - d1 + d2 <= c <= n
    ]

    value = 0
    q = deque()
    q.append([sy, sx])
    check[sy][sx] = 1

    while q:
        r, c = q.popleft()
        value += board[r][c]

        for rdir, cdir in dirr:
            rr = r + rdir
            cc = c + cdir
            if pattern[case](rr, cc) and check[rr][cc] == 0:
                check[rr][cc] = 1
                q.append([rr, cc])

    return value

def section_value(y, x, d1, d2):
    global n, board
    section = [0] * 5
    check = [[0] * (n+1) for _ in range(n+1)]
    start = [[1, 1], [1, n], [n, 1], [n, n]]

    for i in range(d1+1):
        check[y+i][x-i] = 1
    for i in range(d2+1):
        check[y+i][x+i] = 1
    for i in range(d2+1):
        check[y+d1+i][x-d1+i] = 1
    for i in range(d1+1):
        check[y+d2+i][x+d2-i] = 1

    for i in range(4):
        yy, xx = start[i]
        section[i] = bfs(yy, xx, y, x, d1, d2, i, copy.deepcopy(check))

    board_sum = sum(map(sum, board))
    section[4] = board_sum - sum(section)

    return abs(max(section)-min(section))

def divide_section(y, x):
    global n
    ret = MAX
    for d1 in range(1, n+1):
        for d2 in range(1, n+1):
            if 1 <= y + d1 + d2 <= n \
                    and 1 <= x - d1 and x + d2 <= n:
                ret = min(ret, section_value(y, x, d1, d2))

    return ret

def gerrymandering():
    global n

    ret = MAX
    for i in range(1, n+1):
        for j in range(1, n+1):
            ret = min(ret, divide_section(i, j))
            # print(ret, i, j)

    return ret


n = int(input())
board = [list(map(int, ("0 "+input()).split())) for _ in range(n)]
board.insert(0, [0] * (n+1))

print(gerrymandering())