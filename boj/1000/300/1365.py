from bisect import bisect_left

n = int(input())
arr = list(map(int, input().split()))

count = 0
sequence = []
for x in range(n):
    if not sequence or sequence[-1] < arr[x]:
        sequence.append(arr[x])
    else:
        index = bisect_left(sequence, arr[x])
        sequence[index] = arr[x]
        count += 1

print(count)