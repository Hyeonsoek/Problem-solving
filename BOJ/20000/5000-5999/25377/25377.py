ans = 1001
for _ in range(int(input())):
    a, b = map(int, input().split())
    ans = min(1001 if a > b else b, ans)

print(-1 if ans == 1001 else ans)