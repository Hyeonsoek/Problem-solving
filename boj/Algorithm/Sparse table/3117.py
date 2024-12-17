import sys
input = sys.stdin.readline
MAX_POW = 30

n, k, m = map(int, input().split())
starts = list(map(int, input().split()))
sparses = [ [0 for _ in range(MAX_POW)] for _ in range(k + 1) ]

for idx, x in enumerate(map(int, input().split())):
    sparses[idx + 1][0] = x

for pow in range(1, MAX_POW):
    for number in range(1, k + 1):
        sparses[number][pow] = sparses[ sparses[number][pow - 1] ][pow - 1]

answer = []
for x in starts:
    count = m - 1
    for pow in range(MAX_POW, -1, -1):
        if count >= (1 << pow):
            count -= (1 << pow)
            x = sparses[x][pow]
    answer.append(x)

print(*answer)