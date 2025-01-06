import sys
input = sys.stdin.readline
direc = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def solve():
    r, c, t = map(int, input().split())
    board = [list(input().strip()) for _ in range(r)]
    
    sx, sy = 0, 0
    for x in range(r):
        for y in range(c):
            if board[x][y] == 'G':
                sx, sy = x, y
    
    def brute(nx, ny, dist, count):
        if dist == t:
            return count

        result = 0
        for dx, dy in direc:
            xx = nx + dx
            yy = ny + dy
            if 0 <= xx < r and 0 <= yy < c and board[xx][yy] != '#':
                value, board[xx][yy] = board[xx][yy], '.'
                result = max(result, brute(xx, yy, dist + 1, count + (value == 'S')))
                board[xx][yy] = value
        return result
    
    print(brute(sx, sy, 0, 0))
    
solve()