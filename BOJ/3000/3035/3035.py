r, c, zr, zc = map(int, input().split())
board = [[*input()] for _ in range(r)]

result = [['' for _ in range(c * zc)] for _ in range(r * zr)]
for x in range(r):
    for y in range(c):
        for xx in range(x * zr, (x+1) * zr):
            for yy in range(y * zc, (y+1) * zc):
                result[xx][yy] = board[x][y]

print(*map(lambda x: ''.join(x), result), sep='\n')