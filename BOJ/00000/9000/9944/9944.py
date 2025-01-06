import sys
MAX = 100000000
DRX = [-1, 1, 0, 0]
DRY = [0, 0, -1, 1]
input = map(str, sys.stdin.read().split())

def solve():
    n = int(next(input))
    m = int(next(input))
    board = [list(next(input)) for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    
    count = 0
    for i in range(n):
        for j in range(m):
            count += 1 if board[i][j] == '.' else 0
    
    if count == 1:
        return 0
    
    def isinner(xx, yy):
        return 0 <= xx < n and 0 <= yy < m

    def brute(xx, yy, dd, count):
        if count == 0:
            return 0
        
        nx = xx
        ny = yy
        pos = []
        while isinner(nx, ny) and not visited[nx][ny] and board[nx][ny] != '*':
            pos.append((nx, ny))
            nx += DRX[dd]
            ny += DRY[dd]

        nx -= DRX[dd]
        ny -= DRY[dd]
        
        for x, y in pos:
            count -= 1
            visited[x][y] = 1
    
        result = MAX
        if count > 0:
            for d in range(4):
                sx = nx + DRX[d]
                sy = ny + DRY[d]
                if isinner(sx, sy) and not visited[sx][sy] and board[sx][sy] != '*':
                    result = min(result, 1 + brute(sx, sy, d, count))
        else:
            result = 1
            
        for x, y in pos:
            visited[x][y] = 0
        
        return result
    
    result = MAX
    for i in range(n):
        for j in range(m):
            if board[i][j] == '.':
                for d in range(4):
                    result = min(result, brute(i, j, d, count))
    
    return result if result != MAX else -1

index = 1
while True:
    try:
        print(f'Case {index}: {solve()}')
        index += 1
    except StopIteration:
        break