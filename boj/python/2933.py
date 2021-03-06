from collections import deque
from collections import defaultdict

dir_ = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def bfs():
    check = [[0] * c for _ in range(r)]
    for y in range(r):
        for x in range(c):
            if check[y][x] == 0 and board[y][x] == 'x':
                last = False
                cluster = []
                q = deque()
                q.append((y, x))

                check[y][x] = 1

                while q:
                    ny, nx = q.popleft()
                    cluster.append((ny, nx))

                    if ny == r - 1:
                        last = True

                    for yd, xd in dir_:
                        yy = yd + ny
                        xx = xd + nx
                        if (0 <= yy < r) and (0 <= xx < c) \
                                and board[yy][xx] == 'x' \
                                and check[yy][xx] == 0:
                            check[yy][xx] = 1
                            q.append((yy, xx))

                if not last:
                    return cluster
    return []


def gravity():
    clusters = bfs()

    if not clusters:
        return

    map_dict = defaultdict(list)

    for y, x in clusters:
        board[y][x] = '.'
        map_dict[x].append(y)

    min_move = 101

    for x in map_dict:
        map_dict[x].sort()
        my, move = map_dict[x][-1], 0
        while my < r and board[my][x] == '.':
            my += 1
            move += 1
        if my == r or board[my][x] == 'x':
            move -= 1
        min_move = min(move, min_move)

    for x in map_dict:
        for y in map_dict[x]:
            board[y + min_move][x] = 'x'


def destroy_mineral(side, row):
    global board
    row_string = ''.join(board[row])
    if 'x' in row_string:
        if side:
            row_string = row_string[::-1]
            idx = row_string.find('x')
            board[row][c - idx - 1] = '.'
        else:
            idx = row_string.find('x')
            board[row][idx] = '.'

def simulate():
    for i in range(n):
        destroy_mineral(bool(i % 2), r - bar[i])
        gravity()
    for line in board:
        print(''.join(line))


r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]

n = int(input())
bar = list(map(int, input().split()))

simulate()