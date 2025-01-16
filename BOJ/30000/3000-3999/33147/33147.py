import sys, math
input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())
    arr = [*map(int, input().split())]

    gcd = math.gcd(n, k)

    for i in range(n):
        if (arr[i] - i) % gcd:
            return 'NO'
    return 'YES'

print(solve())