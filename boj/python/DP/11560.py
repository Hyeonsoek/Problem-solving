import sys
input = sys.stdin.readline
MAX = 21

degree = ((MAX + 2) * (MAX + 1)) // 2

cache = [[], [1, 1]]

for i in range(1, MAX+1):
    length = len(cache[-1])
    
    result = [0] * (length + i + 1)
    for j in range(i + 2):
        for k in range(length):
            result[j + k] += cache[-1][k]
    
    cache.append(result)

t = int(input())
for _ in range(t):
    k, n = map(int, input().split())
    print(cache[k][n])