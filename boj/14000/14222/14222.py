def solve():
    n, k = map(int, input().split())
    arr = [*map(int, input().split())]

    for x in range(n):
        if x + 1 < arr[x]:
            return 0
    
        if (arr[x] - x - 1) % k != 0:
            return 0
    
    return 1

print(solve())