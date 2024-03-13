n = int(input())
d = {}
for x in range(n):
    s = input()
    if s[0] in d:
        d[s[0]] += 1
    else:
        d[s[0]] = 1

result = []
for x, y in d.items():
    if y >= 5:
        result.append(x)
print(''.join(sorted(result)) if result else "PREDAJA")