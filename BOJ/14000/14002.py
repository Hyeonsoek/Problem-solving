from bisect import *

n = int(input())
arr = list(map(int, input().split()))

seq = []
indexes = [0] * n
for x in range(n):
    if not seq or seq[-1] < arr[x]:
        indexes[x] = len(seq)
        seq.append(arr[x])
    else:
        index = bisect_left(seq, arr[x])
        seq[index] = arr[x]
        indexes[x] = index

print(len(seq))

result = []
count = len(seq) - 1
for x in reversed(range(n)):
    if indexes[x] == count:
        result.append(arr[x])
        count -= 1

print(*reversed(result))