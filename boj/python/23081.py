n = int(input())
board = [list(input()) for _ in range(n)]

loc = [-1, -1]
answer = 0
dir_ = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, 1], [1, 1], [1, -1], [-1, -1]]

for y in range(n):
    for x in range(n):
        if board[y][x] == '.':
            count = 0
            for yd, xd in dir_:
                yy = y + yd
                xx = x + xd
                white = 0
                while 0 <= yy < n and 0 <= xx < n:
                    if board[yy][xx] == '.':
                        break
                    if board[yy][xx] == 'B':
                        count += white
                        break
                    if board[yy][xx] == 'W':
                        white += 1
                        yy += yd
                        xx += xd

            if answer < count:
                answer = count
                loc = [x, y]

if loc != [-1, -1]:
    print(*loc)
    print(answer)
else:
    print("PASS")