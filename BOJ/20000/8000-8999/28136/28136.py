import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    result = 0
    for x in range(n):
        if arr[x - 1] >= arr[x]:
            result += 1
        
    print(result)

solve()