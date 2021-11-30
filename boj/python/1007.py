from sys import stdin
from math import sqrt
from itertools import combinations

MAX = 987654321

T = int(input())

for _ in range(T):
    N = int(stdin.readline())

    vector = []

    for _ in range(N):
        vector.append(tuple(map(int, stdin.readline().split())))

    answer = MAX
    target = list(combinations([x for x in range(N)], N//2))

    for start in target:
        yy, xx = 0, 0
        for idx in start:
            y, x = vector[idx]
            yy += y
            xx += x

        for i in range(N):
            if i not in start:
                y, x = vector[i]
                yy -= y
                xx -= x

        answer = min(answer, sqrt(yy ** 2 + xx ** 2))

    print(answer)