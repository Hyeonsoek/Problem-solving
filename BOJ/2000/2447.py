n = int(input())
board = [ [ 'X' ] * n for _ in range(n) ]

def daq(sx, sy, nn):
    if nn == 3:
        for x in range(sx, sx + 3):
            for y in range(sy, sy + 3):
                board[x][y] = '*'
        midx, midy = sx + 1, sy + 1
        board[midx][midy] = ' '
    else:
        ternary = nn // 3
        for x in range(sx, sx + nn, ternary):
            for y in range(sy, sy + nn, ternary):
                daq(x, y, ternary)
        
        midx, midy = sx + ternary, sy + ternary
        for x in range(midx, midx + ternary):
            for y in range(midy, midy + ternary):
                board[x][y] = ' '

daq(0, 0, n)

for xx in board:
    print(''.join(xx))