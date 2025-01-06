DRX = [-1, 1, 0, 0]
DRY = [0, 0, -1, 1]

r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]
visited = [[0] * c for _ in range(r)]

def dfs(xx, yy):
    for d in range(4):
        nx = xx + DRX[d]
        ny = yy + DRY[d]
        if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny] and board[nx][ny] == '#':
            visited[nx][ny] = 1
            dfs(nx, ny)

result = 0
for i in range(r):
    for j in range(c):
        if board[i][j] == '#' and not visited[i][j]:
            dfs(i, j)
            result += 1

print(result)