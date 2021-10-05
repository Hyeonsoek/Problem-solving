from collections import deque

dir_ = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def cheese():
    global n, m, board

    time = 0
    while True:
        if sum(map(sum, board)) == 0:
            break

        check = [[0] * m for _ in range(n)]
        q = deque()

        check[0][0] = 1
        q.append((0, 0))

        while q:
            y, x = q.popleft()

            for yd, xd in dir_:
                yy = y + yd
                xx = x + xd
                if 0 <= yy < n and 0 <= xx < m:
                    if board[yy][xx] == 1:
                        check[yy][xx] += 1
                    elif board[yy][xx] == 0 and check[yy][xx] == 0:
                        check[yy][xx] = 1
                        q.append((yy, xx))

        for y in range(n):
            for x in range(m):
                if check[y][x] >= 2:
                    board[y][x] = 0

        time += 1

    return time


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
print(cheese())