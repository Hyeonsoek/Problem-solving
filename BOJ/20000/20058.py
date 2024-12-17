# pypy pass

from collections import deque

dirr = [[-1, 0], [1, 0], [0, 1], [0, -1]]


def bfs():
    answer = 0
    check = [[0] * n for _ in range(n)]

    for y in range(n):
        for x in range(n):
            if check[y][x] == 0 and board[y][x] > 0:
                q = deque([[y, x]])
                check[y][x] = 1

                count = 0
                while q:
                    sy, sx = q.popleft()
                    count += 1

                    for ydir, xdir in dirr:
                        yy = sy + ydir
                        xx = sx + xdir
                        if (0 <= yy < n) and (0 <= xx < n) \
                                and board[yy][xx] > 0 \
                                and not check[yy][xx]:
                            check[yy][xx] = 1
                            q.append([yy, xx])

                answer = max(answer, count)

    return answer

def rotate(y, x, l):
    temp = [[0] * l for _ in range(l)]
    for i in range(l):
        for j in range(l):
            temp[j][l - i - 1] = board[y + i][x + j]

    for i in range(l):
        for j in range(l):
            board[y + i][x + j] = temp[i][j]


def firestorm(l):
    for y in range(0, n, l):
        start = 0 if (y // l) % 2 == 0 else l

        # print(y // l, (y // l) % 2, start)

        for x in range(0, n, l):
            # print(y, x)
            rotate(y, x, l)

    temp = []

    for y in range(n):
        for x in range(n):
            if board[y][x] == 0:
                continue

            count = 0
            for ydir, xdir in dirr:
                yy = y + ydir
                xx = x + xdir
                if (0 <= yy < n) and (0 <= xx < n) and board[yy][xx] > 0:
                    count += 1
            if count < 3:
                temp.append((y, x))

    for y, x in temp:
        board[y][x] -= 1


n, q = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(2 ** n)]
steps = list(map(int, input().split()))

n = 2 ** n
for step in steps:
    firestorm(2 ** step)

print(sum(map(sum, board)))
print(bfs())


# 7 1 7 7 4 5 7 6
# 7 2 2 1 3 6 2 1
# 5 6 6 3 5 6 2 7
# 4 3 5 4 4 3 1 8
# 8 1 3 4 4 5 3 4
# 7 2 6 5 3 6 6 5
# 1 2 6 3 1 2 2 7
# 6 7 5 4 7 7 1 7