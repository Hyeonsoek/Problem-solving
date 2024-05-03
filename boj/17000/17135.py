from collections import deque

dir_ = [[-1, 0], [0, -1], [0, 1]]

def simulate():
    global board
    count = 0
    new_board = [[0] * m for _ in range(n+1)]

    for y in range(n+1):
        for x in range(m):
            new_board[y][x] = board[y][x]

    while True:
        kill = set()
        for i in range(m):
            if new_board[n][i] == 2:
                target = []
                check = [[0] * m for _ in range(n+1)]
                q = deque([(0, n, i)])
                check[n][i] = 1

                while q:
                    cost, y, x = q.popleft()

                    if cost <= d and new_board[y][x] == 1:
                        target.append((cost, y, x))

                    for yd, xd in dir_:
                        yy, xx = y + yd, x + xd
                        if 0 <= yy < n+1 and 0 <= xx < m and not check[yy][xx]:
                            q.append((cost + 1, yy, xx))
                            check[yy][xx] = 1

                if not target:
                    continue

                target.sort(key=lambda item: (item[0], item[2]))
                kill.add(tuple(target[0][1:]))

        for y, x in kill:
            new_board[y][x] = 0
        count += len(kill)

        move = []
        for y in range(n-1):
            for x in range(m):
                if new_board[y][x] == 1:
                    move.append((y+1, x))

        temp = [[0] * m for _ in range(n)]
        for y, x in move:
            temp[y][x] = 1

        for y in range(n):
            for x in range(m):
                new_board[y][x] = temp[y][x]

        if sum(map(sum, new_board[:-1])) == 0:
            break

    return count

def brute(count, idx):
    if count == 3:
        global answer
        answer = max(simulate(), answer)
    else:
        for x in range(idx, m):
            board[n][x] = 2
            brute(count+1, x+1)
            board[n][x] = 0


n, m, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
board.append([0] * m)
answer = 0

brute(0, 0)
print(answer)