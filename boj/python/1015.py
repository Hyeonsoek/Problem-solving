n = int(input())
a = list(map(int, input().split()))
b = sorted(a)

c = []
v = [True] * n
for x in range(n):
    for y in range(n):
        if a[x] == b[y] and v[y]:
            c.append(y)
            v[y] = False
            break
print(*c)