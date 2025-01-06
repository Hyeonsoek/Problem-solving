arr = [input() for _ in range(5)]
arr = list(zip(*arr))

s1, s2 = '.omln', 'owln.'

result = []
for x in arr:
    x = ''.join(x)
    if x == s1:
        result.append(s2)
    elif x == s2:
        result.append(s1)
    else:
        result.append(x)

print('\n'.join(map(lambda x: ''.join(x), zip(*result))))