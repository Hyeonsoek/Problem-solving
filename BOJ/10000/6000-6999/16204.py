n, m, k = map(int, input().split())
front = "O" * m + "X" * (n - m)
back = "O" * k + "X" * (n - k)

count = 0
for x in range(n):
    count += front[x] == back[x]

print(count)