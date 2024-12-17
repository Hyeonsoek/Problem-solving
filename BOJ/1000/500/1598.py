n, m = map(int, input().split())
print(abs((n - 1) % 4 - (m - 1) % 4) + abs((n - 1) // 4 - (m - 1) // 4))