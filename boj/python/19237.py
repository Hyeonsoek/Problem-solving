n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
shark = list(map(int, input().split()))

priority = [[list(map(int, input().split())) for _ in range(4)] for _ in range(m)]

def simulate():
    global n, m, k, board, shark, shark_pos

    for key in range(1, m+1):
        if key in shark_pos:



shark_pos = {}

for y in range(n):
    for x in range(n):
        if board[y][x] > 0:
            shark_pos[board[y][x]] = (y, x)

for i in range(1000):
    simulate()
    if len(shark_pos) == 1:
        print(i+1)

print(-1)