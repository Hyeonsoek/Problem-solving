DRX = [-1, 1, 0, 0]
DRY = [0, 0, -1, 1]

def solve():
    n, m = map(int, input().split())
    board = [[*map(int, input().split())] for _ in range(n)]
    
    result = n * m * 2
    for x in range(n):
        for y in range(m):
            result += board[x][y] * 4
            for d in range(4):
                dx = x + DRX[d]
                dy = y + DRY[d]
                if 0 <= dx < n and 0 <= dy < m:
                    result -= min(board[x][y], board[dx][dy])
    
    print(result)

solve()