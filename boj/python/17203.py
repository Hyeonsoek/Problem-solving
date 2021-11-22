from sys import stdin

n, m = map(int, input().split())
array = list(map(int, input().split()))
prefix = [0] * n

for i in range(1, n):
    prefix[i] = prefix[i-1] + abs(array[i] - array[i-1])

for _ in range(m):
    i, j = map(int, stdin.readline().split())

    if j - 1 < i:
        print(0)
    else:
        print(prefix[j-1] - prefix[i-1])