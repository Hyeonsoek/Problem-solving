# ~ ing

N, M, K = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]

trees = [[[] for _ in range(N)] for _ in range(N)]
for i in range(M):
    x, y, z = map(int,input().split())
    trees[y][x].append(z)

