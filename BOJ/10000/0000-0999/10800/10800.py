import sys

n = int(input())
balls = []

for i in range(n):
    ci, si = map(int, sys.stdin.readline().split())
    balls.append((si, ci, i))

balls.sort()

j, prefix = 0, 0
answer = [0] * n
color = [0] * (n + 1)

for i in range(n):
    while balls[j][0] < balls[i][0]:
        prefix += balls[j][0]
        color[balls[j][1]] += balls[j][0]
        j += 1

    answer[balls[i][2]] = prefix - color[balls[i][1]]

for ans in answer:
    print(ans)