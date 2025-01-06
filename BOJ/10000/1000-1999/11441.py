from sys import stdin

n = int(input())
array = list(map(int, input().split()))
prefix = [0] * n
prefix[0] = array[0]

for i in range(1, n):
    prefix[i] = prefix[i-1] + array[i]
prefix.insert(0, 0)

m = int(input())
for _ in range(m):
    i, j = map(int, stdin.readline().split())

    print(prefix[j] - prefix[i-1])