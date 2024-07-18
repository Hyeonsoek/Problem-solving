import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def divide(xx, yy, nn):
    if nn == 1:
        return arr[xx][yy]
    
    target = []
    nextnn = nn // 2
    for x in range(2):
        for y in range(2):
            target.append(divide(x * nextnn + xx, y * nextnn + yy, nextnn))
    
    target.sort()
    return target[1]

print(divide(0, 0, n))