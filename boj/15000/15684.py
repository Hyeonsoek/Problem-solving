import sys

n, m, h = map(int, input().split())
board = [[0] * (n+1) for _ in range(h)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    board[a-1][b] = 1

candidates = []
for r in range(h):
    for c in range(1, n):
        if board[r][c-1] == board[r][c] == board[r][c+1] \
                and board[r][c] == 0:
            candidates.append((r, c))

def check():
    for i in range(1, n+1):
        end = line_end(i)
        if end != i:
            return False
    return True

def line_end(i):
    start = i
    for j in range(h):
        if board[j][start]:
            start += 1
        elif board[j][start - 1]:
            start -= 1
    return start

def brute_force(idx, count):
    global answer

    if count >= answer:
        return

    if check():
        answer = count
        return

    for ii in range(idx, len(candidates)):
        i, j = candidates[ii]
        if board[i][j-1] == board[i][j] == board[i][j+1] == 0:
            board[i][j] = 1
            brute_force(ii+1, count+1)
            board[i][j] = 0

answer = 4
brute_force(0, 0)
print(answer if answer < 4 else -1)