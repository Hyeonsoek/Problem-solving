s = input()
c = [0] * 10

for q in s:
    c[int(q)] += 1

ss = c[6] + c[9]
if ss % 2 == 0:
    c[6] = c[9] = ss//2
else:
    if c[6] > c[9]:
        c[6] = ss//2 + 1
        c[9] = ss//2
    else:
        c[6] = ss//2
        c[9] = ss//2 + 1

print(max(c))