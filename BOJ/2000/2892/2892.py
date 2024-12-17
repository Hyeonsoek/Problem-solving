n = int(input())
arr = [*map(lambda x: int(x, 16), input().split())]

dot = ord('.')
space = ord(' ')

result = ''
for x in range(n):
    xordot = arr[x] ^ dot
    xorspace = arr[x] ^ space
    if 48 <= xordot <= 57 or 48 <= xorspace <= 57:
        result += '.'
    else:
        result += '-'

print(result)