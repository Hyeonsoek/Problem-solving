from sys import stdin
from collections import deque, defaultdict

dir_ = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def bfs():
    global board
    q = deque()
    q.append((0, 0))

    check = [[0] * n for _ in range(n)]
    check[0][0] = 1
    board[0][0] = 1

    while q:
        y, x = q.popleft()

        for yy, xx in switch[(y, x)]:
            if not board[yy][xx]:
                board[yy][xx] = 1
                if check[yy][xx]:
                    q.append((yy, xx))

        for yd, xd in dir_:
            yy = y + yd
            xx = x + xd
            if (0 <= yy < n) and (0 <= xx < n)\
                    and not check[yy][xx]:
                check[yy][xx] = 1
                if board[yy][xx]:
                    q.append((yy, xx))

    return sum(map(sum, board))


n, m = map(int, stdin.readline().split())
board = [[0] * n for _ in range(n)]

switch = defaultdict(list)

for _ in range(m):
    yi, xi, ai, bi = map(int, stdin.readline().split())
    switch[(yi-1, xi-1)].append((ai-1, bi-1))

print(bfs())