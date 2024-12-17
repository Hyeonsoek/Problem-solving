def solve():
    n = int(input()) + 1
    board = [[0] * n]
    board += [[0] + list(map(int, input().split())) for _ in range(n-1)]
    xx, yy = map(int, input().split())
    
    def dynamic():
        cache = [[0] * n for _ in range(n)]
        for x in range(1, xx + 1):
            for y in range(1, yy + 1):
                cache[x][y] = board[x][y] + max(cache[x][y-1], cache[x-1][y])
        
        for x in range(xx, n):
            for y in range(yy, n):
                cache[x][y] = board[x][y] + max(cache[x][y-1], cache[x-1][y])
        
        return cache[n-1][n-1]
    
    def dynamic_r():
        cache = [[0] * n for _ in range(n)]
        
        for y in range(1, n):
            if xx == 1 and yy == y:
                break
            cache[1][y] = board[1][y] + cache[1][y-1]
        
        for x in range(1, n):
            if xx == x and yy == 1:
                break
            cache[x][1] = board[x][1] + cache[x-1][1]
        
        for x in range(2, n):
            for y in range(2, n):
                if x == xx and y == yy:
                    continue
                cache[x][y] = board[x][y] + max(cache[x-1][y], cache[x][y-1])
        
        return cache[n-1][n-1]
    
    print(dynamic(), dynamic_r())
    
solve()