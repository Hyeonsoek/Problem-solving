n = int(input())
strings = list(input())

def swap(x, y):
    strings[x], strings[y] = strings[y], strings[x]

indexes = [[], []]
for x in range(n):
    if strings[x] in {'P', 'C'}:
        k = int(strings[x] == 'P')
        indexes[k].append(x)

for x in range(min(map(len, indexes))):
    xx, yy = indexes[0][x], indexes[1][x]
    swap(xx, yy)

print(''.join(strings))