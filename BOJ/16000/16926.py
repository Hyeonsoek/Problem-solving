n, m, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

count = min(n, m) // 2
for x in range(count):
    sx, sy = x, x
    line = []
    
    for t in range(m-x*2-1):
        line.append((board[sx][sy], sx, sy))
        sy += 1

    for t in range(n-x*2-1):
        line.append((board[sx][sy], sx, sy))
        sx += 1
    
    for t in range(m-x*2-1):
        line.append((board[sx][sy], sx, sy))
        sy -= 1
    
    for t in range(n-x*2-1):
        line.append((board[sx][sy], sx, sy))
        sx -= 1
    
    length = len(line)
    for x in range(length):
        ov, ox, oy = line[x]
        tv, tx, ty = line[(x - r) % length]   
        
        board[tx][ty] = ov

for x in board:
    print(*x)