l, r, x = map(int, input().split())

s = set()
for i in range(l, r + 1):
    s.add((i | x))

print(min(set(range(10000)) - s))