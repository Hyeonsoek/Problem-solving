n = int(input())
arr = [0] * 51

for x in map(int, input().split()):
    arr[x] += 1

result = -1
for x in range(51):
    if arr[x] == x:
        result = max(result, x)

print(result)