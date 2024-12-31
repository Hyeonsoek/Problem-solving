import sys
input = sys.stdin.readline

def solve():
    n, h = map(int, input().split())
    arr = sorted(list(map(int, input().split())))
    
    for x in range(n):
        h -= arr[x]
        if h <= 0:
            return x + 1
    
    return -1

print(solve())