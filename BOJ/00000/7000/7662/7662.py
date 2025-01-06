import sys
from heapq import *
input = sys.stdin.readline
output = sys.stdout.write

def solve():
    n = int(input())
    queueMin = []
    queueMax = []
    deleted = [False] * n
    for i in range(n):
        q, value = input().split()
        value = int(value)

        if q == 'I':
            heappush(queueMin, (value, i))
            heappush(queueMax, (-value, i))
        else:
            if value == 1:
                while queueMax:
                    maxValue, index = heappop(queueMax)
                    if deleted[index] == False:
                        deleted[index] = True
                        break
            else:
                while queueMin:
                    minValue, index = heappop(queueMin)
                    if deleted[index] == False:
                        deleted[index] = True
                        break

    minValue = sys.maxsize
    maxValue = -sys.maxsize

    while queueMax:
        mv, index = heappop(queueMax)
        if deleted[index] == False:
            maxValue = mv
            break

    while queueMin:
        mv, index = heappop(queueMin)
        if deleted[index] == False:
            minValue = mv
            break
    
    if minValue != sys.maxsize and maxValue != -sys.maxsize:
        output(f'{-maxValue} {minValue}\n')
    else:
        output('EMPTY\n')

for _ in range(int(input())):
    solve()