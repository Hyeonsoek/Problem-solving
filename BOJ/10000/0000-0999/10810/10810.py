n, m = map(int, input().split())
basket = [0] * n
for _ in range(m):
    a, b, c = map(int, input().split())
    for x in range(a, b + 1):
        basket[x-1] = c
print(*basket)