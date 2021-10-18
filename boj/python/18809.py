from collections import deque
from itertools import combinations

## 동일한 시간에만 만나야 꽃이핌 이거만 수정하면됨
## 미완성!

RED = 1
GREEN = 2
FLOWER = 3

def bfs(green, red):
    global board

    check = [[0] * m for _ in range(n)]
    q = deque()

    for y, x in green:
        q.append((y, x, GREEN))
        check[y][x] = GREEN
        board[y][x] = 0

    for y, x in red:
        q.append((y, x, RED))
        check[y][x] = RED
        board[y][x] = 0

    count = 0
    while q:
        y, x, color = q.popleft()

        if check[y][x] == FLOWER:
            continue

        for yd, xd in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            yy = y + yd
            xx = x + xd
            if (0 <= yy < n) and (0 <= xx < m) \
                    and board[yy][xx] != 0:
                if check[yy][xx] == 0:
                    check[yy][xx] = color
                    q.append((yy, xx, color))
                elif (check[yy][xx] == RED and color == GREEN) \
                        or (check[yy][xx] == GREEN and color == RED):
                    check[yy][xx] = FLOWER
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
answer_com = None
for gg in greens:
    delete_green = delete_other(medium_location, gg)
    reds = list(combinations(delete_green, r))
    for rr in reds:
        answer = max(answer, bfs(gg, rr))

reds = list(combinations(medium_location, r))
for rr in reds:
    delete_red = delete_other(medium_location, rr)
    greens = list(combinations(delete_red, g))
    for gg in greens:
        answer = max(answer, bfs(gg, rr))

print(answer)

# from collections import deque
# from itertools import combinations
#
# ## 동일한 시간에만 만나야 꽃이핌 이거만 수정하면됨
# ## 미완성!
#
# RED = 1
# GREEN = 2
# FLOWER = 3
#
# def bfs(green, red):
#     global board
#
#     check = [[False] * m for _ in range(n)]
#     q = deque()
#
#     for y, x in green:
#         q.append((y, x, GREEN, 0))
#         check[y][x] = (GREEN, 0)
#         board[y][x] = 0
#
#     for y, x in red:
#         q.append((y, x, RED, 0))
#         check[y][x] = (RED, 0)
#         board[y][x] = 0
#
#     count = 0
#     while q:
#         y, x, color, time = q.popleft()
#
#         if check[y][x] == FLOWER:
#             continue
#
#         for yd, xd in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
#             yy = y + yd
#             xx = x + xd
#             if (0 <= yy < n) and (0 <= xx < m) \
#                     and board[yy][xx] != 0:
#                 if not check[yy][xx]:
#                     check[yy][xx] = (color, time)
#                     q.append((yy, xx, color, time + 1))
#                     continue
#
#                 target_color, target_time = check[yy][xx]
#                 if ((target_color == RED and color == GREEN)
#                         or (target_color == GREEN and color == RED))\
#                         and target_time == time:
#                     check[yy][xx] = (FLOWER, time)
#                     count += 1
#
#     for y, x in red:
#         board[y][x] = 1
#
#     for y, x in green:
#         board[y][x] = 1
#
#     return count
#
# def delete_other(locations, others):
#     temp = []
#     for loc in locations:
#         if loc not in others:
#             temp.append(loc)
#     return temp
#
#
# n, m, g, r = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(n)]
#
# answer = 0
# medium_location = []
# for ii in range(n):
#     for jj in range(m):
#         if board[ii][jj] == 2:
#             medium_location.append((ii, jj))
#
# greens = list(combinations(medium_location, g))
# answer_com = None
# for gg in greens:
#     delete_green = delete_other(medium_location, gg)
#     reds = list(combinations(delete_green, r))
#     for rr in reds:
#         answer = max(answer, bfs(gg, rr))
#
# reds = list(combinations(medium_location, r))
# for rr in reds:
#     delete_red = delete_other(medium_location, rr)
#     greens = list(combinations(delete_red, g))
#     for gg in greens:
#         answer = max(answer, bfs(gg, rr))
#
# print(answer)