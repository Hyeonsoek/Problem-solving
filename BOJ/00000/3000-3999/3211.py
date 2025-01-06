def solve():
    n = int(input())
    arr = sorted([int(input()) for _ in range(n)])
    
    result = 1
    while arr[result - 1] + 1 > result:
        result = arr[result - 1] + 1
    
    print(result)
    
solve()