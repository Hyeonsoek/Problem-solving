import sys
from heapq import *
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    score = [*map(int, input().split())]
    inc = [*map(int, input().split())]
    
    stamp = [0] * 101
    for x in range(m):
        xx, yy = divmod(100 - score[x], inc[x])
        stamp[inc[x]] += xx
        stamp[yy] += 1

    result = sum(score)
    time = 24 * n
    for x in reversed(range(101)):
        if time >= stamp[x]:
            result += x * stamp[x]
            time -= stamp[x]
        else:
            result += x * time
            break
        
    print(result)
    
    # data = []
    # for x in range(m):
    #     heappush(data, (-inc[x], score[x] - 100))
    
    # result = sum(score)
    # time = 24 * n
    # while data and time > 0:
    #     i, s = heappop(data)
    #     i, s = -i, -s
    #     if s >= i:
    #         result += i
    #         heappush(data, (-i, i - s))
    #         time -= 1
    #     else:
    #         heappush(data, (-s, -s))

    # print(result)
    
solve()