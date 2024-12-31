import sys
input = sys.stdin.readline

def solve():
    T, X = map(int, input().split())
    N = int(input())

    arr = [0] * T
    for _ in range(N):
        t = int(input())
        for i in map(int, input().split()):
            arr[i-1] += 1

    return 'YES' if arr[X-1] == N else 'NO'

print(solve())