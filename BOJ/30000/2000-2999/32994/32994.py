VALUE = [1, 2, 3, 4, 5]

def solve():
    n, m = map(int, input().split())
    board = [[0] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            board[i][j] = VALUE[(i * 2 + j) % 5]
    
    for i in range(n):
        print(*board[i])

solve()