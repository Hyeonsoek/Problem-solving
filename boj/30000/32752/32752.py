import sys
input = sys.stdin.readline

def solve():
    N, L, R = map(int, input().split())
    arr = [*map(int, input().split())]    
    arr = arr[:L-1] + sorted(arr[L-1:R]) + arr[R:]

    for i in range(1, N):
        if arr[i - 1] > arr[i]:
            return 0
    return 1

print(solve())