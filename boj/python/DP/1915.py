n, m = map(int, input().split())
board = [ [*map(int, list(input()))] for _ in range(n) ]

for x in range(1, n):
    for y in range(1, m):
        if board[x][y] >= 1:
            board[x][y] += min(board[x][y-1], board[x-1][y], board[x-1][y-1])
            
result = max(map(max, board))
print(result * result)