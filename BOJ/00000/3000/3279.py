n = int(input())
arr = [int(input()) for _ in range(n)]

x = 0
result = 100
while x != n - 1:
    while x < n - 1 and arr[x] <= arr[x+1]:
        x += 1

    high = x

    while x < n - 1 and arr[x] >= arr[x+1]:
        x += 1

    low = x

    result *= arr[high] / arr[low]

print(result)