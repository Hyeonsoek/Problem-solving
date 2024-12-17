n = int(input())
arr = [int(input()) for _ in range(n)][::-1]

result = 0
while n - 1 != arr.index(max(arr)):
    arr[arr.index(max(arr))] -= 1
    arr[-1] += 1
    result += 1

print(result)