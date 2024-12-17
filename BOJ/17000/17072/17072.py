n, m = map(int, input().split())
image = [[*map(int, input().split())] for _ in range(n)]
result = [['' for _ in range(m)] for _ in range(n)]

def intensity(r, g, b):
    return 2126 * r + 7152 * g + 722 * b

def toascii(intensity):
    if intensity < 510_000:
        return '#'
    elif intensity < 1_020_000:
        return 'o'
    elif intensity < 1_530_000:
        return '+'
    elif intensity < 2_040_000:
        return '-'
    else:
        return '.'

for x in range(n):
    for y in range(0, 3*m, 3):
        i = intensity(*image[x][y:y+3])
        result[x][y // 3] = toascii(i)

for x in range(n):
    print(''.join(result[x]))