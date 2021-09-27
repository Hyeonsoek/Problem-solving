from sys import stdin

n, m = map(int, stdin.readline().split())
board = [[0] * (n+1) for _ in range(n+1)]

for i in range(n):
    number = list(map(int, stdin.readline().split()))
    for j in range(n):
        board[i+1][j+1] = board[i+1][j] + board[i][j+1] - board[i][j] + number[j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, stdin.readline().split())
    print(board[x2][y2]-board[x1-1][y2]-board[x2][y1-1]+board[x1-1][y1-1])