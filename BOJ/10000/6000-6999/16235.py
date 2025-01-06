#"각각의"만 읽었어도 더 빨리 풀었을 텐데 ㅂㄷㅂㄷ

import sys

N, M, K = map(int, input().split())

soil = [[5] * N for _ in range(N)]
add_food = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
trees = [[[] for _ in range(N)] for _ in range(N)]

dirr = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

for i in range(M):
    x, y, z = map(int, sys.stdin.readline().split())
    trees[x-1][y-1].append(z)

for i in range(N):
    for j in range(N):
        trees[i][j] = sorted(trees[i][j])

for _ in range(K):

    # spring - summer
    for i in range(N):
        for j in range(N):
            for k in range(len(trees[i][j])):
                if soil[i][j] >= trees[i][j][k]:
                    soil[i][j] -= trees[i][j][k]
                    trees[i][j][k] += 1
                else:
                    for kk in range(k, len(trees[i][j])):
                        soil[i][j] += trees[i][j][kk] // 2
                    del trees[i][j][k:len(trees[i][j])]
                    break

    # fall - winter
    for i in range(N):
        for j in range(N):
            for k in range(len(trees[i][j])):
                if trees[i][j][k] % 5 == 0:
                    for ydir, xdir in dirr:
                        xx = i + ydir
                        yy = j + xdir
                        if (0 <= yy < N) and (0 <= xx < N):
                            trees[xx][yy].insert(0, 1)
            soil[i][j] += add_food[i][j]

answer = 0
for i in range(N):
    for j in range(N):
        answer += len(trees[i][j])

print(answer)