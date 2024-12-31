n = int(input())
arr = [*map(int, input().split())]
print((n - 1) * 180 - sum(arr) * 2)