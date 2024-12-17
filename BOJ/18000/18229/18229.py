def solve():
    n, m, k = map(int, input().split())
    board = [[*map(int, input().split())] for _ in range(n)]

    result = [0] * n
    for x in range(m):
        for y in range(n):
            result[y] += board[y][x]
            if result[y] >= k:
                print(y+1, x+1)
                return
            
solve()