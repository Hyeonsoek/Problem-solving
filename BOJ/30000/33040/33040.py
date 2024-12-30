def solve():
    h, w = map(int, input().split())
    c, d = map(int, input().split())
    
    if h - 1 > w:
        print(-1)
        return
    
    minvalue = h * (h - 1) // 2
    maxvalue = h * w - minvalue
    
    if not (minvalue <= d <= maxvalue):
        print(-1)
        return
    
    board = [[1] * w for _ in range(h)]
    
    for i in range(h):
        for j in range(i):
            board[i][j] = 9
            d -= 1
    
    i = 0
    while d > 0 and i < h:
        j = w - 1 - i
        while d > 0 and j >= 0:
            if board[h - 1 - i][j] == 1:
                board[h - 1 - i][j] = 9
                d -= 1
            j -= 1
        i += 1

    for i in range(h):
        print(*board[i])

solve()