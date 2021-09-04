from collections import deque

dirr = [[-1, 0], [1, 0], [0, -1], [0, 1]]

N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

answer = 0

def check(y, x):
    for ydir, xdir in dirr:
        yy, xx = y + ydir, x + xdir
        if 0 <= yy < N and 0 <= xx < N:
            if L <= abs(board[y][x]-board[yy][xx]) <= R:
                return True
    return False

def repeat_check():
    for y in range(N):
        for x in range(N):
            if check(y, x):
                return False
    return True

while True:
    if repeat_check():
        break

    queue = deque()
    check_map = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if check(i, j) and check_map[i][j] == 0:
                queue.append((i, j))
                check_map[i][j] = 1
                union = []
                cost = 0

                while queue:
                    y, x = queue.popleft()
                    cost += board[y][x]
                    union.append((y, x))

                    for ydir, xdir in dirr:
                        yy, xx = y + ydir, x + xdir
                        if (0 <= yy < N) and (0 <= xx < N) \
                                and (L <= abs(board[yy][xx]-board[y][x]) <= R)\
                                and check_map[yy][xx] == 0:
                            queue.append((yy, xx))
                            check_map[yy][xx] = 1

                for y, x in union:
                    board[y][x] = cost // (len(union))

    answer += 1

print(answer)