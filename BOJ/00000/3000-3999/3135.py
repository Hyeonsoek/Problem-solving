a, b = map(int, input().split())
result = abs(a - b)
n = int(input())
for _ in range(n):
    result = min(result, abs(b - int(input())) + 1)

print(result)