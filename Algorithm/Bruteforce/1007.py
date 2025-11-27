import sys
from itertools import combinations
input = sys.stdin.readline

MAX = 987654321

def solve():
    T = int(input())

    for _ in range(T):
        N = int(input())

        answer = MAX
        vector = [tuple(map(int, input().split())) for _ in range(N)]
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

            answer = min(answer, (yy ** 2 + xx ** 2) ** .5)

        print(answer)

solve()