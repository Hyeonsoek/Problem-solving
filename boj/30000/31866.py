a, b = map(int, input().split())

rps = [1, 3, 4]
finger = {x:[] for x in range(6)}
finger[0] += [2] + rps
finger[2] += [5] + rps
finger[5] += [0] + rps

if b in finger[a]:
    print('>')
elif a in finger[b]:
    print('<')
else:
    print('=')