a, b, n, k = map(int, input().split())
r, m = divmod(k - 1, b * n)
print(r + 1, m // n + 1)