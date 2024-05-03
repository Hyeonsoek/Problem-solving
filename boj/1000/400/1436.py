t = []
for x in range(666, 3000000):
    if "666" in str(x):
        t.append(x)

t.sort()
print(t[int(input())-1])