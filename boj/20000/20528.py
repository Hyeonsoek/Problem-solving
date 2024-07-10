def solve():
    n = int(input())
    arr = input().split()

    start = arr[0][0]
    for x in range(1, n):
        if start != arr[x][0]:
            return 0
    return 1

print(solve())