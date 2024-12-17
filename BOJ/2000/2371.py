n = int(input())
files = [list(map(int, input().split()))[:-1] for _ in range(n)]
maxlen = max(map(len, files))

for x in range(n):
    while len(files[x]) < maxlen:
        files[x].append(0)

    for y in range(1, maxlen):
        files[x][y] += files[x][y-1]

for x in range(maxlen):
    counts = set([ files[y][x] for y in range(n) ])
    if len(counts) == n:
        print(x + 1)
        break