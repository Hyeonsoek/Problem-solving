import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = [*map(int, input().split())]
    
    prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix[i] = prefix[i-1] + arr[i-1]
    
    result = 0
    for i in range(1, n):
        result += arr[i] * prefix[i]
    
    print(result)

solve()