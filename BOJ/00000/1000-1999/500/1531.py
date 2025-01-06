n, m = map(int, input().split())
board = [[0] * 101 for _ in range(101)]

for x in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    for yy in range(y1, y2+1):
        for xx in range(x1, x2+1):
            board[yy][xx] += 1

result = 0
for y in range(1, 101):
    for x in range(1, 101):
        if board[y][x] > m:
            result += 1

print(result)