import sys
input = sys.stdin.readline

def solve():
    n, m, k = map(int, input().split())
    floor = 0
    result = -1
    for x in range(m):
        ti, ri = map(int, input().split())
        if result == -1:
            floor += ri
            if floor > k:
                result = f'{x+1} {1}'
    
    return result

print(solve())