def solve():
    n = 2 ** int(input())
    sx, sy = map(int, input().split())
    board = [[-1] * n for _ in range(n)]
    
    index = [1]
    def divide(xx, yy, k, bx, by):
        if k == 2:
            for x in range(k):
                for y in range(k):
                    if bx == x + xx and by == y + yy:
                        continue
                    board[xx + x][yy + y] = index[0]
            index[0] += 1
            return
        
        
        kk = k // 2
        ssx, ssy = xx, yy
        eex = xx + kk
        eey = yy + kk
        pos = [[0, 0], [0, 0]]
        for x in range(2):
            for y in range(2):
                if ssx + x * kk <= bx < eex + x * kk and\
                    ssy + y * kk <= by < eey + y * kk:
                    pos[x][y] = [bx, by]
                    continue
                tx = eex - 1 + x
                ty = eey - 1 + y
                pos[x][y] = [tx, ty]
                board[tx][ty] = index[0]
                
        index[0] += 1
    
        for x in range(2):
            for y in range(2):
                tx, ty = pos[x][y]
                divide(xx + kk * x, yy + kk * y, kk, tx, ty)
    
    divide(0, 0, n, sx - 1, sy - 1)
    
    board = list(zip(*board))
    
    for x in reversed(range(n)):
        print(*board[x])
        
solve()