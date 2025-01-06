u = [*map(int, input().split())]
d = [*map(int, input().split())]

result = False
uu = dd = 0
for x in range(9):
    uu += u[x]
    result |= uu > dd
    dd += d[x]
    result |= uu > dd

print("Yes" if result else "No")