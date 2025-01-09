n, m = map(int, input().split())
arr = list(map(int, input().split()))
friend = set(map(int, input().split()))

result = 0
for x in range(n):
    if arr[x] in friend and x >= m:
        result += 1

print(result)