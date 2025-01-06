import sys
input = sys.stdin.readline
    
def solve():
    n, m = map(int, input().split())
    arr = { x : x for x in range(1, n + 1) }
    for x in range(m):
        s, b = map(int, input().split())
        arr[s] = b
    
    for x in range(1, n + 1):
        print(arr[x])

solve()