drx = [-1, 1, 0, 0]
dry = [0, 0, -1, 1]

def solve():
    n, m = map(int, input().split())
    board = [list(input()) for _ in range(n)]
    visited = [[0] * m for _ in range(n)]

    def dfs(xx, yy, depth):
        ret = False
        for x in range(4):
            nx = drx[x] + xx
            ny = dry[x] + yy
            
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == board[xx][yy]:
                if visited[nx][ny]:
                    if visited[xx][yy] >= 3 + visited[nx][ny]:
                        return True
                else:
                    visited[nx][ny] = depth
                    ret |= dfs(nx, ny, depth + 1)
                    if ret:
                        return ret
        
        return ret

    for x in range(n):
        for y in range(m):
            if dfs(x, y, 1):
                print("Yes")
                return
                
    print("No")

solve()