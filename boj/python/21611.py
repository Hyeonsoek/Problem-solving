from sys import stdin

dirr = [[-1, 0], [1, 0], [0, -1], [0, 1]]
next_d = {3: 2, 2: 4, 4: 1, 1: 3}

def blizzard(d, s):
    global board, n, m

    answer = 0
    sy, sx = n//2, n//2
    for _ in range(s):
        sy += dirr[d-1][0]
        sx += dirr[d-1][1]


input_test = lambda: map(int, stdin.readline().split())

n, m = input_test()
board = [list(input_test()) for _ in range(n)]
simulate = [list(input_test()) for _ in range(m)]

result = 0
for di, si in simulate[:1]:
    result += blizzard(di, si)