from collections import defaultdict

n = int(input())
m = int(input())
cache = [[0] * (x + 3) for x in range(n)]
cache[0][1] = 1

must = defaultdict(set)
for _ in range(m):
    a, b = map(int, input().split())
    must[a].add(b+1)

for row in range(1, n):
    isRow = row in must
    for column in range(1, row + 2):
        if isRow and column not in must[row]:
            continue
        
        cache[row][column] = cache[row-1][column-1] + cache[row-1][column]

print(sum(cache[-1]))