from collections import deque
from itertools import combinations

RED = 1
GREEN = 2
FLOWER = 3

def bfs(green, red):
    global board

    check = [[(0, 0) for _ in range(m)] for _ in range(n)]
    q = deque()

    for y, x in green:
        q.append((y, x, GREEN, 0))
        check[y][x] = (GREEN, 0)
        board[y][x] = 0

    for y, x in red:
        q.append((y, x, RED, 0))
        check[y][x] = (RED, 0)
        board[y][x] = 0

    count = 0
    while q:
        y, x, color, time = q.popleft()

        if check[y][x][0] == FLOWER:
            continue

        for yd, xd in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            yy = y + yd
            xx = x + xd
            if (0 <= yy < n) and (0 <= xx < m) \
                    and board[yy][xx] != 0:
                if check[yy][xx] == (0, 0):
                    check[yy][xx] = (color, time)
                    q.append((yy, xx, color, time + 1))
                elif (check[yy][xx] == (RED, time) and color == GREEN) \
                        or (check[yy][xx] == (GREEN, time) and color == RED):
                    check[yy][xx] = (FLOWER, time)
                    count += 1

    for y, x in red:
        board[y][x] = 1

    for y, x in green:
        board[y][x] = 1

    return count

def delete_other(locations, others):
    temp = []
    for loc in locations:
        if loc not in others:
            temp.append(loc)
    return temp


n, m, g, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

answer = 0
medium_location = []
for ii in range(n):
    for jj in range(m):
        if board[ii][jj] == 2:
            medium_location.append((ii, jj))

greens = list(combinations(medium_location, g))
for gg in greens:
    delete_green = delete_other(medium_location, gg)
    reds = list(combinations(delete_green, r))
    for rr in reds:
        answer = max(answer, bfs(gg, rr))

print(answer)