import sys
input = sys.stdin.readline

n, t = map(int, input().split())

times = []
scores = []

for x in range(n):
    time, score = map(int, input().split())
    times.append(time)
    scores.append(score)

cache = [[0] * (t + 1) for _ in range(n + 1)]

for x in range(n):
    for time in range(1, t + 1):
        if times[x] <= time:
            left = cache[x][time - times[x]] + scores[x]
            right = cache[x][time]
            cache[x + 1][time] = max(left, right)
        else:
            cache[x + 1][time] = cache[x][time]
            
print(cache[n][t])