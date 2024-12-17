import itertools
from collections import deque

MAX = 987654321
dir_ = [[0, 0, 1], [0, 0, -1], [0, 1, 0], [0, -1, 0], [1, 0, 0], [-1, 0, 0]]

def rotate(idx):
    b = [[board[idx][y][x] for x in range(5)] for y in range(5)]

    for y in range(5):
        for x in range(5):
            board[idx][x][4 - y] = b[y][x]

def bfs():
    check = [[[0] * 5 for _ in range(5)] for _ in range(5)]
    check[0][0][0] = 1

    q = deque()
    q.append([0, 0, 0, 0])

    while q:
        cost, z, y, x = q.popleft()

        if (z, y, x) == (4, 4, 4):
            return cost

        for zd, yd, xd in dir_:
            zz = z + zd
            yy = y + yd
            xx = x + xd
            if 0 <= zz < 5 and 0 <= yy < 5 and 0 <= xx < 5:
                if board[zz][yy][xx] == 1 and check[zz][yy][xx] == 0:
                    check[zz][yy][xx] = 1
                    q.append((cost + 1, zz, yy, xx))

    return MAX

def brute_order(order: list):
    global order_list
    if len(order) == 5:
        order_list.append(order)
    else:
        for i in range(5):
            if i not in order:
                order.append(i)
                brute_order(order[:])
                order.pop()

def brute_rotate(idx):
    global answer
    if idx == 5:
        if board[4][4][4]:
            answer = min(answer, bfs())
    else:
        for i in range(4):
            if board[0][0][0]:
                brute_rotate(idx+1)
            rotate(idx)


order_list = []
answer = MAX
init_board = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]

# brute_order([])

for oder in itertools.permutations(range(5), 5):
    board = [init_board[i] for i in oder]
    brute_rotate(0)

print(-1 if answer == MAX else answer)