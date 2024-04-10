from collections import deque

dir_ = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def bfs(w, h, board):
    check = [[0] * w for _ in range(h)]
    q = deque()

    for i in range(h):
        for j in range(w):
            if board[i][j] == '@':
                q.append(('@', i, j, 0))
                check[i][j] = 1

    for i in range(h):
        for j in range(w):
            if board[i][j] == '*':
                q.append(('*', i, j, 0))
                check[i][j] = 2

    while q:
        ty, y, x, cost = q.popleft()

        for dy, dx in dir_:
            yy = dy + y
            xx = dx + x
            if 0 <= yy < h and 0 <= xx < w:
                if board[yy][xx] != '#':
                    if ty == '*' and check[yy][xx] != 2:
                        check[yy][xx] = 2
                        q.append(('*', yy, xx, cost+1))
                    elif ty == '@' and check[yy][xx] == 0:
                        check[yy][xx] = 1
                        q.append(('@', yy, xx, cost+1))
            else:
                if ty == '@' and check[y][x] != 2:
                    return cost+1

    return "IMPOSSIBLE"


t = int(input())

for _ in range(t):
    wi, hi = map(int, input().split())

    board_i = [list(input()) for _ in range(hi)]

    print(bfs(wi, hi, board_i))
