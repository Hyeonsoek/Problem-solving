import heapq
from itertools import combinations

MAX = 987654321

def bfs(c):
    global board, virus, n, m

    q = []
    dirr = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    check = [[-1] * n for _ in range(n)]

    for y, x in c:
        check[y][x] = 0
        heapq.heappush(q, [0, y, x])

    while q:
        cost, y, x = heapq.heappop(q)

        for ydir, xdir in dirr:
            yy, xx = y + ydir, x + xdir
            if (0 <= yy < n) and (0 <= xx < n) \
                    and check[yy][xx] == -1:
                if board[yy][xx] == 1:
                    continue
                if board[yy][xx] == 0:
                    check[yy][xx] = cost + 1
                else:
                    check[yy][xx] = 0
                heapq.heappush(q, [cost + 1, yy, xx])

    answer = 0
    for i in range(n):
        for j in range(n):
            if check[i][j] == -1 and board[i][j] == 0:
                return MAX
            answer = max(answer, check[i][j])

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