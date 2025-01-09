n = int(input())
arr = sorted(map(int, input().split()), reverse=True)

result = 0
for x in range(n):
    result += abs(arr[x-1] - arr[x])

print(result)