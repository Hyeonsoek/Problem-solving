import heapq

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dirr = [[-1, 0], [0, -1], [0, 1], [1, 0]]
make_check = lambda: [[0] * n for _ in range(n)]

def bfs(sy, sx):
    level, count, answer = 2, 0, 0
    q = [(0, sy, sx)]
    check = make_check()

    check[sy][sx] = 1

    while q:
        cost, y, x = heapq.heappop(q)

        if 1 <= board[y][x] < level:
            count += 1
            board[y][x] = 0
            if count == level:
                count = 0
                level += 1
            check = make_check()
            q.clear()
            answer += cost
            cost = 0

        for ydir, xdir in dirr:
            yy, xx = y + ydir, x + xdir
            if (0 <= yy < n) and (0 <= xx < n) and check[yy][xx] == 0 \
                    and board[yy][xx] <= level:
                check[yy][xx] = 1
                heapq.heappush(q, (cost + 1, yy, xx))

    return answer


sy, sx = -1, -1
for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            sy, sx = i, j
            board[i][j] = 0

print(bfs(sy, sx))
