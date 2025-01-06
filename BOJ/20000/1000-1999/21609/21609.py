from collections import deque
from collections import Counter

dirr = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def ccw():
    return [[board[x][n-1-y] for x in range(n)] for y in range(n)]

def cw():
    return [[board[n-1-x][y] for x in range(n)] for y in range(n)]

def gravity():
    global board
    board = ccw()
    for y in range(n):
        start, end = 0, 0
        while end <= n:
            if end < n and board[y][end] != -1:
                end += 1
            else:
                temp = board[y][start:end]
                # print(temp)
                counter = Counter(temp)
                if -2 in counter:
                    for _ in range(counter[-2]):
                        temp.remove(-2)
                    for _ in range(counter[-2]):
                        temp.insert(0, -2)
                    for t in range(start, end):
                        board[y][t] = temp[t-start]
                start, end = end + 1, end + 1
    board = cw()


def can_go(value, yy, xx):
    return (0 <= yy < n) and (0 <= xx < n) \
                    and board[yy][xx] in [value, 0]

def remove_block(count, rainbow, y, x):
    check = [[0] * n for _ in range(n)]
    q = deque([[y, x]])
    check[y][x] = 1
    value = board[y][x]

    while q:
        ny, nx = q.popleft()
        board[ny][nx] = -2

        for ydir, xdir in dirr:
            yy, xx = ny + ydir, nx + xdir
            if can_go(value, yy, xx) and check[yy][xx] == 0:
                check[yy][xx] = 1
                q.append([yy, xx])

    return count * count


def find_block():
    block = []
    check = [[0] * n for _ in range(n)]
    for y in range(n):
        for x in range(n):
            if board[y][x] > 0 and check[y][x] == 0:
                zeros = []
                q = deque([[y, x]])
                check[y][x] = 1
                value = board[y][x]

                rainbow, count = 0, 0
                while q:
                    ny, nx = q.popleft()

                    count += 1

                    if board[ny][nx] == 0:
                        rainbow += 1

                    for ydir, xdir in dirr:
                        yy = ny + ydir
                        xx = nx + xdir
                        if can_go(value, yy, xx):
                            if board[yy][xx] > 0 and check[yy][xx] == 0:
                                check[yy][xx] = 1
                                q.append([yy, xx])
                            if board[yy][xx] == 0 and (yy, xx) not in zeros:
                                zeros.append((yy, xx))
                                q.append([yy, xx])

                block.append([count, rainbow, y, x])

    block.sort(key=lambda item: (-item[0], -item[1], -item[2], -item[3]))

    if len(block) > 0:
        return remove_block(*block[0])
    else:
        return 0

def auto_play():
    global board

    answer = 0
    while True:
        ret = find_block()

        if ret >= 4:
            answer += ret
        else:
            break

        gravity()
        board = ccw()
        gravity()

    return answer


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

print(auto_play())