import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = sorted([*map(int, input().split())], reverse=True)
    
    result = -1
    for x in range(n):
        if arr[x]:
            result = min(n - 1, max(result, x + arr[x] - 1))
    
    print(result + 1)

solve()