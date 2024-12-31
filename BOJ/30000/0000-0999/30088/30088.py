import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = []
    for x in range(n):
        count, *times = map(int, input().split())
        arr.append(sum(times))
    
    arr.sort()
    for x in range(n):
        arr[x] *= n - x
    
    print(sum(arr))
    
solve()