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

    cost = 0

    while q:
        y, x = q.popleft()

        if switch[(y, x)]:
            for yy, xx in switch[(y, x)]:
                board[yy][xx] = 1
            switch.pop((y, x))
            check = [[0] * n for _ in range(n)]

        for yd, xd in dir_:
            yy = y + yd
            xx = x + xd
            if (0 <= yy < n) and (0 <= xx < n)\
                    and board[yy][xx] == 1\
                    and check[yy][xx] == 0:
                check[yy][xx] = 1
                q.append((yy, xx))

    return sum(map(sum, board))


n, m = map(int, stdin.readline().split())
board = [[0] * n for _ in range(n)]

switch = defaultdict(list)

for _ in range(m):
    yi, xi, ai, bi = map(int, stdin.readline().split())
    switch[(yi-1, xi-1)].append((ai-1, bi-1))

print(bfs())