import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = [0, *map(int, input().split())]
    
    for i in range(1, n + 1):
        arr[i] += arr[i-1]
        
    result = -sys.maxsize
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            result = max(result, arr[j] - arr[j - i])
    
    print(result)

for _ in range(int(input())):
    solve()