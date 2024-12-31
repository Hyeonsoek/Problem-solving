import sys
from bisect import *
from collections import *
input = sys.stdin.readline

def solve():
    N, Q = map(int, input().split())
    T = [*map(int, input().split())]
    S = [*map(int, input().split())]

    classify = defaultdict(list)
    for i in range(N):
        classify[S[i]].append(T[i])
        
    maxT = max(T)
    minT = min(T)
    maxS = max(S)

    for i in classify.keys():
        classify[i].sort()

    sortedTS = sorted(zip(T, S))
    sortedT, sortedS = list(zip(*sortedTS))

    maxValueS = [0] * N
    maxValueS[N-1] = sortedS[N-1]
    for i in reversed(range(N-1)):
        maxValueS[i] = max(maxValueS[i+1], sortedS[i])

    result = []
    for _ in range(Q):
        P = int(input())
        if minT <= P <= maxT:
            size = maxValueS[bisect_left(sortedT, P)]
            value = len(classify[size]) - bisect_left(classify[size], P)
            result.append(value)
        else:
            if P < minT:
                result.append(len(classify[maxS]))
            else:
                result.append(0)

    print(*result, sep='\n')

solve()