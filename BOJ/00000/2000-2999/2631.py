from bisect import bisect_left

n = int(input())
arr = [int(input()) for _ in range(n)]

result = []
for x in range(n):
    if not result or result[-1] < arr[x]:
        result.append(arr[x])
    else:
        result[bisect_left(result, arr[x])] = arr[x]

print(n - len(result))