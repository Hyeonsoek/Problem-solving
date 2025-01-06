R, C, W = map(int, input().split())

cache = [[0] * (x + 1) for x in range(32)]
cache[0][0] = 1

for x in range(31):
    for y in range(x + 1):
        cache[x+1][y]   += cache[x][y]
        cache[x+1][y+1] += cache[x][y]

result = 0
for x in range(R - 1, R + W - 1):
    for y in range(C - 1, C + (x - R) + 1):
        result += cache[x][y]
        
print(result)