import string

left, right = input(), input()
n = len(left)

counts = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
character = { x : y for x, y in zip(string.ascii_uppercase, counts) }
cache = [[-1] * (2 * n + 1) for _ in range(2 * n + 1)]

for x in range(2 * n):
    cache[0][x] = character[right[x >> 1]] if x & 1 else character[left[x >> 1]]

for x in range(2 * n - 2):
    for y in range(2 * n - x - 1):
        cache[x + 1][y] = (cache[x][y] + cache[x][y + 1]) % 10
    
print(''.join(map(str, cache[2*n-2][:2])))