import sys
input = sys.stdin.readline

def solve():
    N, X = map(int, input().split())
    arr = [0, *map(int, input().split())]
    
    for i in range(1, N + 1):
        arr[i] += arr[i-1]
    
    result = 0
    for i in range(X, N + 1):
        result = max(result, arr[i] - arr[i - X])
    
    count = 0
    for i in range(X, N + 1):
        count += result == (arr[i] - arr[i - X])
    
    if result:
        print(result, count, sep='\n')
    else:
        print('SAD')

solve()