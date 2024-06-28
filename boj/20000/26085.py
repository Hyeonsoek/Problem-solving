def solve():
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    count = [0, 0]
    for x in range(n):
        for y in range(m):
            count[board[x][y]] += 1

    if count[0] & 1 or count[1] & 1:
        return -1

    for x in range(n):
        for y in range(m):
            for xd, yd in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                xx = x + xd
                yy = y + yd
                if 0 <= xx < n and 0 <= yy < m and board[xx][yy] == board[x][y]:
                    return 1
    
    return -1

print(solve())

# 3 4
# 1 0 1 0
# 0 1 0 1
# 1 0 1 0
# -1