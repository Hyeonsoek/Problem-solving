from collections import defaultdict

n, m = map(int, input().split())
strings = defaultdict(list)

for _ in range(m):
    index, time, key = input().split()
    strings[int(time)].append((int(index), key))

result = ''
for key, value in sorted(strings.items()):
    if value:
        result += ''.join(list(zip(*sorted(value)))[1])
    
print(result)