import sys
input = sys.stdin.readline
output = sys.stdout.write

dirr = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

def solve():
    n = int(input())
    board = [ list(input().strip()) for _ in range(n) ]
    convert = [ [0] * n for _ in range(n) ]

    for x in range(n):
        for y in range(n):
            if board[x][y] != '.':
                convert[x][y] = -1
                for xd, yd in dirr:
                    xx = xd + x
                    yy = yd + y
                    if 0 <= xx < n and 0 <= yy < n and board[xx][yy] == '.':
                        convert[xx][yy] += int(board[x][y])

    for x in range(n):
        line = ''
        for y in range(n):
            if convert[x][y] == -1:
                line += '*'
            elif convert[x][y] >= 10:
                line += 'M'
            else:
                line += str(convert[x][y])
        output(line + '\n')
        
solve()