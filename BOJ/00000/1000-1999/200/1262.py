from string import ascii_lowercase

n, R1, C1, R2, C2 = map(int, input().split())

length = 2 * n - 1
result = []

for x in range(R1, R2 + 1):
    line = ""
    for y in range(C1, C2 + 1):
        xx = x % length
        yy = y % length
        dist = abs(n - xx - 1) + abs(n - yy - 1)
        line += ascii_lowercase[dist % 26] if dist < n else '.'
    result.append(line)

for x in result:
    print(x)