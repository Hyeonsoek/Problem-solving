n = int(input())
arr = list(map(int, input().split()))

result = arr[0] + arr[-1] + 2 * n
for x in range(n):
    result += 2 * arr[x]
    
for x in range(1, n):
    result += abs(arr[x] - arr[x-1])
    
print(result)