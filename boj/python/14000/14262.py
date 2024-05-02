import sys
input = sys.stdin.readline

n, m, t = map(int, input().split())
copy = [list(input().rstrip()) for _ in range(n)]

repeat = min(n, m)

count = [{'R':0, 'G':0, 'B':0} for _ in range(repeat + 1)]
board = [['.'] * (m + repeat) for _ in range(n + repeat)]

for r in range(repeat + 1):
    for x in range(n):
        for y in range(m):
            if copy[x][y] != '.':
                board[x+r][y+r] = copy[x][y]
    
    for x in range(n + r):
        for y in range(m + r):
            if board[x][y] != '.':
                count[r][board[x][y]] += 1

if repeat < t:
    init = count[repeat]
    
    for color in "RGB":
        increase = count[repeat][color] - count[repeat-1][color]
        init[color] += increase * (t - repeat - 1)

    print(*init.values(), sep='\n')
else:
    print(*count[t-1].values(), sep='\n')