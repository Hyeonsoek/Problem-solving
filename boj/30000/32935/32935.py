import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = sorted([*map(int, input().split())])
    
    s = -sum(arr)
    for i in range(n):
        if arr[i] < s:
            k = s
            s += (arr[i] - s)
            arr[i] = k
    
    print(-s)

solve()