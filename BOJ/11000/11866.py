k, n = map(int, input().split())
l = [i+1 for i in range(k)]

idx = 0
sequence = []
while l:
    idx += n-1
    if idx >= len(l):
        idx %= len(l)
    sequence.append(l.pop(idx))

print('<' + ', '.join(map(str, sequence)) + '>')