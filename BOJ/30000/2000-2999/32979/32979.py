def solve():
    n = int(input())
    t = int(input())
    arr = [*map(int, input().split())]
    
    i = 0
    result = []
    for j in map(int, input().split()):
        i = (i + j - 1) % (2 * n)
        result.append(arr[i])
    
    print(*result)

solve()