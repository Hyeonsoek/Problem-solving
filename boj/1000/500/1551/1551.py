n, k = map(int, input().split())
arr = list(map(int, input().split(',')))

narr = []
for x in range(1, k + 1):
    for xx in range(n-x):
        narr.append(arr[xx + 1] - arr[xx])
    arr = narr[:]
    narr.clear()

print(','.join(map(str, arr)))