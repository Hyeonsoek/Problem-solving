i=lambda: map(int, input().split())
r, c = i()
a, b = i()

board = [[''] * b * c for _ in range(r * a)]

for x in range(r):
    for y in range(c):
        for xx in range(a):
            for yy in range(b):
                board[x * a + xx][y * b + yy] = '.' if (x + y) & 1 else 'X'

for x in board:
    print(''.join(x))