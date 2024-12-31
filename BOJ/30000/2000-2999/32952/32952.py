r, k, m = map(int, input().split())

i = 1
while i * k <= m and r >= 1:
    i += 1
    r //= 2

print(r)