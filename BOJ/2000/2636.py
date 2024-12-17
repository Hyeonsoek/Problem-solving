import collections
import copy

dir_ = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def bfs():
    q = collections.deque()
    temp = copy.deepcopy(board)
    check = [[0] * w for _ in range(h)]

    q.append((0, 0))
    check[0][0] = 1

    while q:
        y, x = q.popleft()

        for yd, xd in dir_:
            yy, xx = y + yd, x + xd
            if 0 <= yy < h and 0 <= xx < w and not check[yy][xx]:
                if board[yy][xx] == 1:
                    temp[yy][xx] = 0
                else:
                    q.append((yy, xx))
                check[yy][xx] = 1

    for y in range(h):
        for x in range(w):
            board[y][x] = temp[y][x]


h, w = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(h)]

last = sum(map(sum, board))
hour = 0
while True:
    bfs()
    hour += 1

    count = sum(map(sum, board))
    if count == 0:
        break

    last = count

print(hour)
print(last)