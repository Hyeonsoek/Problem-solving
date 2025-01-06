r, c, n = map(int, input().split())
board = [list(input()) for _ in range(r)]

if n % 2 == 0:
    for y in range(r):
        print('O' * c)
    exit()

sec = 0
dirr = [[-1, 0], [1, 0], [0, -1], [0, 1]]

while sec < n-1:
    bomb = []
    for i in range(r):
        for j in range(c):
            if board[i][j] == '.':
                board[i][j] = 'O'
            else:
                bomb.append([i, j])

    sec += 1
    if sec >= n-1:
        break

    for y, x in bomb:
        board[y][x] = '.'
        for ydir, xdir in dirr:
            yy = y + ydir
            xx = x + xdir
            if 0 <= yy < r and 0 <= xx < c and board[yy][xx] == 'O':
                board[yy][xx] = '.'

    sec += 1

for y in board:
    print(''.join(y))