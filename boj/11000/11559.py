from collections import deque

dir_ = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def delete_block():
    pop_block = []
    for y in range(12):
        for x in range(6):
            if board[y][x] in ['R', 'G', 'B', 'P', 'Y']:
                block = []
                check = [[0] * 6 for _ in range(12)]
                q = deque()

                color = board[y][x]
                check[y][x] = 1
                q.append((y, x))

                while q:
                    ny, nx = q.popleft()
                    block.append((ny, nx))

                    for yd, xd in dir_:
                        yy = ny + yd
                        xx = nx + xd
                        if (0 <= yy < 12) and (0 <= xx < 6) \
                                and board[yy][xx] == color and not check[yy][xx]:
                            check[yy][xx] = 1
                            q.append((yy, xx))

                if len(block) >= 4:
                    pop_block.append(block[:])

    return pop_block


def gravity():
    global board

    rev_board = list(map(list, zip(*board)))
    for line in range(6):
        count = 0
        while True:
            try:
                rev_board[line].remove('.')
                count += 1
            except ValueError:
                break

        for _ in range(count):
            rev_board[line].insert(0, '.')

    board = list(map(list, zip(*rev_board)))

def puyopuyo():
    chain = 0
    while True:
        gravity()
        pop_block = delete_block()

        if not pop_block:
            break

        for block in pop_block:
            for y, x in block:
                board[y][x] = '.'

        chain += 1
    return chain


board = [list(input()) for _ in range(12)]
print(puyopuyo())
