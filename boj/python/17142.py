from collections import deque
from itertools import combinations

MAX = 987654321

def bfs(c):
    global board, virus, n, m

    q = deque()
    dirr = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    check = [[-1] * n for _ in range(n)]

    for y, x in c:
        check[y][x] = 0
        q.append([y, x])

    while q:
        y, x = q.popleft()

        for ydir, xdir in dirr:
            yy, xx = y + ydir, x + xdir
            if (0 <= yy < n) and (0 <= xx < n) \
                    and check[yy][xx] == -1:
                if board[yy][xx] == 1:
                    continue
                check[yy][xx] = check[y][x] + 1
                q.append([yy, xx])

    answer = 0
    print("-----------------")
    print(c)
    for y in check:
        print(*y)
    for i in range(n):
        for j in range(n):
            if check[i][j] == -1 and board[i][j] == 0:
                return MAX
            answer = max(answer, check[i][j])
    print(answer)

    return answer


def solve():
    global board, virus, n, m

    answer = MAX
    comb = list(combinations(virus, m))

    for c in comb:
        answer = min(answer, bfs(list(c)))

    return -1 if answer == MAX else answer


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
virus = []

for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            virus.append((i, j))

print(solve())

#  0  1  0  1 -1 -1  3
#  3  2 -1  2 -1  3  2
#  4 -1 -1 -1 -1  2  1
#  0 -1  4  3  2  1  0
# -1  6  5  4  3 -1 -1
#  1 -1  6  5  4  5  6
#  0 -1  2  1  0  1  0

# 11 2
# 1 1 0 1 1 1 1 1 0 1 1
# 1 1 2 1 1 1 1 1 2 1 1
# 0 1 2 1 1 1 0 1 2 1 1
# 0 1 0 1 1 1 0 1 0 1 1
# 0 0 2 0 0 1 0 0 2 0 0
# 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1