from collections import deque

MAX = 987654321
dir_ = [[0, 0, 1], [0, 0, -1], [0, 1, 0], [0, -1, 0], [1, 0, 0], [-1, 0, 0]]

vertex = [((0, 0, 0), (4, 4, 4)),
          ((0, 0, 4), (4, 4, 0)),
          ((0, 4, 0), (4, 0, 4)),
          ((0, 4, 4), (4, 0, 0))]

def rotate(idx, count):
    a = [[board[idx][y][x] for x in range(5)] for y in range(5)]
    b = [[board[idx][y][x] for x in range(5)] for y in range(5)]

    if count == 1:
        for y in range(5):
            for x in range(5):
                a[x][4 - y] = b[y][x]
    elif count == 3:
        for y in range(5):
            for x in range(5):
                a[4-x][y] = b[y][x]
    elif count == 2:
        for y in range(5):
            for x in range(5):
                a[4-y][4-x] = b[y][x]

    return a

def bfs(order: list):

    ret = MAX

    for count in ro:
        b_board = [rotate(idx, c) for idx, c in zip(order, count)]

        for sl, el in vertex:
            sz, sy, sx = sl
            ez, ey, ex = el

            if b_board[sz][sy][sx] == 0 or b_board[ez][ey][ex] == 0:
                continue

            check = [[[0] * 5 for _ in range(5)] for _ in range(5)]
            check[sz][sy][sx] = 1

            q = deque()
            q.append([0, sz, sy, sx])

            while q:
                cost, z, y, x = q.popleft()

                if (z, y, x) == (ez, ey, ex):
                    if cost == 12:
                        print(12)
                        exit()
                    ret = min(ret, cost)
                    break

                for zd, yd, xd in dir_:
                    zz = z + zd
                    yy = y + yd
                    xx = x + xd
                    if 0 <= zz < 5 and 0 <= yy < 5 and 0 <= xx < 5:
                        if b_board[zz][yy][xx] == 1 and check[zz][yy][xx] == 0:
                            check[zz][yy][xx] = 1
                            q.append((cost + 1, zz, yy, xx))
    # print(ret)
    return ret

def brute_order(order: list):
    global answer
    if len(order) == 5:
        answer = min(answer, bfs(order))
    else:
        for i in range(5):
            if i not in order:
                order.append(i)
                brute_order(order[:])
                order.pop()

def brute_rotate(rot: list):
    global ro
    if len(rot) == 5:
        ro.append(rot)
    else:
        for i in range(4):
            rot.append(i)
            brute_rotate(rot[:])
            rot.pop()


ro = []
answer = MAX
board = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]

brute_rotate([])
brute_order([])

print(-1 if answer == MAX else answer)