n, k = map(int, input().split())
arr = list(map(int, input().split()))

result = []
for x in arr:
    if x % k == 0:
        result.append(x // k)

print(*sorted(result))