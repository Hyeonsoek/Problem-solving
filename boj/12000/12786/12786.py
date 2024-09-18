def solve():
    n = int(input())
    k = int(input())
    
    board = [[1] * 21 for _ in range(n + 1)]
    board[0][1] = 0
    for x in range(1, n + 1):
        kk, *pos = map(int, input().split())
        for i in range(kk):
            board[x][pos[i]] = 0
    
    cache = [[0] * 21] + [[200] * 21 for _ in range(n)]
    
    for x in range(n):
        for h in range(1, 2 if x == 0 else 21):
            for nh in range(1, 21):
                if not board[x][h] and not board[x+1][nh]:
                    value = 1 - (abs(nh - h) <= 1 or min(h * 2, 20) == nh)
                    cache[x + 1][nh] = min(cache[x + 1][nh], cache[x][h] + value)
    
    result = min(cache[n])
    print(result if result <= k else -1)
    
solve()