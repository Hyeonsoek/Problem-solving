n = int(input())
board = [[0] * 100 for _ in range(100)]

for x in range(n):
    sx, sy = map(int, input().split())
    for xx in range(sx, sx + 10):
        for yy in range(sy, sy + 10):
            board[xx][yy] = 1

result = 0
for x in range(100):
    y = 0
    while y < 100:
        while y < 100 and board[x][y] == 0:
            y += 1
            
        if y == 100:
            break
        
        while y < 100 and board[x][y] == 1:
            y += 1
            
        result += 2
    
    y = 0
    while y < 100:
        while y < 100 and board[y][x] == 0:
            y += 1
            
        if y == 100:
            break
        
        while y < 100 and board[y][x] == 1:
            y += 1
    
        result += 2
            
print(result)