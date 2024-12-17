n, m = map(int, input().split())
if n > 0:
    arr = list(map(int, input().split()))

    count = [0]
    for x in range(n):
        if count[-1] + arr[x] <= m:
            count[-1] += arr[x]
        else:
            count.append(arr[x])

    print(len(count))
else:
    print(0)