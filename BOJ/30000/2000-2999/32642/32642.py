import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = [*map(lambda x: 1 if int(x) else -1, input().split())]
    
    for x in range(1, n):
        arr[x] += arr[x-1]
    
    print(sum(arr))

solve()