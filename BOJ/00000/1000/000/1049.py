n, m = map(int, input().split())

mina, minb = 1000, 1000
for _ in range(m):
    a, b = map(int, input().split())
    mina = min(mina, a)
    minb = min(minb, b)

result = 1000000000
for x in range(n // 6 + 2):
    count = max(n - x * 6, 0)
    result = min(result, x * mina + count * minb)
    
print(result)