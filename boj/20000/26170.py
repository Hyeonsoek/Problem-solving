dirr = [[-1, 0], [1, 0], [0, -1], [0, 1]]

board = [list(map(int, input().split())) for _ in range(5)]
sx, sy = map(int, input().split())

visited = [[0] * 5 for _ in range(5)]
visited[sx][sy] = 1

MAX = 300

def dfs(nx, ny, count, dist):
    if count == 3:
        return dist
    else:
        result = MAX
        for dx, dy in dirr:
            xx = dx + nx
            yy = dy + ny
            if 0 <= xx < 5 and 0 <= yy < 5 and\
                    board[xx][yy] != -1 and not visited[xx][yy]:
                visited[xx][yy] = 1
                result = min(result, dfs(xx, yy, count + board[xx][yy], dist + 1))
                visited[xx][yy] = 0
        return result

result = dfs(sx, sy, board[sx][sy], 0)
print(-1 if result == MAX else result)